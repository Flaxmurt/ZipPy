Zippy Archive Utility
=====================

A Python script to archive files from a directory and its subfolders into multiple, size-limited ZIP files.

--------------------
REQUIREMENTS
--------------------
- Python 3.6+ installed and accessible from the command line.

--------------------
SETUP
--------------------
- Place zippy.py and run_zipper.bat in the same folder.

--------------------
USAGE
--------------------

Easy Method (run_zipper.bat):
Drag a folder onto the run_zipper.bat file. Enter the number of files per archive when prompted. Archives will be saved in a new "_archives_[folder_name]" folder created next to the script.

Advanced Method (Command Line):
Use the format: python zippy.py [folder_path] -s [size] -o [output_path]
Run "python zippy.py -h" for details on all options.

--------------------
CONFIGURATION
--------------------

- To change default settings (files per archive, etc.), edit the variables at the top of the run_zipper.bat file.

- To exclude more file types, add their extensions to the EXCLUDED_EXTENSIONS set inside the zippy.py script.