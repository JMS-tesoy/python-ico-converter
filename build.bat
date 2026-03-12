@echo off
title Building IconConverter.exe

echo Cleaning up previous build artifacts...

if exist "dist" (
    echo   - Deleting 'dist' folder
    rmdir /s /q "dist"
)

if exist "build" (
    echo   - Deleting 'build' folder
    rmdir /s /q "build"
)

if exist "IconConverter.spec" (
    echo   - Deleting 'IconConverter.spec' file
    del "IconConverter.spec"
)

echo.
echo Starting the PyInstaller build process...
pyinstaller --noconfirm --clean --onefile --windowed --name IconConverter app_ui.py

echo.
echo Build process finished. The executable is in the 'dist' folder.
pause