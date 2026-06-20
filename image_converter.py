from pathlib import Path
import argparse
from converter import DEFAULT_ICO_SIZES, convert_images_in_folder

def parse_icon_sizes(size_text):
    """
    Parses comma-separated icon sizes, such as "16,32,256".
    """
    try:
        sizes = [int(size.strip()) for size in size_text.split(",") if size.strip()]
    except ValueError:
        raise argparse.ArgumentTypeError("Sizes must be comma-separated numbers, like 16,32,256.")

    if not sizes:
        raise argparse.ArgumentTypeError("At least one icon size is required.")

    if any(size <= 0 for size in sizes):
        raise argparse.ArgumentTypeError("Icon sizes must be positive numbers.")

    return sizes

def main():
    """
    Converts all supported images from a source folder to .ico files
    in a destination folder.
    """
    parser = argparse.ArgumentParser(description="Batch convert images to the .ico format.")
    parser.add_argument("-s", "--source", type=Path, default="Raw File", help="Source folder containing images (default: Raw File)")
    parser.add_argument("-d", "--dest", type=Path, default="Icon File", help="Destination folder for .ico files (default: Icon File)")
    parser.add_argument(
        "--sizes",
        type=parse_icon_sizes,
        default=list(DEFAULT_ICO_SIZES),
        help="Comma-separated icon sizes in pixels (default: 16,32,48,64,128,256)",
    )
    args = parser.parse_args()

    # The core logic is now handled by the shared converter module.
    convert_images_in_folder(str(args.source), str(args.dest), pixel_sizes=args.sizes)

if __name__ == "__main__":
    main()
