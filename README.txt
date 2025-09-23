Zippy Archive Utility
=====================

A Python script to archive files from a directory and its subfolders into multiple, size-limited ZIP files.

--------------------
REQUIREMENTS
--------------------
- Python 3.6+ installed and accessible from the command line.
- OS: Tested on Windows only. The `run_zippy.bat` script is Windows-specific.

--------------------
SETUP
--------------------
- Place zippy.py and run_zipper.bat in the same folder.

--------------------
USAGE
--------------------

Easy Method (run_zippy.bat):
Drag a folder onto the run_zippy.bat file.  You will be prompted to choose an archiving mode and configure the relevant settings.
Archives will be saved in a new "archives[folder_name]" folder created next to the script. 
1. Context Mode: Groups files by type, combines their text into large .txt files, and then zips those text files.
2. Direct Mode: Zips your original files directly into archives, preserving the folder structure.

Advanced Method (Command Line):
The script supports two modes ('direct' and 'context') controlled via arguments.
Use the format: python zippy.py [folder_path] --mode [mode] [options]
Run "python zippy.py -h" for details on all options. 



--------------------
CONFIGURATION
--------------------

- To change default settings (files per archive, etc.), edit the variables at the top of the run_zippy.bat file.

- To exclude more file types, add their extensions to the EXCLUDED_EXTENSIONS set inside the zippy.py script.


--------------------
USE CASES
--------------------

Context Mode: Ideal for preparing large sets of text-based files for analysis.


- AI/LLM Data Preparation: Consolidate an entire codebase or set of documents into a few large text files. This makes it easy to copy-paste the contents into a Large Language Model for analysis, summarization, or training. 

- Codebase Review: Create a "flat" representation of your project's code (e.g., all .py files) in a single document, making it simple to search and analyze without navigating the directory structure. 

- Project Documentation: Combine all project documentation files (.txt, .md, etc.) into one searchable context file.


Direct Mode: Standard file archiving for backup and transfer. 

- Project Backup: Create size-limited archives of a project folder, useful for storing on systems with file size restrictions.

- Easy File Transfer: Break down a large directory into smaller, more manageable ZIP files for easier uploading or sharing.

- Version Snapshots: Quickly create a complete, versioned archive of your project's state while preserving the original folder structure. 