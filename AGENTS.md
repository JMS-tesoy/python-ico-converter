# Repository Guidelines

## Project Structure & Module Organization
This is a command-line utility for batch converting image files to the `.ico` format.
- `convert_all_png_to_ico.py`: The main script that handles argument parsing and image conversion.
- `Raw File/`: The default source directory for input images.
- `Icon File/`: The default destination directory for generated `.ico` files.

## Build, Test, and Development Commands
The script depends on the **Pillow** (`PIL`) library. Ensure it is installed:
```sh
pip install Pillow
```

To run the script with default folders (`Raw File/` and `Icon File/`):
```sh
python convert_all_png_to_ico.py
```

To specify custom source and destination folders:
```sh
python convert_all_png_to_ico.py --source "path/to/your/images" --dest "path/for/your/icons"
```

## Testing Guidelines
No automated test suite is currently implemented. Verification is performed by checking the contents of the `Icon File/` directory after execution.
