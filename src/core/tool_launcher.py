"""Tool launcher for OmniPilot - starts AI tools with correct models and agents"""
import subprocess
import time
import os
import sys
from typing import Optional, Dict, List
from dataclasses import dataclass
import psutil

@dataclass
class LaunchConfig:
    tool: str
    model: Optional[str] = None
    agent: Optional[str] = None
    prompt: Optional[str] = None
    working_dir: Optional[str] = None

class ToolLauncher:
    """Manages launching and monitoring AI tools"""

    # Tool configurations
    TOOL_CONFIGS = {
        "opencode": {
            "exe": "opencode",
            "args": ["--provider", "ollama", "--api-base", "http://localhost:11434"],
            "needs_ollama": True,
            "default_model": "qwen3:8b",
            "env": {}
        },
        "hermes": {
            "exe": "hermes",
            "args": [],
            "needs_ollama": True,
            "default_model": "devstral:24b",
            "env": {}
        },
        "interpreter": {
            "exe": "interpreter",
            "args": ["--api_base", "http://localhost:11434"],
            "needs_ollama": True,
            "default_model": "phi4",
            "env": {}
        },
        "ai3d": {
            "exe": "AI 3D Generator Pro",
            "args": [],
            "needs_ollama": False,
            "default_model": None,
            "env": {}
        }
    }

    def __init__(self, ollama_url: str = "http://localhost:11434"):
        self.ollama_url = ollama_url
        self.active_processes: Dict[str, subprocess.Popen] = {}
        self.ollama_process: Optional[subprocess.Popen] = None

    def is_ollama_running(self) -> bool:
        """Check if Ollama server is running"""
        try:
            import requests
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False

    def start_ollama(self) -> bool:
        """Start Ollama server if not running"""
        if self.is_ollama_running():
            return True

        try:
            # Try to start ollama serve
            self.ollama_process = subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Wait for it to be ready
            for _ in range(30):  # 30 seconds max
                time.sleep(1)
                if self.is_ollama_running():
                    return True

            return False
        except Exception as e:
            print(f"Failed to start Ollama: {e}")
            return False

    def load_model(self, model: str) -> bool:
        """Pre-load a model into Ollama"""
        try:
            import requests
            # Pull model if not exists
            response = requests.post(
                f"{self.ollama_url}/api/pull",
                json={"name": model, "stream": False},
                timeout=300
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Failed to load model {model}: {e}")
            return False

    def kill_existing_tool(self, tool_name: str):
        """Kill any existing instances of a tool to free RAM"""
        # Find processes by name
        tool_exe = self.TOOL_CONFIGS.get(tool_name, {}).get("exe", tool_name)

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] and tool_exe.lower() in proc.info['name'].lower():
                    proc.kill()
                    proc.wait(timeout=5)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass

        # Also check our tracked processes
        if tool_name in self.active_processes:
            try:
                self.active_processes[tool_name].terminate()
                self.active_processes[tool_name].wait(timeout=5)
            except:
                pass
            del self.active_processes[tool_name]

    def launch(self, config: LaunchConfig) -> bool:
        """Launch a tool with the given configuration"""

        tool_name = config.tool
        if tool_name not in self.TOOL_CONFIGS:
            print(f"Unknown tool: {tool_name}")
            return False

        tool_config = self.TOOL_CONFIGS[tool_name]

        # Step 1: Ensure Ollama is running if needed
        if tool_config["needs_ollama"]:
            if not self.start_ollama():
                print("Failed to start Ollama server")
                return False

        # Step 2: Kill existing tool instances to free RAM
        self.kill_existing_tool(tool_name)

        # Step 3: Kill other AI tools to free RAM (sequential usage)
        for other_tool in self.active_processes:
            if other_tool != tool_name:
                self.kill_existing_tool(other_tool)

        # Step 4: Load model if needed
        model = config.model or tool_config["default_model"]
        if model and tool_config["needs_ollama"]:
            print(f"Loading model: {model}...")
            if not self.load_model(model):
                print(f"Warning: Could not pre-load model {model}")

        # Step 5: Build command
        cmd = [tool_config["exe"]]

        # Add model argument if applicable
        if model and tool_config["needs_ollama"]:
            if tool_name == "opencode":
                cmd.extend(["--model", f"ollama/{model}"])
            elif tool_name == "interpreter":
                cmd.extend(["--model", f"ollama/{model}"])
            # Hermes uses its own config

        # Add default args
        cmd.extend(tool_config["args"])

        # Step 6: Set environment
        env = os.environ.copy()
        env.update(tool_config["env"])
        if config.working_dir:
            env["PWD"] = config.working_dir

        # Step 7: Launch
        try:
            print(f"Launching {tool_name}...")

            # For GUI apps (AI 3D Generator Pro), use shell=True
            if tool_name == "ai3d":
                process = subprocess.Popen(
                    f'start "" "{tool_config["exe"]}"',
                    shell=True,
                    env=env,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            else:
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    env=env,
                    cwd=config.working_dir,
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )

            self.active_processes[tool_name] = process

            # Wait a moment for tool to start
            time.sleep(2)

            # If we have an agent for opencode, we need to send it after startup
            if tool_name == "opencode" and config.agent:
                # This is tricky - we'd need to interact with the running process
                # For now, show instruction to user
                print(f"\n👉 In OpenCode, type: /agent {config.agent}")

            # If we have a prompt, also show it
            if config.prompt:
                print(f"👉 Then type your prompt: {config.prompt}")

            return True

        except Exception as e:
            print(f"Failed to launch {tool_name}: {e}")
            return False

    def get_status(self) -> Dict:
        """Get status of all managed processes"""
        status = {
            "ollama_running": self.is_ollama_running(),
            "active_tools": {},
            "memory": {
                "total": psutil.virtual_memory().total // (1024**3),  # GB
                "available": psutil.virtual_memory().available // (1024**3),  # GB
                "percent": psutil.virtual_memory().percent
            }
        }

        for tool_name, process in self.active_processes.items():
            status["active_tools"][tool_name] = {
                "pid": process.pid,
                "running": process.poll() is None
            }

        return status

    def shutdown_all(self):
        """Shutdown all managed processes"""
        for tool_name in list(self.active_processes.keys()):
            self.kill_existing_tool(tool_name)

        if self.ollama_process:
            try:
                self.ollama_process.terminate()
                self.ollama_process.wait(timeout=5)
            except:
                pass
