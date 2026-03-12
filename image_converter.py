from pathlib import Path
import argparse
from converter import convert_images_in_folder

def main():
    """
    Converts all supported images from a source folder to .ico files
    in a destination folder.
    """
    parser = argparse.ArgumentParser(description="Batch convert images to the .ico format.")
    parser.add_argument("-s", "--source", type=Path, default="Raw File", help="Source folder containing images (default: Raw File)")
    parser.add_argument("-d", "--dest", type=Path, default="Icon File", help="Destination folder for .ico files (default: Icon File)")
    args = parser.parse_args()

    # The core logic is now handled by the shared converter module.
    convert_images_in_folder(str(args.source), str(args.dest))

if __name__ == "__main__":
    main()
