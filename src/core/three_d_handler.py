"""3D generation handler for OmniPilot - manages AI 3D Generator Pro"""
import subprocess
import os
import time
from typing import Optional, Dict
from dataclasses import dataclass

@dataclass
class Model3DConfig:
    """Configuration for 3D model generation"""
    input_type: str  # "image" or "text"
    input_path: Optional[str] = None  # Path to image file
    prompt: Optional[str] = None  # Text prompt
    model_type: str = "triposr"  # "triposr" or "stable_fast_3d"
    output_format: str = "stl"  # "stl", "obj", "glb", "ply", "gltf"
    inference_steps: int = 50
    guidance_scale: float = 7.5
    frame_size: int = 512

class ThreeDHandler:
    """Handles 3D generation via AI 3D Generator Pro"""

    APP_NAME = "AI 3D Generator Pro"

    def __init__(self):
        self.app_path = self._find_app()

    def _find_app(self) -> Optional[str]:
        """Find AI 3D Generator Pro installation"""
        # Common install locations
        possible_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\AI 3D Generator Pro.exe"),
            os.path.expandvars(r"%PROGRAMFILES%\AI 3D Generator Pro\AI 3D Generator Pro.exe"),
            os.path.expandvars(r"%PROGRAMFILES(X86)%\AI 3D Generator Pro\AI 3D Generator Pro.exe"),
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\AI 3D Generator Pro\AI 3D Generator Pro.exe"),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        # Try to find via Start Menu
        start_menu_paths = [
            os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\AI 3D Generator Pro.lnk"),
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\AI 3D Generator Pro.lnk"),
        ]

        for path in start_menu_paths:
            if os.path.exists(path):
                return path

        return None

    def is_installed(self) -> bool:
        """Check if AI 3D Generator Pro is installed"""
        return self.app_path is not None

    def launch_app(self) -> bool:
        """Launch AI 3D Generator Pro"""
        if not self.is_installed():
            print("AI 3D Generator Pro not found. Install from Microsoft Store.")
            print("ms-windows-store://pdp/?productid=9PBW96JQBB91")
            return False

        try:
            # Check if already running
            import psutil
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and '3d generator' in proc.info['name'].lower():
                    print("AI 3D Generator Pro is already running")
                    return True

            # Launch the app
            if self.app_path.endswith('.lnk'):
                # Start Menu shortcut
                os.startfile(self.app_path)
            else:
                subprocess.Popen(
                    [self.app_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )

            time.sleep(3)  # Wait for app to open
            return True

        except Exception as e:
            print(f"Failed to launch AI 3D Generator Pro: {e}")
            return False

    def generate_from_image(self, image_path: str, config: Model3DConfig) -> bool:
        """Generate 3D model from image"""
        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            return False

        if not self.launch_app():
            return False

        # Note: AI 3D Generator Pro is a GUI app
        # We can't directly control it via CLI
        # User needs to manually:
        # 1. Click "Import Image" in the app
        # 2. Select the image_path
        # 3. Select model (TripoSR or Stable Fast 3D)
        # 4. Click Generate
        # 5. Export as STL

        print(f"\n📸 AI 3D Generator Pro opened")
        print(f"👉 Please:")
        print(f"   1. Click 'Import Image'")
        print(f"   2. Select: {image_path}")
        print(f"   3. Choose model: {config.model_type}")
        print(f"   4. Click 'Generate'")
        print(f"   5. Export as: {config.output_format.upper()}")
        print(f"   6. Import to Cura/PrusaSlicer for printing")

        return True

    def generate_from_text(self, prompt: str, config: Model3DConfig) -> bool:
        """Generate 3D model from text prompt"""
        if not self.launch_app():
            return False

        print(f"\n📝 AI 3D Generator Pro opened")
        print(f"👉 Please:")
        print(f"   1. Switch to 'Text to 3D' mode")
        print(f"   2. Enter prompt: {prompt}")
        print(f"   3. Choose model: {config.model_type}")
        print(f"   4. Click 'Generate'")
        print(f"   5. Export as: {config.output_format.upper()}")
        print(f"   6. Import to Cura/PrusaSlicer for printing")

        return True

    def get_workflow(self, task_type: str) -> str:
        """Get workflow instructions for different 3D tasks"""

        workflows = {
            "image_to_3d": """
Image-to-3D Workflow:
1. Take or select a photo of the object
2. Open AI 3D Generator Pro
3. Import the image
4. Select model (TripoSR = fast, Stable Fast 3D = balanced)
5. Generate 3D model
6. Preview in 3D viewer
7. Export as STL (for 3D printing) or OBJ/GLB (for other uses)
8. Import to Cura or PrusaSlicer
9. Slice for Elegoo Neptune 4 Pro
10. Print!
""",
            "text_to_3d": """
Text-to-3D Workflow:
1. Open AI 3D Generator Pro
2. Switch to Text-to-3D mode
3. Describe what you want (e.g., "medieval wooden chair with curved legs")
4. Select model (TripoSR = fast, Stable Fast 3D = balanced)
5. Generate 3D model
6. Preview and refine if needed
7. Export as STL
8. Slice and print on Elegoo Neptune 4 Pro
""",
            "print_ready": """
Print-Ready Workflow:
1. Generate or load 3D model
2. Check for manifold edges (no holes)
3. Check wall thickness (min 0.8mm for FDM)
4. Add supports if needed (overhangs > 45°)
5. Export as STL
6. Import to Cura:
   - Profile: Elegoo Neptune 4 Pro
   - Layer height: 0.2mm (standard) or 0.12mm (fine)
   - Infill: 20% (standard) or 50% (strong)
   - Supports: Touching buildplate (if needed)
7. Slice and preview
8. Save G-code to SD card or send via USB
9. Print!
"""
        }

        return workflows.get(task_type, "Unknown workflow")

    def suggest_settings(self, filament_type: str) -> Dict:
        """Suggest print settings for different filaments"""

        settings = {
            "pla": {
                "nozzle_temp": 200,
                "bed_temp": 60,
                "speed": 50,
                "retraction": 6,
                "fan_speed": 100
            },
            "ht_pla_gf": {
                "nozzle_temp": 220,
                "bed_temp": 70,
                "speed": 40,
                "retraction": 4,
                "fan_speed": 80
            },
            "pa6_gf": {
                "nozzle_temp": 260,
                "bed_temp": 80,
                "speed": 30,
                "retraction": 2,
                "fan_speed": 50
            },
            "pa_gf": {
                "nozzle_temp": 250,
                "bed_temp": 75,
                "speed": 35,
                "retraction": 3,
                "fan_speed": 60
            },
            "pa_cf": {
                "nozzle_temp": 270,
                "bed_temp": 85,
                "speed": 25,
                "retraction": 2,
                "fan_speed": 40
            }
        }

        return settings.get(filament_type.lower(), settings["pla"])
