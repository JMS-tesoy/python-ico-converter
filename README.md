# Python ICO Converter

A simple and efficient command-line utility to batch convert image files (`.png`, `.jpg`, `.jpeg`) into multi-resolution `.ico` files.

This script is perfect for developers and designers who need to quickly generate high-quality icons for applications, websites, or favicons from standard image sources.

## Features

- **Batch Conversion**: Convert all supported images in a source directory at once.
- **Multi-Resolution Icons**: Creates `.ico` files with standard sizes (16x16, 32x32, 48x48, 64x64, 128x128, 256x256) for high-quality display across all platforms.
- **Flexible Paths**: Specify custom source and destination folders via command-line arguments.
- **Robust Error Handling**: Skips corrupted or unsupported files and provides a final summary of successful and failed conversions.

## Prerequisites

- Python 3.6+
- Pillow (the Python Imaging Library fork)

## Installation

1.  **Clone the repository (or download the script):**
    ```sh
    git clone https://github.com/JMS-tesoy/python-ico-converter.git
    cd python-ico-converter
    ```

2.  **Install the required library:**
    ```sh
    pip install Pillow
    ```

## Usage

Place your source images (`.png`, `.jpg`) into the `Raw File/` directory (or a folder of your choice).

Run the script from your terminal. The converted `.ico` files will be saved in the `Icon File/` directory.

```sh
# Use default folders ('Raw File/' and 'Icon File/')
python convert_all_png_to_ico.py

# Specify custom source and destination folders
python convert_all_png_to_ico.py --source "path/to/your/images" --dest "path/for/your/icons"
```