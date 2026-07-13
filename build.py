#!/usr/bin/env python3
"""Build script for OmniPilot .exe"""
import PyInstaller.__main__
import os
import shutil

# Clean previous builds
for folder in ['build', 'dist']:
    if os.path.exists(folder):
        shutil.rmtree(folder)

PyInstaller.__main__.run([
    'src/main.py',
    '--name=OmniPilot',
    '--onefile',
    '--windowed',
    '--icon=src/assets/icon.ico',
    '--add-data=src/assets;assets',
    '--hidden-import=PyQt6',
    '--hidden-import=requests',
    '--hidden-import=psutil',
    '--hidden-import=win32gui',
    '--hidden-import=win32process',
    '--hidden-import=win32con',
    '--hidden-import=keyboard',
    '--hidden-import=watchdog',
    '--hidden-import=watchdog.observers',
    '--hidden-import=watchdog.events',
    '--clean',
    '--noconfirm',
])

print("Build complete! .exe is in dist/OmniPilot.exe")
