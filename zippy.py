import argparse
import logging
import sys
import zipfile
from pathlib import Path
from typing import List

# You can add more extensions to ignore.
EXCLUDED_EXTENSIONS = {'.zip', '.7z', '.rar', '.tar', '.gz', '.log', '.tmp'}

def setup_logging():
    """Configures basic logging to the console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout,
    )

def find_files_to_archive(src_path: Path) -> List[Path]:
    """
    Scans a directory and returns a sorted list of files to be archived.
    """
    script_path = Path(sys.argv[0]).resolve()
    files_found = []

    logging.info(f"Scanning '{src_path}' and its subdirectories for files...")
    
    for file_path in src_path.rglob('*'):
        if not file_path.is_file():
            continue
        if file_path == script_path:
            continue
        if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
            continue
        
        files_found.append(file_path)
    
    files_found.sort()
    return files_found

def create_archives(files: List[Path], src_path: Path, chunk_size: int, output_path: Path, prefix: str):
    """
    Creates ZIP archives from a list of files, splitting them into chunks.
    """
    if not files:
        logging.info("No files to archive.")
        return

    total_files = len(files)
    num_archives = (total_files + chunk_size - 1) // chunk_size
    logging.info(f"Found {total_files} files. Will create {num_archives} archive(s).")

    for i in range(0, total_files, chunk_size):
        file_chunk = files[i:i + chunk_size]
        archive_number = (i // chunk_size) + 1
        
        zip_filename = output_path / f'{prefix}_{archive_number}.zip'

        logging.info(f"Creating '{zip_filename}' with {len(file_chunk)} files...")
        
        try:
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in file_chunk:
                    arcname = file_path.relative_to(src_path)
                    zipf.write(file_path, arcname)
                    logging.debug(f"  -> Added '{arcname}'")
        except (IOError, OSError) as e:
            logging.error(f"Error creating '{zip_filename}': {e}")
            
    logging.info(f"Process complete. Created {num_archives} archive(s) in '{output_path}'.")

def main():
    """
    Main function to parse command-line arguments and run the zipping process.
    """
    parser = argparse.ArgumentParser(
        description="Scans a directory and its subdirectories to create ZIP archives in chunks.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "src_directory", nargs='?', default='.', help="The directory to scan."
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=10,
        help="Number of files per ZIP archive."
    )
    parser.add_argument(
        "-o", "--output", default='.', help="The output directory for archives."
    )
    parser.add_argument(
        "-p", "--prefix",
        default='archive',
        help="Prefix for the output archive filenames."
    )
    
    args = parser.parse_args()
    
    setup_logging()
    
    src_path = Path(args.src_directory).resolve()
    output_path = Path(args.output).resolve()
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    files_to_zip = find_files_to_archive(src_path)
    create_archives(files_to_zip, src_path, args.size, output_path, args.prefix)

if __name__ == "__main__":
    main()