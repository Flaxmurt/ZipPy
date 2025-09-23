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