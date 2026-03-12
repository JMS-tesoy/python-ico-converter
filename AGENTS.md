# Repository Guidelines for AI Agents & Developers

## Project Structure & Module Organization
This project provides a GUI application and a legacy command-line script for batch converting images to the `.ico` format.

- **`app_ui.py`**: The main graphical user interface application (recommended for users).
- **`image_converter.py`**: The legacy command-line script.
- **`requirements.txt`**: Lists Python dependencies for the project.

## Build, Test, and Development Commands
Dependencies are listed in `requirements.txt`. Install them with:
```sh
pip install -r requirements.txt
```

To run the script with default folders (`Raw File/` and `Icon File/`):
```sh
python image_converter.py
```

To specify custom source and destination folders:
```sh
python image_converter.py --source "path/to/your/images" --dest "path/for/your/icons"
```

## Testing Guidelines
No automated test suite is currently implemented. Verification is performed by checking the contents of the `Icon File/` directory after execution.
