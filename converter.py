from PIL import Image
from pathlib import Path
from typing import Callable, Optional

DEFAULT_ICO_SIZES = (16, 32, 48, 64, 128, 256)

def build_ico_sizes(pixel_sizes=None):
    """
    Builds Pillow-compatible ICO size tuples from selected pixel widths.

    Args:
        pixel_sizes: Optional iterable of integer pixel sizes. If omitted,
                     standard Windows icon sizes are used.
    """
    sizes = pixel_sizes if pixel_sizes is not None else DEFAULT_ICO_SIZES
    clean_sizes = sorted({int(size) for size in sizes if int(size) > 0})

    if not clean_sizes:
        raise ValueError("Please select at least one icon size.")

    return [(size, size) for size in clean_sizes]

def prepare_square_icon_image(image, size):
    """
    Fits an image onto a transparent square canvas for ICO generation.
    """
    image = image.convert("RGBA")
    width, height = image.size
    scale = min(size / width, size / height)
    resized_size = (
        max(1, round(width * scale)),
        max(1, round(height * scale)),
    )
    resized_image = image.resize(resized_size, Image.LANCZOS)

    icon_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    paste_position = (
        (size - resized_size[0]) // 2,
        (size - resized_size[1]) // 2,
    )
    icon_image.paste(resized_image, paste_position, resized_image)
    return icon_image

def convert_images_in_folder(
    source_folder_str: str,
    dest_folder_str: str,
    log_callback: Optional[Callable[[str], None]] = None,
    pixel_sizes=None,
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
        ico_sizes = build_ico_sizes(pixel_sizes)

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
                logger(f"Skipped: {ico_name} already exists.")
                skipped_count += 1
                continue

            try:
                with Image.open(source_path) as img:
                    icon_image = prepare_square_icon_image(img, max(size[0] for size in ico_sizes))
                    icon_image.save(destination_path, format="ICO", sizes=ico_sizes)
                logger(f"Converted: {source_path.name} -> {ico_name}")
                success_count += 1
            except Exception as e:
                logger(f"Failed to convert {source_path.name}: {e}")
                failure_count += 1

        logger("\n--- Conversion Summary ---")
        logger(f"Successful: {success_count}")
        if skipped_count > 0:
            logger(f"Skipped: {skipped_count}")
        if failure_count > 0:
            logger(f"Failed: {failure_count}")
        logger("--------------------------")

    except Exception as e:
        logger(f"An unexpected error occurred: {e}")

def convert_single_file(
    source_file_str: str,
    dest_folder_str: str,
    log_callback: Optional[Callable[[str], None]] = None,
    pixel_sizes=None,
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
        ico_sizes = build_ico_sizes(pixel_sizes)

        if not source_path.is_file() or source_path.suffix.lower() not in valid_extensions:
            logger("Invalid file: Please select a .png, .jpg, or .jpeg file.")
            return

        destination_folder.mkdir(exist_ok=True)

        ico_name = source_path.stem + ".ico"
        destination_path = destination_folder / ico_name

        logger(f"Starting conversion for {source_path.name}...")

        with Image.open(source_path) as img:
            icon_image = prepare_square_icon_image(img, max(size[0] for size in ico_sizes))
            icon_image.save(destination_path, format="ICO", sizes=ico_sizes)
        logger(f"Converted: {source_path.name} -> {ico_name}")

    except Exception as e:
        logger(f"Failed to convert {source_path.name}: {e}")
