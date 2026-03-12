# Python ICO Converter

A simple and efficient utility to batch convert image files (`.png`, `.jpg`, `.jpeg`) into multi-resolution `.ico` files.

This script is perfect for developers and designers who need to quickly generate high-quality icons for applications, websites, or favicons from standard image sources.

## Features

- **Graphical User Interface**: Easy-to-use interface for selecting folders and viewing progress.
- **Portable Application**: Can be bundled into a single `.exe` file that runs anywhere on Windows without installation.
- **Batch Conversion**: Convert all supported images in a directory at once.
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
    pip install -r requirements.txt
    ```

## Usage

### GUI Application (Recommended)

Run the `app_ui.py` script. Use "Browse" to upload your source image file, click "Convert to ICO", and then click "Download ICO" to save the result.

```sh
python app_ui.py
```

### Command-Line (Legacy)

```sh
# Use default folders ('Raw File/' and 'Icon File/')
python image_converter.py

# Specify custom source and destination folders
python image_converter.py --source "path/to/your/images" --dest "path/for/your/icons"
```