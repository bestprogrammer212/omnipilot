#!/usr/bin/env python3
"""OmniPilot - AI Tool Orchestrator for HP OmniBook X Flip

A desktop application that intelligently routes user prompts to the best
local AI tool (OpenCode, Hermes Agent, Open Interpreter, AI 3D Generator Pro)
based on context analysis and LLM classification.

Usage:
    python src/main.py              # Run from source
    OmniPilot.exe                   # Run built executable

Hotkeys:
    Ctrl+Shift+O    Show window
    Esc             Minimize to tray
    Ctrl+Enter      Submit prompt
"""
import sys
import os
import time

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase

from gui.main_window import MainWindow

def setup_application() -> QApplication:
    """Initialize Qt application with proper settings"""
    # Enable high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName("OmniPilot")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("OmniPilot")

    # Set default font
    font = QFont("Segoe UI", 10)
    if not QFontDatabase.hasFamily("Segoe UI"):
        font = QFont("SF Pro Display", 10)
    if not QFontDatabase.hasFamily("SF Pro Display"):
        font = QFont("Arial", 10)
    app.setFont(font)

    # Set application-wide stylesheet base
    app.setStyle("Fusion")

    return app

def main():
    """Main entry point"""
    print("Starting OmniPilot...")
    print("   AI Tool Orchestrator for HP OmniBook X Flip")
    print("   Press Ctrl+Shift+O to show window")
    print()

    app = setup_application()

    # Create and show main window
    window = MainWindow()

    # Start minimized to tray
    window.hide()

    print("OmniPilot running in system tray")
    print("   Right-click tray icon for options")

    # Run application
    exit_code = app.exec()

    print("OmniPilot shutting down...")
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
