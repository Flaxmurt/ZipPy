import argparse
import logging
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Literal, Union

# File extensions to ignore during the scan.
EXCLUDED_EXTENSIONS = {
    '.zip', '.7z', 'rar', '.tar', '.gz', '.log', '.tmp', '.exe', '.dll'
}


def setup_logging():
    """Sets up simple logging to show script progress in the console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout,
    )


def find_files(src_path: Path, mode: Literal['direct', 'context']) -> Union[Dict[str, List[Path]], List[Path]]:
    """
    Finds and returns files from a source path based on the chosen mode.

    In 'direct' mode, returns a flat list of all files.
    In 'context' mode, returns files grouped by extension in a dictionary.
    """
    script_path = Path(sys.argv[0]).resolve()
    logging.info(f"Scanning '{src_path}' for files...")

    if mode == 'context':
        grouped_files = defaultdict(list)
        all_files_gen = src_path.rglob('*')
        for file_path in all_files_gen:
            if not file_path.is_file():
                continue
            if file_path.resolve() == script_path:
                continue
            if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
                continue

            key = file_path.suffix.lower() if file_path.suffix else 'no_extension'
            grouped_files[key].append(file_path)

        total_files = sum(len(v) for v in grouped_files.values())
        for ext in grouped_files:
            grouped_files[ext].sort()

        logging.info(f"Found and grouped {total_files} files into {len(grouped_files)} types.")
        return grouped_files
    else:  # direct mode
        direct_files = []
        for file_path in src_path.rglob('*'):
            if not file_path.is_file():
                continue
            if file_path.resolve() == script_path:
                continue
            if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
                continue
            direct_files.append(file_path)

        direct_files.sort()
        logging.info(f"Found {len(direct_files)} files to archive directly.")
        return direct_files


def create_context_files(
    grouped_files: Dict[str, List[Path]], output_path: Path, src_path: Path, max_size_mb: float
) -> List[Path]:
    """Combines grouped files into large text files, splitting by size."""
    context_files = []
    max_size_bytes = max_size_mb * 1024 * 1024
    logging.info(f"Creating context files in '{output_path}' with a max size of {max_size_mb} MB each...")

    for ext, files in grouped_files.items():
        part_num = 1
        current_size = 0
        outfile = None
        base_filename_stem = f"{ext[1:] if ext.startswith('.') else ext}_context"

        for file_path in files:
            try:
                file_size = file_path.stat().st_size
            except FileNotFoundError:
                continue

            if outfile and (current_size + file_size) > max_size_bytes and current_size > 0:
                outfile.close()
                outfile = None
                part_num += 1
                current_size = 0

            if outfile is None:
                context_filename = f"{base_filename_stem}_{part_num}.txt"
                context_filepath = output_path / context_filename
                logging.info(f"  -> Opening new context file '{context_filename}'...")
                outfile = open(context_filepath, 'w', encoding='utf-8', errors='replace')
                context_files.append(context_filepath)

            separator = f"\n{'='*25} START: {file_path.relative_to(src_path)} {'='*25}\n\n"
            outfile.write(separator)
            try:
                content = file_path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                content = file_path.read_text(encoding='latin-1', errors='replace')
                logging.warning(f"    - Used fallback encoding for '{file_path.name}'")
            outfile.write(content)
            current_size += file_size

        if outfile:
            outfile.close()

    return context_files


def create_archives(files: List[Path], output_path: Path, chunk_size: int, prefix: str, src_path: Path, mode: str):
    """Zips the provided files into one or more archives."""
    if not files:
        logging.info("No files to archive.")
        return

    num_archives = (len(files) + chunk_size - 1) // chunk_size
    logging.info(f"Creating {num_archives} archive(s)...")

    for i in range(0, len(files), chunk_size):
        chunk = files[i:i + chunk_size]
        archive_num = (i // chunk_size) + 1
        zip_filename = output_path / f'{prefix}_{archive_num}.zip'

        logging.info(f"Creating '{zip_filename}' with {len(chunk)} files...")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in chunk:
                # In direct mode, preserve relative paths. In context mode, add files to root.
                arcname = file_path.relative_to(src_path) if mode == 'direct' else file_path.name
                zipf.write(file_path, arcname)

    logging.info(f"Process complete. Created {num_archives} archive(s) in '{output_path}'.")


def main():
    """Parses arguments and runs the full file processing workflow."""
    parser = argparse.ArgumentParser(description="A versatile file archiver with multiple modes.")
    parser.add_argument("src_directory", nargs='?', default='.', help="The root directory to scan.")
    parser.add_argument("--mode", choices=['direct', 'context'], default='context', help="Archiving mode.")
    parser.add_argument("-s", "--size", type=int, default=10, help="Number of files or context files per ZIP archive.")
    parser.add_argument("--max-size", type=float, default=100.0, help="(Context Mode) Max size of each context file in MB.")
    parser.add_argument("-p", "--prefix", default='archive', help="Prefix for the output archive filenames.")

    args = parser.parse_args()
    setup_logging()

    src_path = Path(args.src_directory).resolve()
    script_dir = Path(sys.argv[0]).parent.resolve()

    # Define the output directory name as per the new requirement.
    output_path = script_dir / f"_archives_{src_path.name}"
    output_path.mkdir(parents=True, exist_ok=True)

    if args.mode == 'context':
        grouped_files = find_files(src_path, 'context')
        if grouped_files:
            context_files = create_context_files(grouped_files, output_path, src_path, args.max_size)
            create_archives(context_files, output_path, args.size, "context_project", src_path, 'context')
    else:  # direct mode
        direct_files = find_files(src_path, 'direct')
        if direct_files:
            create_archives(direct_files, output_path, args.size, "direct_project", src_path, 'direct')

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

