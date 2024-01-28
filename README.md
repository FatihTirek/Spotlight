# Windows Spotlight Image Extractor
The Windows Spotlight Image Extractor is a Python script designed to extract images from the Windows Spotlight assets directory and save them to the default Windows "Saved Pictures" directory. Additionally, it provides functionality to rename the extracted images in a sequential manner.

## Features
• Image Extraction: Extracts images from the Windows Spotlight assets directory.  
• Image Size Filter: Filters out images based on a specified size threshold (default threshold: 400 KB).  
• Image Renaming: Optionally renames extracted images in a sequential manner, with user-defined base name.  

## Note
• Ensure that the script has appropriate permissions to access the Windows Spotlight assets directory and the destination directory for extracted images.  
• Images are filtered based on their file size, with a default threshold of 400 KB. You can adjust this threshold as needed by modifying the `file_size` condition in the `main()` function.  
