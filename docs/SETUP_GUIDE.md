# OmniPilot Setup Guide

**Windows 11 · Local AI with Ollama · Without OpenClaw**

---

## What Gets Installed

| Component | Purpose |
|-----------|---------|
| **Ollama** | Local LLM runtime |
| **devstral:24b** | Hermes Agent — large project planning & architecture |
| **qwen3:8b** | OpenCode — coding with 233 specialist agents |
| **phi4** | Open Interpreter — desktop automation & file tasks |
| **OpenCode** | CLI coding agent with agent roles |
| **Open Interpreter** | General-purpose desktop AI assistant |
| **Hermes Agent** | Autonomous coding agent with memory |
| **AI 3D Generator Pro** | Image-to-3D / text-to-3D for 3D printing |
| **OmniPilot GUI** | PyQt6 desktop orchestrator (your app) |

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Windows 10 | Windows 11 23H2+ |
| RAM | 16 GB | 32 GB |
| Disk space | 30 GB free | 50 GB free |
| GPU | CPU-only (slow) | NVIDIA RTX 3060+ |
| Python | 3.10 | 3.11+ |

---

## Quick Start (Automatic)

### 1. Open PowerShell as Administrator

Right-click Start button → **Terminal (Admin)** or **PowerShell (Admin)**.

### 2. Allow script execution (one-time)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Confirm with `Y` (Yes).

### 3. Download and run the setup script

```powershell
# Download script
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/bestprogrammer212/omnipilot/main/setup_omnipilot.ps1" -OutFile "$env:TEMP\setup_omnipilot.ps1"

# Run it
& "$env:TEMP\setup_omnipilot.ps1"
```

The script installs everything automatically. **Estimated time: 30–60 minutes** depending on your internet speed.

---

## Manual Setup (Alternative)

If you prefer to install step-by-step, follow this section.

### 1. Install Ollama

```powershell
# Download installer
Invoke-WebRequest "https://ollama.com/download/OllamaSetup.exe" -OutFile "$env:TEMP\OllamaSetup.exe"

# Silent install
Start-Process "$env:TEMP\OllamaSetup.exe" -ArgumentList "/S" -Wait

# Add to PATH (if not already)
$ollamaPath = "$env:LOCALAPPDATA\Programs\Ollama"
if ($env:Path -notlike "*$ollamaPath*") {
    [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$ollamaPath", "User")
    $env:Path += ";$ollamaPath"
}

# Start Ollama
& "$ollamaPath\ollama.exe" serve
```

### 2. Pull AI Models

```powershell
# Hermes — large projects (~15 GB)
ollama pull devstral:24b

# OpenCode — coding agents (~5 GB)
ollama pull qwen3:8b

# Open Interpreter — desktop tasks (~9 GB)
ollama pull phi4
```

> **Note:** First download takes 10–20 minutes per model. Subsequent pulls are incremental.

### 3. Install Python Tools

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# OpenCode
pip install opencode

# Open Interpreter
pip install open-interpreter

# OmniPilot dependencies
pip install PyQt6>=6.4.0 requests>=2.28.0 psutil>=5.9.0 pywin32>=304 keyboard>=0.13.5 watchdog>=2.1.0 pillow>=9.0.0
```

### 4. Install Hermes Agent (Manual)

> **Hermes does not have an automatic Windows installer.**

1. Visit: https://hermes-agent.nousresearch.com/
2. Download the Windows version
3. Extract and add `hermes.exe` to your system PATH

Verify:
```powershell
hermes --version
```

### 5. Install AI 3D Generator Pro

Search **"AI 3D Generator Pro"** in the Microsoft Store, or use the direct link:

https://apps.microsoft.com/detail/9pbw96jqbb91

### 6. Clone and Run OmniPilot

```powershell
cd ~
git clone https://github.com/bestprogrammer212/omnipilot.git
cd omnipilot\src
python main.py
```

**Create a desktop shortcut** (optional):
```powershell
$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\OmniPilot.lnk")
$shortcut.TargetPath = "powershell.exe"
$shortcut.Arguments = "-WindowStyle Hidden -Command `"cd '$env:USERPROFILE\OmniPilot\src'; python main.py`""
$shortcut.WorkingDirectory = "$env:USERPROFILE\OmniPilot\src"
$shortcut.Save()
```

---

## Agent Roster (233 Agents, 16 Divisions)

The `tool_registry.py` contains agent definitions from the [Agency Agents](https://github.com/msitarzewski/agency-agents) catalog.

| Division | Agents | Examples |
|----------|--------|----------|
| **Engineering** | 34 | Frontend Developer, AI Engineer, Code Reviewer, Database Optimizer, Embedded Firmware Engineer |
| **Marketing** | 36 | SEO Specialist, TikTok Strategist, Content Creator, Reddit Community Builder, Douyin Strategist |
| **Specialized** | 52 | MCP Builder, Grant Writer, CFO, ESG Officer, Legal Document Review, Real Estate Agent |
| **Game Dev** | 20 | Unity Architect, Godot Scripter, Unreal Systems Engineer, Roblox Designer, Blender Addon Engineer |
| **GIS** | 13 | Drone/Reality Mapping, Web GIS Developer, Cartography Designer, BIM/GIS Specialist |
| **Sales** | 10 | Deal Strategist, Sales Engineer, Pipeline Analyst, Discovery Coach |
| **Security** | 10 | Penetration Tester, Threat Intelligence Analyst, Compliance Auditor, Blockchain Security |
| **Design** | 9 | UI Designer, Whimsy Injector, Brand Guardian, Image Prompt Engineer |
| **Testing** | 8 | Reality Checker, Accessibility Auditor, API Tester, Evidence Collector |
| **Project Management** | 7 | Studio Producer, Jira Workflow Steward, Meeting Notes Specialist |
| **Paid Media** | 7 | PPC Strategist, Ad Creative Strategist, Programmatic Buyer |
| **Support** | 6 | Analytics Reporter, Executive Summary Generator, Finance Tracker |
| **Spatial Computing** | 6 | visionOS Engineer, XR Immersive Developer, macOS Spatial/Metal Engineer |
| **Product** | 5 | Product Manager, Sprint Prioritizer, Behavioral Nudge Engine |
| **Finance** | 5 | Financial Analyst, Tax Strategist, Bookkeeper & Controller, FP&A Analyst |
| **Academic** | 5 | Historian, Anthropologist, Geographer, Narratologist, Psychologist |

---

## Hotkeys

| Hotkey | Action |
|--------|--------|
| `Ctrl + Shift + O` | Show OmniPilot window |
| `Esc` | Minimize to system tray |
| `Ctrl + Enter` | Submit prompt |

---

## Tool Mapping

OmniPilot routes prompts to the correct tool based on keyword classification:

| Prompt contains... | Routed to | Example |
|--------------------|-----------|---------|
| `game`, `unity`, `godot`, `html`, `react`, `api` | **OpenCode** | "Build a React PWA" |
| `plan project`, `architecture`, `system design` | **Hermes** | "Design microservices architecture" |
| `create file`, `open browser`, `desktop`, `read pdf` | **Open Interpreter** | "Create a folder and open Chrome" |
| `3d model`, `stl`, `mesh`, `generate 3d` | **AI 3D Generator Pro** | "Generate an STL from this image" |

---

## Troubleshooting

### Ollama not in PATH

```powershell
$env:Path += ";$env:LOCALAPPDATA\Programs\Ollama"
[Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
```

Restart your terminal after this.

### Re-download a model

```powershell
ollama list                    # Show installed models
ollama rm devstral:24b         # Remove a model
ollama pull devstral:24b       # Re-download it
```

### OmniPilot won't start

1. Check if Ollama is running: `ollama list`
2. Verify Python dependencies: `pip list | findstr PyQt6`
3. Run from the correct directory: `cd ~\OmniPilot\src; python main.py`
4. Check for Windows Defender blocking the app

### Out of memory when loading models

Run smaller quantizations:
```powershell
ollama pull devstral:24b-q4_K_M    # 4-bit quantized (~8 GB)
ollama pull qwen3:4b               # Smaller variant (~2.5 GB)
```

---

## Why OpenClaw Is Not Included

OpenClaw uses a **workspace-based architecture** where each agent requires a dedicated folder with `SOUL.md`, `AGENTS.md`, and `IDENTITY.md` files. This is fundamentally different from OmniPilot's "prompt → classify → launch tool" pattern.

| Aspect | OmniPilot Pattern | OpenClaw Pattern |
|--------|-------------------|------------------|
| Activation | Single prompt, immediate launch | Workspace setup, then restart gateway |
| Persistence | Tool process runs, then exits | Agent identities persist across sessions |
| Use case | Quick task delegation | Long-term multi-agent pipelines |

If you later need persistent multi-agent orchestration (e.g., Frontend Developer + UI Designer + Code Reviewer collaborating on one feature), OpenClaw can be added as a v2.0 integration.

---

## File Structure

```
OmniPilot/
├── src/
│   ├── main.py                 # Entry point
│   ├── gui/
│   │   ├── main_window.py      # PyQt6 main window
│   │   ├── input_widget.py     # Prompt input field
│   │   ├── context_panel.py    # Desktop context display
│   │   ├── suggestion_card.py  # Tool suggestion UI
│   │   ├── history_view.py     # Action history
│   │   └── style.py            # Dark theme stylesheet
│   ├── core/
│   │   ├── context_scanner.py  # Desktop/project scanning
│   │   ├── llm_classifier.py   # Ollama-based prompt classification
│   │   ├── tool_launcher.py    # Tool process management
│   │   ├── three_d_handler.py  # AI 3D Generator Pro integration
│   │   └── history_manager.py  # Learning & preferences
│   └── agents/
│       └── tool_registry.py    # 233 agent definitions (this file!)
├── requirements.txt
├── build.py                    # PyInstaller build script
├── setup_omnipilot.ps1         # Windows setup script
└── README.md
```

---

## Building the .exe

```powershell
pip install pyinstaller
python build.py
# Output: dist/OmniPilot.exe
```

---

## License

MIT License — based on [Agency Agents](https://github.com/msitarzewski/agency-agents) by Michael Sitarzewski.

---

*Generated for OmniPilot v1.0 · Windows Setup · Without OpenClaw*
