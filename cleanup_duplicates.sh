#!/bin/bash

# Remove duplicate files from root directory
rm -f get_all_languages.py
rm -f index.html

echo "Duplicate files removed from root directory."
echo "Files are now organized properly:"
echo "- get_all_languages.py is only in the backend/ directory"
echo "- index.html is only in the frontend/ directory"