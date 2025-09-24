# Zippy Archive Utility

A robust Python tool to archive files from a directory and its subfolders into multiple, size-limited ZIP files. It is designed to handle large sets of files efficiently by segmenting directories into manageable archives.

This tool is ideal for preparing text-based datasets for analysis, creating project backups, or splitting large directories for easier transfer.

---

## Features

-   **Folder-Based Processing**: Archive an entire directory and its subfolders in one operation.
-   **Multiple Archiving Modes**:
    1.  **Context Mode**: Groups files by type, merges their contents into `.txt` files, and compresses those generated text files.
    2.  **Direct Mode**: Compresses the original files directly into ZIP archives while preserving the folder structure.
-   **Configurable Output**: Control how many files go into each ZIP and set maximum sizes for context files.
-   **Interactive Interface**: The `run_zippy.bat` script provides a simple menu-driven interface for Windows users.
-   **Customizable Exclusions**: Exclude specific file types by editing the extension list in `zippy.py`.

---

## Requirements

-   **Python 3.6+**: Must be installed and accessible from the command line (`python`).
-   **OS**: Tested on Windows. The `run_zippy.bat` script is Windows-specific.

---

## Usage

1.  **Place Files**: Ensure `zippy.py` and `run_zippy.bat` are in the same directory.
2.  **Prepare Data**: Put all the files you want to process into a single folder.
3.  **Run**: Drag and drop that folder onto the `run_zippy.bat` file.
4.  **Select Mode**: Choose one of the processing modes from the on-screen menu.

The script will begin processing, and all output ZIPs will be created in folders alongside the script.

---

## Use Cases

-   **AI/LLM Data Preparation**: Convert large sets of text files into structured, compressed datasets.
-   **Bulk Backups**: Segment large projects or directories into smaller archives for long-term storage.
-   **File Transfer**: Break down oversized directories into size-limited ZIP files for easier transport.
-   **Selective Archiving**: Exclude unnecessary file types and archive only what matters.

---

## Getting Help

If you encounter a bug or have a feature request, please open an issue on the GitHub repository.

---

## Contributing

Contributions are welcome. Please read the `CONTRIBUTING.md` file for guidelines on how to submit pull requests.
