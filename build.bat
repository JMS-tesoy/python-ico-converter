@echo off
title Building IconConverter.exe

echo Closing any running IconConverter.exe process...
taskkill /IM IconConverter.exe /F >nul 2>&1
if %errorlevel% equ 0 (
    echo   - Closed running IconConverter.exe
) else (
    echo   - No running IconConverter.exe found
)

echo Cleaning up previous build artifacts...

if exist "dist" (
    echo   - Deleting 'dist' folder
    rmdir /s /q "dist"
    if exist "dist" (
        echo.
        echo ERROR: Could not delete the 'dist' folder.
        echo Close IconConverter.exe, close any File Explorer window previewing it, then run build.bat again.
        pause
        exit /b 1
    )
)

if exist "build" (
    echo   - Deleting 'build' folder
    rmdir /s /q "build"
    if exist "build" (
        echo.
        echo ERROR: Could not delete the 'build' folder.
        echo Close any program that may be using the project files, then run build.bat again.
        pause
        exit /b 1
    )
)

if exist "IconConverter.spec" (
    echo   - Deleting 'IconConverter.spec' file
    del "IconConverter.spec"
    if exist "IconConverter.spec" (
        echo.
        echo ERROR: Could not delete IconConverter.spec.
        pause
        exit /b 1
    )
)

echo.
echo Starting the PyInstaller build process...
pyinstaller --noconfirm --clean --onefile --windowed --name IconConverter --collect-all tkinterdnd2 app_ui.py
if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller build failed.
    echo Read the error above, fix it, then run build.bat again.
    pause
    exit /b 1
)

echo.
echo Build process finished. The executable is in the 'dist' folder.
pause
