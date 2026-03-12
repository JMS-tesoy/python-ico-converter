from PIL import Image
from pathlib import Path
from typing import Callable, Optional

def convert_images_in_folder(
    source_folder_str: str,
    dest_folder_str: str,
    log_callback: Optional[Callable[[str], None]] = None,
):
    """
    Converts images from a source folder to .ico files.

    Args:
        source_folder_str: Path to the source folder as a string.
        dest_folder_str: Path to the destination folder as a string.
        log_callback: An optional function to call for logging progress.
                      If None, progress will be printed to the console.
    """
    # Use a default print logger if no callback is provided
    logger = log_callback if log_callback is not None else print

    try:
        source_folder = Path(source_folder_str)
        destination_folder = Path(dest_folder_str)
        valid_extensions = (".png", ".jpg", ".jpeg")
        ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

        # Create folders if they don't exist
        source_folder.mkdir(exist_ok=True)
        destination_folder.mkdir(exist_ok=True)

        success_count = 0
        failure_count = 0
        skipped_count = 0

        files_to_process = [
            f for f in source_folder.iterdir()
            if f.is_file() and f.suffix.lower() in valid_extensions
        ]

        if not files_to_process:
            logger("No images found in the source folder to convert.")
            return

        logger(f"Found {len(files_to_process)} image(s) to convert...")

        for source_path in files_to_process:
            ico_name = source_path.stem + ".ico"
            destination_path = destination_folder / ico_name

            if destination_path.exists():
                logger(f"⏭️  Skipped: {ico_name} already exists.")
                skipped_count += 1
                continue

            try:
                with Image.open(source_path) as img:
                    img.save(destination_path, format="ICO", sizes=ico_sizes)
                logger(f"✅ Converted: {source_path.name} → {ico_name}")
                success_count += 1
            except Exception as e:
                logger(f"❌ Failed to convert {source_path.name}: {e}")
                failure_count += 1

        logger("\n--- Conversion Summary ---")
        logger(f"✅ Successful: {success_count}")
        if skipped_count > 0:
            logger(f"⏭️  Skipped: {skipped_count}")
        if failure_count > 0:
            logger(f"❌ Failed: {failure_count}")
        logger("--------------------------")

    except Exception as e:
        logger(f"An unexpected error occurred: {e}")

def convert_single_file(
    source_file_str: str,
    dest_folder_str: str,
    log_callback: Optional[Callable[[str], None]] = None,
):
    """
    Converts a single image file to an .ico file.

    Args:
        source_file_str: Path to the source image file as a string.
        dest_folder_str: Path to the destination folder as a string.
        log_callback: An optional function to call for logging progress.
                      If None, progress will be printed to the console.
    """
    logger = log_callback if log_callback is not None else print

    try:
        source_path = Path(source_file_str)
        destination_folder = Path(dest_folder_str)
        valid_extensions = (".png", ".jpg", ".jpeg")
        ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

        if not source_path.is_file() or source_path.suffix.lower() not in valid_extensions:
            logger(f"❌ Invalid file: Please select a .png, .jpg, or .jpeg file.")
            return

        destination_folder.mkdir(exist_ok=True)

        ico_name = source_path.stem + ".ico"
        destination_path = destination_folder / ico_name

        logger(f"Starting conversion for {source_path.name}...")

        with Image.open(source_path) as img:
            img.save(destination_path, format="ICO", sizes=ico_sizes)
        logger(f"✅ Converted: {source_path.name} → {ico_name}")

    except Exception as e:
        logger(f"❌ Failed to convert {source_path.name}: {e}")