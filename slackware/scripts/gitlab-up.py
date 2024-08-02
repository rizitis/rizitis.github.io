import requests
import os
import argparse

# Define your GitLab instance, project ID, or namespace/project
# Example with GitLab.com, replace 'your-namespace/your-project' with the appropriate values
gitlab_base_url = "https://gitlab.com"
project_path = "your-namespace/your-project"  # Use your project path

# Function to get the latest release info
def get_latest_release():
    # GitLab's releases API endpoint
    api_url = f"{gitlab_base_url}/api/v4/projects/{project_path.replace('/', '%2F')}/releases"
    response = requests.get(api_url)
    
    # Ensure valid response
    if response.status_code != 200:
        print("Error retrieving releases. Check the project path or URL.")
        exit(1)

    # GitLab returns a list of releases, with the most recent at the beginning
    releases = response.json()
    if not releases:
        print("No releases found.")
        exit(1)

    return releases[0]  # The latest release

# Get the latest release information
latest_release = get_latest_release()

# Get the release tag name
tag_name = latest_release.get("tag_name", "unknown")

print(f"Latest Release: {tag_name}")

# List available assets
assets = latest_release.get("assets", [])

# Construct auto-generated source code archive URLs (GitLab creates source code archives)
source_zip_url = f"{gitlab_base_url}/{project_path}/repository/archive.zip?ref={tag_name}"
source_tar_url = f"{gitlab_base_url}/{project_path}/repository/archive.tar.gz?ref={tag_name}"

# Add auto-generated source code archives to the list of assets
assets.append({
    "name": f"{project_path.replace('/', '-')}-{tag_name}.zip",
    "browser_download_url": source_zip_url,
})

assets.append({
    "name": f"{project_path.replace('/', '-')}-{tag_name}.tar.gz",
    "browser_download_url": source_tar_url,
})

# Set up command-line arguments with argparse
parser = argparse.ArgumentParser(description='Download assets from the latest GitLab release.')
parser.add_argument('-i', '--index', type=int, nargs='+', help='Indices of assets to download (e.g., -i 1 2 3)')
parser.add_argument('-s', '--source', choices=['zip', 'tar.gz'], help='Download source code (zip or tar.gz)')

args = parser.parse_args()

# Determine which assets to download based on command-line input
selected_indices = []

if args.index:
    selected_indices = [i - 1 for i in args.index]  # Convert to zero-based index

if args.source:
    if args.source == 'zip':
        selected_indices.append(len(assets) - 2)  # Index of the zip source code
    elif args.source == 'tar.gz':
        selected_indices.append(len(assets) - 1)  # Index of the tar.gz source code

# Download the chosen assets
for index in set(selected_indices):  # Use set to avoid duplicates
    if 0 <= index < len(assets):
        asset = assets[index]
        asset_url = asset["browser_download_url"]

        response = requests.get(asset_url, stream=True)

        # Set the file path where you'd like to save the asset
        file_name = asset["name"]
        file_path = os.path.join(os.getcwd(), file_name)

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded {file_name} to {file_path}")
    else:
        print(f"Invalid index: {index + 1}. Skipping...")

