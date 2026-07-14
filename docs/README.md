# OmniPilot 🤖

AI Tool Orchestrator for HP OmniBook X Flip and other Windows PCs.

## What is OmniPilot?

OmniPilot is a desktop application that intelligently routes your prompts to the best local AI tool:

- **Hermes Agent** → Large project planning, architecture, complex refactoring
- **OpenCode** → Coding with specialist agents (game dev, web dev, embedded, 3D printing, etc.)
- **Open Interpreter** → File creation, browser automation, desktop control
- **AI 3D Generator Pro** → Image-to-3D and text-to-3D model generation for 3D printing

## Features

- 🧠 **Context Awareness**: Scans your desktop, active windows, and project folders
- 🤖 **Intelligent Routing**: Uses local LLM (Ollama) to classify prompts and select the best tool
- 🎯 **Agent Selection**: Automatically picks the right specialist agent from 232+ options
- 📊 **Learning**: Remembers your preferences and improves over time
- 🎨 **Beautiful UI**: Dark theme, system tray, hotkeys
- ⚡ **Fast**: Background scanning, async classification

## Installation

### Prerequisites

1. **Windows 11** with 32 GB RAM (recommended)
2. **Ollama** installed with models:
   - `devstral:24b` (for Hermes)
   - `qwen3:8b` (for OpenCode)
   - `phi4` (for Open Interpreter)
3. **Tools installed**:
   - Hermes Agent (from https://hermes-agent.nousresearch.com/)
   - OpenCode (`pip install opencode`)
   - Open Interpreter Desktop (`irm https://www.openinterpreter.com/install.ps1 | iex`)
   - AI 3D Generator Pro (from Microsoft Store)
   - Agency Agents https://github.com/msitarzewski/agency-agents-app

### Quick Start

```powershell
# 1. Clone repository
git clone https://github.com/yourusername/omnipilot.git
cd omnipilot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python src/main.py

# 4. Build .exe (optional)
python build.py
```

### Build .exe

```powershell
pip install pyinstaller
python build.py
# Output: dist/OmniPilot.exe
```

## Usage

1. **Press Ctrl+Shift+O** to show OmniPilot
2. **Type your prompt** (e.g., "Create a micro:bit game with collision detection")
3. **Click Analyze** or **Ctrl+Enter** to classify
4. **Review suggestion** (tool, agent, model, confidence)
5. **Click Launch** to start the tool automatically

## Architecture

```
OmniPilot/
├── src/
│   ├── main.py              # Entry point
│   ├── gui/                 # PyQt6 UI components
│   │   ├── main_window.py   # Main window
│   │   ├── input_widget.py  # Prompt input
│   │   ├── context_panel.py # Desktop context display
│   │   ├── suggestion_card.py # Tool suggestion
│   │   ├── history_view.py  # Action history
│   │   └── style.py         # Dark theme
│   ├── core/                # Core logic
│   │   ├── context_scanner.py  # Desktop/project scanning
│   │   ├── llm_classifier.py # Ollama-based classification
│   │   ├── tool_launcher.py  # Tool process management
│   │   ├── three_d_handler.py # AI 3D Generator Pro integration
│   │   └── history_manager.py # Learning & preferences
│   └── agents/
│       └── tool_registry.py  # Agent definitions
├── requirements.txt
├── build.py
└── README.md
```

## Hotkeys

| Hotkey | Action |
|--------|--------|
| `Ctrl+Shift+O` | Show OmniPilot |
| `Esc` | Minimize to tray |
| `Ctrl+Enter` | Submit prompt |

## License

MIT License - see LICENSE file
