import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Base URL for the directory listing
base_url = "https://www.freedesktop.org/software/"

# Function to fetch and parse the directory listing
def fetch_directory_listing(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch directory listing.")
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract valid folder links
def extract_folders(soup):
    folders = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('/') and '?' not in href and href != "Parent Directory":
            folders.append(href)
    return folders

# Function to extract valid file links
def extract_files(soup):
    files = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if not href.endswith('/') and '?' not in href:
            files.append(href)
    return files

# Function to find the latest compressed file in a list of files
def find_latest_compressed_file(files):
    compressed_files = [file for file in files if file.endswith('.tar.xz') or file.endswith('.tar.gz')]

    if not compressed_files:
        return None  # No compressed files found

    # Get the latest compressed file
    return compressed_files[-1]

# Recursive function to search for compressed files in subfolders
def search_in_subfolders(base_url, max_depth=5):
    def recursive_search(url, depth=0):
        if depth > max_depth:
            return None, None  # Prevent infinite recursion
        
        print(f"Searching in: {url}")

        # Fetch and parse the directory listing
        soup = fetch_directory_listing(url)

        # Extract files and subfolders
        files = extract_files(soup)
        subfolders = extract_folders(soup)

        # Find the latest compressed file
        latest_compressed_file = find_latest_compressed_file(files)

        if latest_compressed_file:
            return latest_compressed_file, url

        # If no compressed file, check in subfolders
        for subfolder in subfolders:
            subfolder_url = urljoin(url, subfolder)
            if subfolder_url.startswith(base_url):
                result = recursive_search(subfolder_url, depth + 1)
                if result:
                    return result

        return None, None

    return recursive_search(base_url)

# Fetch the main directory listing
soup = fetch_directory_listing(base_url)

# Extract folders
folders = extract_folders(soup)

# List available folders
print("Available folders:")
for idx, folder in enumerate(folders, start=1):
    print(f"{idx}. {folder}")

# Ask the user to choose a folder
choice = int(input("Choose a folder to explore (number): "))
if not (1 <= choice <= len(folders)):
    raise Exception("Invalid choice. Exiting.")

chosen_folder = folders[choice - 1]

# Get the full URL of the chosen folder
folder_url = urljoin(base_url, chosen_folder)

# Fetch the content of the chosen folder
soup = fetch_directory_listing(folder_url)

# Extract files and subfolders
files = extract_files(soup)
subfolders = extract_folders(soup)

# Check for compressed files in the main folder
latest_compressed_file = find_latest_compressed_file(files)

# If no compressed file, search in subfolders
if not latest_compressed_file:
    print("No .tar.xz or .tar.gz files found in the selected folder.")
    
    if subfolders:
        print("Available subfolders:")
        for subfolder in subfolders:
            print(f"- {subfolder}")

        explore_choice = input("Do you want to search in subfolders for compressed files? (yes/no): ").strip().lower()
        if explore_choice == "yes":
            latest_compressed_file, folder_path = search_in_subfolders(folder_url)

    if latest_compressed_file:
        # Download the found compressed file
        download_url = urljoin(folder_path, latest_compressed_file)

        download_directory = "downloads"
        os.makedirs(download_directory, exist_ok=True)
        file_path = os.path.join(download_directory, latest_compressed_file)

        print(f"Downloading {latest_compressed_file} from {download_url} to {file_path}")

        response = requests.get(download_url, stream=True)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print("Download completed.")
    else:
        print("No compressed files found after searching. Exiting.")

else:
    # If compressed files are found in the main folder
    download_url = urljoin(folder_url, latest_compressed_file)

    download_directory = "downloads"
    os.makedirs(download_directory, exist_ok=True)
    file_path = os.path.join(download_directory, latest_compressed_file)

    print(f"Downloading {latest_compressed_file} from {download_url} to {file_path}")

    response = requests.get(download_url, stream=True)
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Download completed.")

