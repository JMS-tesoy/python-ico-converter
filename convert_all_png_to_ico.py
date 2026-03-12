from PIL import Image
import os
from pathlib import Path
import argparse

def main():
    """
    Converts all supported images from a source folder to .ico files
    in a destination folder.
    """
    parser = argparse.ArgumentParser(description="Batch convert images to the .ico format.")
    parser.add_argument("-s", "--source", type=Path, default="Raw File", help="Source folder containing images (default: Raw File)")
    parser.add_argument("-d", "--dest", type=Path, default="Icon File", help="Destination folder for .ico files (default: Icon File)")
    args = parser.parse_args()

    # --- Configuration ---
    source_folder: Path = args.source
    destination_folder: Path = args.dest
    valid_extensions = (".png", ".jpg", ".jpeg")
    # Added 256x256 for modern high-DPI displays
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # Create folders if they don't exist
    source_folder.mkdir(exist_ok=True)
    destination_folder.mkdir(exist_ok=True)

    success_count = 0
    failure_count = 0

    # Find all supported image files in the source directory
    files_to_process = [
        f for f in source_folder.iterdir()
        if f.is_file() and f.suffix.lower() in valid_extensions
    ]

    if not files_to_process:
        print(f"No images found in '{source_folder}' to convert.")
        print("Please add .png, .jpg, or .jpeg files and run again.")
        return

    print(f"Found {len(files_to_process)} image(s) to convert...")

    # Convert all supported files
    for source_path in files_to_process:
        ico_name = source_path.stem + ".ico"
        destination_path = destination_folder / ico_name

        try:
            # Use a context manager to ensure the image file is properly closed
            with Image.open(source_path) as img:
                img.save(destination_path, format='ICO', sizes=ico_sizes)
            print(f"✅ Converted: {source_path.name} → {ico_name}")
            success_count += 1
        except Exception as e:
            print(f"❌ Failed to convert {source_path.name}: {e}")
            failure_count += 1

    print("\n--- Conversion Summary ---")
    print(f"Total files processed: {len(files_to_process)}")
    print(f"✅ Successful: {success_count}")
    if failure_count > 0:
        print(f"❌ Failed: {failure_count}")
    print("--------------------------")

if __name__ == "__main__":
    main()
