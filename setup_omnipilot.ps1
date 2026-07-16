<#
.SYNOPSIS
    OmniPilot Windows Setup Script
    Installs Ollama, AI models, Python tools, and configures OmniPilot
    WITHOUT OpenClaw

.DESCRIPTION
    Run this in an elevated PowerShell (Admin) on your new Windows laptop.
    It installs: Ollama, devstral:24b, qwen3:8b, phi4, OpenCode, Open Interpreter,
    Hermes (download link), and clones OmniPilot from GitHub.

.EXAMPLE
    .\setup_omnipilot.ps1
#>

param(
    [switch]$SkipOllama,
    [switch]$SkipModels,
    [switch]$SkipPython,
    [switch]$SkipTools,
    [switch]$SkipOmniPilot
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "Continue"

function Write-Header($text) {
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "  $text" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
}

function Write-Step($text) {
    Write-Host "[+] $text" -ForegroundColor Green
}

function Write-Warn($text) {
    Write-Host "[!] $text" -ForegroundColor Yellow
}

function Write-Error($text) {
    Write-Host "[X] $text" -ForegroundColor Red
}

# ============================================================
# CHECK ADMIN
# ============================================================
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Please run this script as Administrator!"
    Write-Host "Right-click PowerShell -> 'Run as Administrator'" -ForegroundColor Yellow
    exit 1
}

Write-Header "OmniPilot Windows Setup"
Write-Host "This will install your complete local AI stack."
Write-Host "Estimated time: 30-60 minutes (depending on download speed)"
Write-Host "Required: ~40 GB disk space, 32 GB RAM recommended`n"

$confirm = Read-Host "Continue? (y/n)"
if ($confirm -ne 'y') { exit 0 }

# ============================================================
# 1. INSTALL OLLAMA
# ============================================================
if (-not $SkipOllama) {
    Write-Header "1. Installing Ollama"

    if (Get-Command ollama -ErrorAction SilentlyContinue) {
        Write-Warn "Ollama already installed: $(ollama --version)"
    } else {
        Write-Step "Downloading Ollama installer..."
        $ollamaUrl = "https://ollama.com/download/OllamaSetup.exe"
        $ollamaInstaller = "$env:TEMP\OllamaSetup.exe"

        try {
            Invoke-WebRequest -Uri $ollamaUrl -OutFile $ollamaInstaller -UseBasicParsing
            Write-Step "Installing Ollama..."
            Start-Process -FilePath $ollamaInstaller -ArgumentList "/S" -Wait
            Write-Step "Ollama installed successfully!"
        } catch {
            Write-Error "Failed to download/install Ollama. Please install manually from https://ollama.com"
            exit 1
        }
    }

    # Add Ollama to PATH if not present
    $ollamaPath = "$env:LOCALAPPDATA\Programs\Ollama"
    if ($env:Path -notlike "*$ollamaPath*") {
        [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$ollamaPath", "User")
        $env:Path += ";$ollamaPath"
        Write-Step "Added Ollama to PATH"
    }

    # Start Ollama service
    Write-Step "Starting Ollama service..."
    Start-Process -FilePath "$ollamaPath\ollama.exe" -WindowStyle Hidden
    Start-Sleep -Seconds 5
}

# ============================================================
# 2. PULL MODELS
# ============================================================
if (-not $SkipModels) {
    Write-Header "2. Downloading AI Models (this takes a while!)"

    $models = @(
        @{ Name = "devstral:24b"; Size = "~15 GB"; Desc = "Hermes Agent (large projects)" },
        @{ Name = "qwen3:8b"; Size = "~5 GB"; Desc = "OpenCode (coding agents)" },
        @{ Name = "phi4"; Size = "~9 GB"; Desc = "Open Interpreter (desktop tasks)" }
    )

    foreach ($model in $models) {
        Write-Step "Pulling $($model.Name) ($($model.Desc), $($model.Size))..."
        Write-Host "    This may take 10-20 minutes. Press Ctrl+C once to cancel." -ForegroundColor DarkGray
        try {
            ollama pull $model.Name
            Write-Step "$($model.Name) ready!"
        } catch {
            Write-Error "Failed to pull $($model.Name). Run manually: ollama pull $($model.Name)"
        }
    }
}

# ============================================================
# 3. PYTHON & PIP
# ============================================================
if (-not $SkipPython) {
    Write-Header "3. Checking Python"

    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Warn "Python not found. Please install Python 3.11+ from https://python.org"
        Write-Warn "IMPORTANT: Check 'Add Python to PATH' during installation!"
        Start-Process "https://www.python.org/downloads/"
        Read-Host "Press Enter after installing Python..."
    }

    $pyVersion = python --version 2>$null
    Write-Step "Python found: $pyVersion"

    Write-Step "Upgrading pip..."
    python -m pip install --upgrade pip
}

# ============================================================
# 4. INSTALL TOOLS
# ============================================================
if (-not $SkipTools) {
    Write-Header "4. Installing AI Tools"

    # OpenCode
    Write-Step "Installing OpenCode..."
    pip install opencode

    # Open Interpreter
    Write-Step "Installing Open Interpreter..."
    pip install open-interpreter

    # OmniPilot dependencies
    Write-Step "Installing OmniPilot Python dependencies..."
    $deps = @("PyQt6>=6.4.0", "requests>=2.28.0", "psutil>=5.9.0", "pywin32>=304", "keyboard>=0.13.5", "watchdog>=2.1.0", "pillow>=9.0.0")
    foreach ($dep in $deps) {
        pip install $dep
    }

    # Hermes (manual download hint)
    Write-Header "Hermes Agent Setup"
    Write-Warn "Hermes Agent must be installed manually:"
    Write-Host "    1. Visit: https://hermes-agent.nousresearch.com/" -ForegroundColor White
    Write-Host "    2. Download and install the Windows version" -ForegroundColor White
    Write-Host "    3. Ensure 'hermes' is available in your PATH" -ForegroundColor White
    Write-Host ""

    # AI 3D Generator Pro (MS Store)
    Write-Header "AI 3D Generator Pro"
    Write-Warn "Install from Microsoft Store:"
    Write-Host "    https://apps.microsoft.com/detail/9pbw96jqbb91" -ForegroundColor White
    Write-Host "    Or search 'AI 3D Generator Pro' in the Microsoft Store app" -ForegroundColor White
    Write-Host ""

    # Agency Agents App
    Write-Header "Agency Agents App (optional)"
    Write-Warn "For browsing all 232 agents with a GUI:"
    Write-Host "    brew install --cask msitarzewski/agency-agents/agency-agents" -ForegroundColor White
    Write-Host "    (Requires Homebrew for Windows, or use the direct download)" -ForegroundColor White
    Write-Host "    https://agencyagents.app/" -ForegroundColor White
    Write-Host ""
}

# ============================================================
# 5. CLONE OMNIPILOT
# ============================================================
if (-not $SkipOmniPilot) {
    Write-Header "5. Setting up OmniPilot"

    $omniPath = "$env:USERPROFILE\OmniPilot"
    if (Test-Path $omniPath) {
        Write-Warn "OmniPilot folder already exists at $omniPath"
        $pull = Read-Host "Pull latest changes? (y/n)"
        if ($pull -eq 'y') {
            Set-Location $omniPath
            git pull
        }
    } else {
        Write-Step "Cloning OmniPilot from GitHub..."
        Set-Location $env:USERPROFILE
        git clone https://github.com/bestprogrammer212/omnipilot.git
        Write-Step "OmniPilot cloned to $omniPath"
    }

    # Create desktop shortcut
    Write-Step "Creating desktop shortcut..."
    $WshShell = New-Object -ComObject WScript.Shell
    $shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\OmniPilot.lnk")
    $shortcut.TargetPath = "powershell.exe"
    $shortcut.Arguments = "-WindowStyle Hidden -Command `"cd '$omniPath\src'; python main.py`""
    $shortcut.WorkingDirectory = "$omniPath\src"
    $shortcut.IconLocation = "powershell.exe,0"
    $shortcut.Save()
    Write-Step "Desktop shortcut created!"
}

# ============================================================
# DONE
# ============================================================
Write-Header "Setup Complete!"
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Install Hermes Agent manually (see link above)" -ForegroundColor White
Write-Host "  2. Install AI 3D Generator Pro from Microsoft Store" -ForegroundColor White
Write-Host "  3. Restart PowerShell/Terminal to refresh PATH" -ForegroundColor White
Write-Host "  4. Run OmniPilot: cd ~\OmniPilot\src; python main.py" -ForegroundColor White
Write-Host "  5. Or double-click the 'OmniPilot' shortcut on your desktop" -ForegroundColor White
Write-Host ""
Write-Host "Hotkeys when running:" -ForegroundColor Cyan
Write-Host "  Ctrl+Shift+O    Show OmniPilot" -ForegroundColor White
Write-Host "  Esc             Minimize to tray" -ForegroundColor White
Write-Host "  Ctrl+Enter      Submit prompt" -ForegroundColor White
Write-Host ""
Write-Host "Models installed:" -ForegroundColor Cyan
Write-Host "  ollama list" -ForegroundColor DarkGray
Write-Host ""
Read-Host "Press Enter to exit"
