#!/bin/bash

# Anagnostakis Yiannis (rizitis.github.io)
# License: MIT

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <folder1> [<folder2> ...] or $0 <folders.txt>"
    exit 1
fi

# Add yours...;)
REPO_OWNER="rizitis"
REPO_NAME="One4All_SlackBuild"
BRANCH="main"

# Function to download files from a folder
download_folder() {
    local FOLDER_PATH="$1"
    local DOWNLOAD_PATH="$2"

    echo "Processing folder: $FOLDER_PATH"

    # Fetch the list of files and folders in the directory
    CONTENTS=$(curl -s "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${FOLDER_PATH}?ref=${BRANCH}")

    # Check if curl succeeded
    if [ $? -ne 0 ]; then
        echo "Failed to fetch contents from GitHub for folder: $FOLDER_PATH"
        return 1
    fi

    # Download files
    echo "$CONTENTS" | jq -r '.[] | select(.type == "file") | .download_url' | while read -r FILE_URL; do
        FILE_NAME=$(basename "$FILE_URL")
        echo "Downloading file: ${DOWNLOAD_PATH}/${FILE_NAME}"
        curl -L -o "${DOWNLOAD_PATH}/${FILE_NAME}" "$FILE_URL"
        # Check if curl succeeded
        if [ $? -ne 0 ]; then
            echo "Failed to download file: $FILE_URL"
        fi
    done

    # Process subdirectories
    echo "$CONTENTS" | jq -r '.[] | select(.type == "dir") | .path' | while read -r SUBDIR_PATH; do
        DIR_NAME=$(basename "$SUBDIR_PATH")
        mkdir -p "${DOWNLOAD_PATH}/${DIR_NAME}"
        # Check if directory creation succeeded
        if [ $? -ne 0 ]; then
            echo "Failed to create directory: ${DOWNLOAD_PATH}/${DIR_NAME}"
            continue
        fi
        download_folder "$SUBDIR_PATH" "${DOWNLOAD_PATH}/${DIR_NAME}"
    done
}

# Check if the first argument is a file
if [ -f "$1" ]; then
    # Read folder names from the text file
    FOLDER_FILE="$1"
    shift
    while IFS= read -r FOLDER; do
        # Skip empty lines
        [ -z "$FOLDER" ] && continue
        mkdir -p "$FOLDER"
        # Check if directory creation succeeded
        if [ $? -ne 0 ]; then
            echo "Failed to create directory: $FOLDER"
            continue
        fi
        download_folder "$FOLDER" "$FOLDER"
    done < "$FOLDER_FILE"
else
    # If no text file, use command-line arguments
    for FOLDER in "$@"; do
        mkdir -p "$FOLDER"
        # Check if directory creation succeeded
        if [ $? -ne 0 ]; then
            echo "Failed to create directory: $FOLDER"
            continue
        fi
        download_folder "$FOLDER" "$FOLDER"
    done
fi

echo "All downloads complete. Happy hack."
