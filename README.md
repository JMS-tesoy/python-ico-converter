# Python ICO Converter

A small Windows-friendly Python utility for converting `.png`, `.jpg`, and `.jpeg` images into `.ico` files. The project includes a graphical desktop app for normal use and a legacy command-line script for batch conversion.

## Features

- GUI image upload with Browse and drag-and-drop support.
- Selectable icon pixel sizes: `16x16`, `32x32`, `48x48`, `64x64`, `128x128`, and `256x256`.
- Transparent square padding for non-square source images, so selected icon sizes are generated as true square frames.
- Batch conversion through the command line.
- Custom source and destination folders for CLI usage.
- Portable `.exe` build process through PyInstaller.

## Project Structure

- `app_ui.py`: Main graphical application.
- `converter.py`: Shared conversion logic used by both GUI and CLI.
- `image_converter.py`: Command-line batch converter.
- `requirements.txt`: Python package dependencies.
- `install.bat`: Installs dependencies from `requirements.txt`.
- `run_gui.bat`: Starts the GUI app.
- `run_cli.bat`: Runs the CLI converter with default folders.
- `build.bat`: Builds a standalone Windows executable.
- `Raw File/`: Default source folder for CLI conversion.
- `Icon File/`: Default output folder for CLI conversion.
- `USERGUIDE.md`: End-user guide, including usage and build instructions.

## Requirements

- Python 3.10+ recommended
- pip
- Windows PowerShell or Command Prompt

Install dependencies:

```powershell
pip install -r requirements.txt
```

Or run:

```powershell
.\install.bat
```

## Run the GUI

```powershell
python app_ui.py
```

Or run:

```powershell
.\run_gui.bat
```

In the GUI, choose an image, select the icon sizes you want, click **Convert to ICO**, then click **Save to...**.

## Run the CLI

Use the default folders:

```powershell
python image_converter.py
```

Use custom folders:

```powershell
python image_converter.py --source "path\to\images" --dest "path\to\icons"
```

Choose specific icon sizes:

```powershell
python image_converter.py --source "Raw File" --dest "Icon File" --sizes 16,32,256
```

## Build the Windows Executable

Install PyInstaller if needed:

```powershell
pip install pyinstaller
```

Then run:

```powershell
.\build.bat
```

The build script creates a standalone executable at:

```text
dist\IconConverter.exe
```

## Testing

There is no automated test suite yet. Manual verification is recommended:

- Start the GUI with `python app_ui.py`.
- Convert a PNG or JPG with only one or two sizes selected.
- Save the `.ico` file.
- Confirm the output file opens correctly in Windows or an icon viewer.
- Run the CLI with `--sizes 16,32` and confirm the output appears in the destination folder.

## More Help

See `USERGUIDE.md` for a fuller step-by-step guide for installation, usage, building, and troubleshooting.
