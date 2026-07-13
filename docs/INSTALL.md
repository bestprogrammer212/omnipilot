# Installation Guide

## Step 1: Install Base Tools

### Windows Terminal
```powershell
winget install Microsoft.WindowsTerminal
```

### Git
```powershell
winget install Git.Git
```

### Python 3.12
```powershell
winget install Python.Python.3.12
# Check "Add Python to PATH" during installation
```

### VS Code (optional)
```powershell
winget install Microsoft.VisualStudioCode
```

## Step 2: Install Ollama

```powershell
winget install Ollama.Ollama
```

Download models:
```powershell
ollama pull devstral:24b
ollama pull qwen3:8b
ollama pull phi4
```

Set context length (important for agents):
```powershell
# System environment variable
[Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "64000", "Machine")
```

## Step 3: Install AI Tools

### Hermes Agent
1. Visit https://hermes-agent.nousresearch.com/
2. Download Windows app
3. Configure: Provider=Ollama, URL=http://localhost:11434/v1, Model=devstral:24b

### OpenCode
```powershell
pip install opencode
```

### Open Interpreter Desktop
```powershell
irm https://www.openinterpreter.com/install.ps1 | iex
```

### AI 3D Generator Pro
1. Open Microsoft Store
2. Search: "AI Text & Image to 3D Generator Pro"
3. Install

### Agency Agents (optional)
1. Download from https://github.com/msitarzewski/agency-agents-app/releases
2. Install `Agency-Agents-Setup-0.2.1-x64.exe`
3. Browse catalog and install agents for OpenCode

## Step 4: Install OmniPilot

```powershell
# Clone repository
git clone https://github.com/yourusername/omnipilot.git
cd omnipilot

# Install dependencies
pip install -r requirements.txt

# Run
python src/main.py
```

## Step 5: Build .exe (Optional)

```powershell
pip install pyinstaller
python build.py
```

The executable will be in `dist/OmniPilot.exe`.

## Troubleshooting

### Ollama not found
- Ensure Ollama is running: `ollama serve`
- Check URL in Hermes Agent: `http://localhost:11434/v1` (with /v1!)

### Tools not found
- Add tool directories to PATH
- Or specify full paths in OmniPilot settings

### Memory issues
- Close other applications before running large models
- Use smaller models: phi4 instead of devstral:24b
- Run tools sequentially, not in parallel

### Build fails
- Install Visual C++ Build Tools
- Use `--onedir` instead of `--onefile` if single file fails
