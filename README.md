# Zippy Archive Utility

[cite_start]A Python utility to archive files from a directory and its subfolders into multiple, size-limited ZIP files. [cite: 16]

[cite_start]This tool is ideal for preparing large sets of text-based files for analysis [cite: 27][cite_start], creating project backups [cite: 32][cite_start], or segmenting large directories for easier file transfer[cite: 33].

---

## Features

-   [cite_start]**Folder-Based Processing**: Archives an entire directory and its subfolders with a single operation. [cite: 16]
-   [cite_start]**Multiple Archiving Modes**: The script supports two distinct modes of operation. [cite: 23]
    1.  [cite_start]**Context Mode**: Groups files by type, combines their contents into large `.txt` files, and then zips those generated text files. [cite: 21]
    2.  [cite_start]**Direct Mode**: Zips the original files directly into archives while preserving the original folder structure. [cite: 22]
-   [cite_start]**Configurable Output**: Control the number of files per ZIP archive and, in context mode, the maximum size of each generated text file. [cite: 25]
-   [cite_start]**Interactive Interface**: A `run_zippy.bat` file provides a simple, interactive menu for Windows users. [cite: 19]
-   [cite_start]**Customizable Exclusions**: File types can be excluded from the archive by adding their extensions to a set within the `zippy.py` script. [cite: 26]

---

## Requirements

-   [cite_start]**Python 3.6+**: Must be installed and accessible from the command line. [cite: 17]
-   [cite_start]**OS**: Tested on Windows. [cite: 17] [cite_start]The `run_zippy.bat` script is Windows-specific. [cite: 18]

---

## Usage

1.  **Place Files**: Ensure `zippy.py` and `run_zippy.bat` are in the same directory.
2.  [cite_start]**Run**: Drag and drop the folder you want to process onto the `run_zippy.bat` file. [cite: 19]
3.  [cite_start]**Select Mode**: Choose one of the archiving modes from the on-screen menu and configure the settings as prompted. [cite: 19]

[cite_start]The script will begin processing, and all output will be placed in a new `_archives_[folder_name]` folder created in the same directory as the script. [cite: 20]

---

## Use Cases

-   [cite_start]**AI/LLM Data Preparation**: Consolidate an entire codebase or set of documents into a few large text files, making them easy to copy into a Large Language Model for analysis or training. [cite: 28, 29]
-   [cite_start]**Codebase Review**: Create a "flat" representation of your project's code (e.g., all `.py` files) in a single document, which simplifies searching and analysis. [cite: 30]
-   [cite_start]**Project Backup**: Create size-limited archives of a project folder, which is useful for storing on systems with file size restrictions. [cite: 32]
-   [cite_start]**Easy File Transfer**: Break down a large directory into smaller, more manageable ZIP files for easier uploading or sharing. [cite: 33]

---

## Contributing

Contributions are welcome. Please read the `CONTRIBUTING.md` file for guidelines on how to submit bug reports, feature requests, and pull requests.