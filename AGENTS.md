# Repository Guidelines for AI Agents & Developers

## Project Overview

This repository is a Python desktop utility for converting images into `.ico` files. It is not a Next.js or React project. Keep changes focused on the existing Python GUI, shared conversion module, and legacy CLI workflow.

## Project Structure & Module Organization

- `app_ui.py`: Main CustomTkinter GUI application. This is the recommended user-facing entry point.
- `converter.py`: Shared image conversion logic used by both the GUI and CLI. Put conversion behavior here so both entry points stay consistent.
- `image_converter.py`: Legacy command-line batch converter.
- `requirements.txt`: Python dependencies.
- `install.bat`: Installs dependencies.
- `run_gui.bat`: Starts the GUI app.
- `run_cli.bat`: Runs the CLI converter with default folders.
- `build.bat`: Builds `dist\IconConverter.exe` with PyInstaller.
- `Raw File/`: Default CLI source folder.
- `Icon File/`: Default CLI output folder.
- `USERGUIDE.md`: End-user setup, usage, build, and troubleshooting documentation.

## Development Principles

- Inspect the existing files before making changes.
- Prefer small, safe edits over broad rewrites.
- Keep conversion behavior centralized in `converter.py`.
- Keep GUI-only behavior in `app_ui.py`.
- Keep CLI parsing and command-line options in `image_converter.py`.
- Use Windows PowerShell-compatible commands in documentation.
- Avoid unrelated refactors when implementing a focused feature.
- Preserve existing user workflows unless a change is explicitly requested.

## Build, Test, and Development Commands

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the GUI:

```powershell
python app_ui.py
```

Run the CLI with default folders:

```powershell
python image_converter.py
```

Run the CLI with custom folders:

```powershell
python image_converter.py --source "path\to\images" --dest "path\to\icons"
```

Run the CLI with selected icon sizes:

```powershell
python image_converter.py --sizes 16,32,256
```

Build the standalone executable:

```powershell
pip install pyinstaller
.\build.bat
```

The generated executable is expected at:

```text
dist\IconConverter.exe
```

## Testing Guidelines

No automated test suite is currently implemented. After code changes, manually verify the affected workflows:

- GUI opens successfully with `python app_ui.py`.
- Browse and drag-and-drop image selection still work.
- Conversion works with all default icon sizes selected.
- Conversion works with only a subset of sizes selected.
- GUI blocks conversion when no icon size is selected.
- CLI still works with default folders.
- CLI `--sizes` accepts comma-separated positive integers.
- Built executable starts and converts an image after running `.\build.bat`.

## Documentation Expectations

When changing user-facing behavior, update both:

- `README.md` for project overview and quickstart.
- `USERGUIDE.md` for step-by-step user instructions.
