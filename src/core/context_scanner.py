"""Desktop and project context scanner for OmniPilot"""
import os
import psutil
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import win32gui
import win32process
import win32con

@dataclass
class WindowInfo:
    title: str
    process_name: str
    process_id: int
    window_handle: int
    is_minimized: bool

@dataclass
class ProjectContext:
    path: str
    name: str
    project_type: str
    files: List[str]
    recent_files: List[str]
    git_branch: Optional[str] = None
    has_readme: bool = False
    has_package_json: bool = False
    has_requirements: bool = False
    has_cargo_toml: bool = False

class ContextScanner:
    """Scans desktop environment for active projects and windows"""

    PROJECT_TYPES = {
        "python": [".py", "requirements.txt", "setup.py", "pyproject.toml"],
        "web": [".html", ".css", ".js", ".ts", ".jsx", ".tsx", "package.json", "vite.config"],
        "microbit": [".hex", "main.py", "microbit"],
        "arduino": [".ino", ".cpp", "platformio.ini"],
        "esp32": [".ino", "sdkconfig", "CMakeLists.txt"],
        "game": [".godot", "project.godot", "Assets", "Scenes"],
        "unity": ["Assets", "ProjectSettings", ".unity"],
        "3d": [".blend", ".stl", ".obj", ".glb", ".gltf", "cura", "prusaslicer"],
        "rust": ["Cargo.toml", ".rs"],
        "go": ["go.mod", ".go"],
        "java": ["pom.xml", "build.gradle", ".java"],
    }

    def __init__(self):
        self.last_scan = None
        self.scan_interval = 2.0  # seconds
        self._cache = {}

    def get_active_window(self) -> Optional[WindowInfo]:
        """Get information about the currently focused window"""
        try:
            hwnd = win32gui.GetForegroundWindow()
            if not hwnd:
                return None

            # Get window title
            title = win32gui.GetWindowText(hwnd)

            # Get process info
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            process_name = process.name()

            # Check if minimized
            is_minimized = win32gui.IsIconic(hwnd)

            return WindowInfo(
                title=title,
                process_name=process_name,
                process_id=pid,
                window_handle=hwnd,
                is_minimized=is_minimized
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied, Exception):
            return None

    def get_project_from_window(self, window: WindowInfo) -> Optional[str]:
        """Extract project path from window title"""
        title = window.title
        process = window.process_name.lower()

        # VS Code: "foldername - VS Code" or "filename - foldername - VS Code"
        if process == "code.exe" and " - " in title:
            parts = title.split(" - ")
            # Last part before "VS Code" is usually the folder
            for part in reversed(parts[:-1]):
                if part and part not in ["Visual Studio Code", ""]:
                    return self._resolve_path(part)

        # PyCharm / IntelliJ
        if "pycharm" in process or "idea" in process:
            if " - " in title:
                parts = title.split(" - ")
                for part in parts:
                    if "." in part or "\" in part or "/" in part:
                        return self._resolve_path(part)

        # File Explorer
        if process == "explorer.exe":
            # Try to get actual path from shell
            path = self._get_explorer_path()
            if path:
                return path
            # Fallback: window title might be folder name
            if title and title not in ["File Explorer", ""]:
                return self._resolve_path(title)

        # Terminal / PowerShell / CMD
        if process in ["cmd.exe", "powershell.exe", "windowsterminal.exe", "wt.exe"]:
            # Try to get current directory from process
            try:
                proc = psutil.Process(window.process_id)
                cwd = proc.cwd()
                if cwd and os.path.exists(cwd):
                    return cwd
            except:
                pass

        return None

    def _resolve_path(self, name: str) -> Optional[str]:
        """Try to resolve a folder name to full path"""
        # Check if it's already a full path
        if os.path.isabs(name) and os.path.exists(name):
            return name

        # Common locations to check
        search_paths = [
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Projects"),
            os.path.expanduser("~/Dev"),
            os.path.expanduser("~/GitHub"),
            os.path.expanduser("~"),
        ]

        for base in search_paths:
            full = os.path.join(base, name)
            if os.path.exists(full):
                return full

        return None

    def _get_explorer_path(self) -> Optional[str]:
        """Get current path from File Explorer using COM"""
        try:
            import comtypes
            from comtypes.client import CreateObject

            shell = CreateObject("Shell.Application")
            for window in shell.Windows():
                try:
                    if window.Document:
                        path = window.Document.Folder.Self.Path
                        if path and os.path.exists(path):
                            return path
                except:
                    continue
        except:
            pass
        return None

    def scan_project(self, path: str) -> Optional[ProjectContext]:
        """Scan a project directory and identify its type"""
        if not path or not os.path.exists(path):
            return None

        path_obj = Path(path)
        if not path_obj.is_dir():
            path_obj = path_obj.parent

        try:
            files = [f.name for f in path_obj.iterdir() if f.is_file()]
            all_files = [f.name for f in path_obj.rglob("*") if f.is_file() and f.parent == path_obj]

            # Determine project type
            project_type = self._detect_project_type(path_obj, files)

            # Get recent files (modified in last 24 hours)
            recent = []
            for f in path_obj.rglob("*"):
                if f.is_file():
                    try:
                        mtime = f.stat().st_mtime
                        if time.time() - mtime < 86400:  # 24 hours
                            recent.append((f.name, mtime))
                    except:
                        pass

            recent.sort(key=lambda x: x[1], reverse=True)

            # Check for git
            git_branch = None
            git_path = path_obj / ".git"
            if git_path.exists():
                try:
                    head = (git_path / "HEAD").read_text().strip()
                    if head.startswith("ref: "):
                        git_branch = head.replace("ref: refs/heads/", "")
                except:
                    pass

            return ProjectContext(
                path=str(path_obj),
                name=path_obj.name,
                project_type=project_type,
                files=files[:20],
                recent_files=[r[0] for r in recent[:10]],
                git_branch=git_branch,
                has_readme="README.md" in files or "README.txt" in files,
                has_package_json="package.json" in files,
                has_requirements="requirements.txt" in files,
                has_cargo_toml="Cargo.toml" in files
            )
        except Exception:
            return None

    def _detect_project_type(self, path: Path, files: List[str]) -> str:
        """Detect project type based on files"""
        # Check for specific markers
        for ptype, markers in self.PROJECT_TYPES.items():
            for marker in markers:
                if marker.startswith("."):
                    # File extension
                    if any(f.endswith(marker) for f in files):
                        return ptype
                else:
                    # Specific filename or folder
                    if marker in files or (path / marker).exists():
                        return ptype

        # Check subdirectories for game engines
        if (path / "Assets").exists() and (path / "ProjectSettings").exists():
            return "unity"
        if (path / ".godot").exists():
            return "game"

        return "unknown"

    def get_full_context(self) -> Dict:
        """Get complete desktop context"""
        context = {
            "timestamp": time.time(),
            "active_window": None,
            "active_project": None,
            "recent_projects": [],
            "system_info": {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_usage": psutil.disk_usage("/").percent
            }
        }

        # Get active window
        window = self.get_active_window()
        if window:
            context["active_window"] = {
                "title": window.title,
                "process": window.process_name,
                "minimized": window.is_minimized
            }

            # Get project from window
            project_path = self.get_project_from_window(window)
            if project_path:
                project = self.scan_project(project_path)
                if project:
                    context["active_project"] = {
                        "name": project.name,
                        "path": project.path,
                        "type": project.project_type,
                        "files": project.files[:10],
                        "recent_files": project.recent_files[:5],
                        "git_branch": project.git_branch,
                        "has_readme": project.has_readme
                    }

        # Cache result
        self._cache = context
        self.last_scan = time.time()

        return context

    def get_cached_context(self) -> Dict:
        """Get cached context or rescan if stale"""
        if self.last_scan and (time.time() - self.last_scan) < self.scan_interval:
            return self._cache
        return self.get_full_context()
