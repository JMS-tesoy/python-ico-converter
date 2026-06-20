# Icon Converter User Guide

This guide explains how to install, run, use, and build the Python ICO Converter project.

## What This App Does

Icon Converter turns common image files into Windows `.ico` files. It supports:

- `.png`
- `.jpg`
- `.jpeg`

You can use the graphical app for single-file conversion or the command-line tool for batch conversion.

## Requirements

Before using the project, install:

- Python 3.10 or newer
- pip
- Windows PowerShell or Command Prompt

To check your Python version:

```powershell
python --version
```

## Install Dependencies

From the project folder, run:

```powershell
pip install -r requirements.txt
```

You can also double-click or run:

```powershell
.\install.bat
```

This installs the required packages:

- `customtkinter`
- `tkinterdnd2`
- `Pillow`

## Using the GUI App

Start the graphical app:

```powershell
python app_ui.py
```

Or run:

```powershell
.\run_gui.bat
```

### Convert an Image

1. Click **Browse** and select a `.png`, `.jpg`, or `.jpeg` image.
2. Choose the icon sizes you want to include.
3. Click **Convert to ICO**.
4. Wait for the log to say the icon is ready.
5. Click **Save to...** and choose where to save the `.ico` file.

### Drag and Drop

You can also drag an image file directly into the app window. After dropping the file, choose your icon sizes and convert it normally.

## Icon Size Selection

The GUI supports these icon sizes:

- `16x16`
- `32x32`
- `48x48`
- `64x64`
- `128x128`
- `256x256`

All sizes are selected by default. Uncheck any sizes you do not need.

At least one icon size must be selected before converting.

## How Non-Square Images Are Handled

If the source image is not square, the app fits it onto a transparent square canvas. This keeps the image from being stretched and makes sure the final `.ico` contains true square icon frames.

For example, a wide logo converted at `32x32` will stay proportional and be centered inside a transparent `32x32` icon.

## Using the Command-Line Converter

The CLI is useful for converting every supported image in a folder.

### Default Folders

By default, the CLI reads from:

```text
Raw File\
```

And writes to:

```text
Icon File\
```

Run:

```powershell
python image_converter.py
```

Or:

```powershell
.\run_cli.bat
```

### Custom Source and Output Folders

```powershell
python image_converter.py --source "path\to\your\images" --dest "path\for\your\icons"
```

### Choose Icon Sizes from the CLI

Use `--sizes` with comma-separated pixel sizes:

```powershell
python image_converter.py --sizes 16,32,256
```

With custom folders:

```powershell
python image_converter.py --source "Raw File" --dest "Icon File" --sizes 16,32,48
```

The CLI accepts positive integer sizes. Avoid spaces inside the comma-separated list.

## Build the Windows Executable

The project includes a build script that creates a standalone `.exe` file.

### 1. Install Project Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Install PyInstaller

```powershell
pip install pyinstaller
```

### 3. Run the Build Script

```powershell
.\build.bat
```

The build script will:

1. Delete old `dist` and `build` folders if they exist.
2. Delete the old `IconConverter.spec` file if it exists.
3. Run PyInstaller with the correct options.
4. Create the executable.

When the build finishes, the executable should be here:

```text
dist\IconConverter.exe
```

## Regenerate a New EXE File

Use this process whenever you change the Python code and want a fresh `IconConverter.exe`.

### 1. Close the Old App

If `dist\IconConverter.exe` is currently open, close it first. Windows may block the build if the old executable is still running.

### 2. Confirm Dependencies Are Installed

```powershell
pip install -r requirements.txt
pip install pyinstaller
```

### 3. Run the Build Script

From the project folder, run:

```powershell
.\build.bat
```

The script removes the previous build output and creates a new executable at:

```text
dist\IconConverter.exe
```

### 4. Test the New EXE

Run:

```powershell
.\dist\IconConverter.exe
```

Then convert a sample image to confirm the new build works.

### Build Command Used Internally

The `build.bat` file runs this PyInstaller command:

```powershell
pyinstaller --noconfirm --clean --onefile --windowed --name IconConverter --collect-all tkinterdnd2 app_ui.py
```

## Recommended Manual Testing

After installing or building, test these workflows:

1. Start the GUI.
2. Select an image with **Browse**.
3. Convert with all icon sizes selected.
4. Convert again with only `16x16` and `32x32` selected.
5. Try converting with no sizes selected and confirm the app shows a warning.
6. Drag and drop an image into the app.
7. Save the generated `.ico` file.
8. Run the CLI with default folders.
9. Run the CLI with custom sizes:

```powershell
python image_converter.py --sizes 16,32
```

10. Build the executable and confirm `dist\IconConverter.exe` opens.

## Troubleshooting

### `python` Is Not Recognized

Python may not be installed or may not be added to PATH. Reinstall Python and enable **Add python.exe to PATH** during installation.

### Missing Package Error

If you see an error for `customtkinter`, `tkinterdnd2`, or `PIL`, reinstall dependencies:

```powershell
pip install -r requirements.txt
```

### PyInstaller Is Not Recognized

Install PyInstaller:

```powershell
pip install pyinstaller
```

Then run:

```powershell
.\build.bat
```

### Drag and Drop Does Not Work in the Built App

Make sure the build command includes:

```powershell
--collect-all tkinterdnd2
```

The provided `build.bat` already includes this option.

### Output File Already Exists in CLI Mode

The CLI skips files when the destination `.ico` already exists. Delete the existing file from `Icon File\` or choose a different destination folder.

## File Reference

- GUI app: `app_ui.py`
- Shared conversion logic: `converter.py`
- CLI converter: `image_converter.py`
- Dependency list: `requirements.txt`
- Build script: `build.bat`
- Output executable: `dist\IconConverter.exe`
