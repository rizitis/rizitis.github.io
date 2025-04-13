import requests
import os
import argparse

# Define repository owner and name
repo_owner = "rizitis"
repo_name = "Slackware-Commander"

# Get the latest release information
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
response = requests.get(api_url)
latest_release = response.json()

# Check if the response is valid
if 'assets' not in latest_release:
    print("Error retrieving assets. Please check the repository details.")
    exit(1)

# Get the release tag name
tag_name = latest_release.get("tag_name", "unknown")

# Construct the auto-generated source URLs
source_zip_url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/tags/{tag_name}.zip"
source_tar_url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/tags/{tag_name}.tar.gz"

# List available assets including source code archives
assets = latest_release.get("assets", [])

# Add auto-generated source code archives to the list of assets
assets.append({
    "name": f"{repo_name}-{tag_name}.zip",
    "browser_download_url": source_zip_url
})

assets.append({
    "name": f"{repo_name}-{tag_name}.tar.gz",
    "browser_download_url": source_tar_url
})

# Set up command-line arguments with argparse
parser = argparse.ArgumentParser(description='Download assets from the latest GitHub release.')
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

