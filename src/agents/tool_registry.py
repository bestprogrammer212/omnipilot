"""Tool and Agent Registry for OmniPilot"""
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Agent:
    name: str
    description: str
    keywords: List[str]
    tool: str
    model: str
    division: str

@dataclass
class Tool:
    name: str
    executable: str
    description: str
    requires_ollama: bool
    default_model: Optional[str] = None
    supports_agents: bool = False

# Tool definitions
TOOLS: Dict[str, Tool] = {
    "opencode": Tool(
        name="OpenCode",
        executable="opencode",
        description="Coding agent with specialist roles",
        requires_ollama=True,
        default_model="qwen3:8b",
        supports_agents=True
    ),
    "hermes": Tool(
        name="Hermes Agent",
        executable="hermes",
        description="Autonomous coding agent with memory",
        requires_ollama=True,
        default_model="devstral:24b",
        supports_agents=False
    ),
    "interpreter": Tool(
        name="Open Interpreter",
        executable="interpreter",
        description="General-purpose desktop assistant",
        requires_ollama=True,
        default_model="phi4",
        supports_agents=False
    ),
    "ai3d": Tool(
        name="AI 3D Generator Pro",
        executable="AI 3D Generator Pro",
        description="Image-to-3D and text-to-3D generation",
        requires_ollama=False,
        default_model=None,
        supports_agents=False
    )
}

# Agent definitions from Agency Agents catalog
AGENTS: Dict[str, Agent] = {
    "game-developer": Agent(
        name="Game Developer",
        description="Expert in browser games, Python games, and micro:bit games",
        keywords=["game", "spiel", "collision", "level", "sprite", "pygame", "canvas", "unity", "godot", "roblox", "mechanic", "score", "health", "enemy"],
        tool="opencode",
        model="qwen3:8b",
        division="Game Dev"
    ),
    "web-developer": Agent(
        name="Web Developer",
        description="Full-stack web developer specializing in PWAs, vanilla JS, and modern CSS",
        keywords=["web", "html", "css", "javascript", "pwa", "website", "manifest", "service worker", "responsive", "react", "vue", "frontend"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "embedded-developer": Agent(
        name="Embedded Developer",
        description="Expert in micro:bit, Arduino, and ESP32 development",
        keywords=["microbit", "micro:bit", "arduino", "esp32", "sensor", "pin", "gpio", "i2c", "spi", "firmware", "hardware", "circuit", "wiring"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "code-reviewer": Agent(
        name="Code Reviewer",
        description="Senior code reviewer for security, performance, and style",
        keywords=["review", "bug", "fix", "security", "refactor", "optimize", "test", "coverage", "vulnerability", "performance", "memory leak"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "3d-designer": Agent(
        name="3D Printing Designer",
        description="3D printing and CAD expert for Elegoo Neptune 4 Pro",
        keywords=["3d print", "elegoo", "neptune", "filament", "slicer", "cura", "prusaslicer", "stl", "mesh", "overhang", "support", "nozzle", "temperature"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "ai-engineer": Agent(
        name="AI Engineer",
        description="Expert in local AI, Ollama, and model deployment",
        keywords=["ai", "ollama", "model", "llm", "neural", "training", "inference", "quantization", "fine-tune", "embedding", "vector"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "frontend-developer": Agent(
        name="Frontend Developer",
        description="React/Vue/Angular, UI components, performance",
        keywords=["frontend", "react", "vue", "angular", "component", "ui", "ux", "typescript", "sass", "tailwind"],
        tool="opencode",
        model="qwen3:8b",
        division="Engineering"
    ),
    "testing-engineer": Agent(
        name="Testing Engineer",
        description="QA, unit tests, integration tests, automation",
        keywords=["test", "testing", "qa", "unit test", "integration", "cypress", "selenium", "pytest", "jest", "automation"],
        tool="opencode",
        model="qwen3:8b",
        division="Testing"
    ),
    "level-designer": Agent(
        name="Level Designer",
        description="Game level design, layout, pacing, encounter design",
        keywords=["level", "map", "layout", "pacing", "encounter", "dungeon", "world", "terrain", "tilemap"],
        tool="opencode",
        model="qwen3:8b",
        division="Game Dev"
    ),
    "ui-designer": Agent(
        name="UI Designer",
        description="Visual design, components, design systems",
        keywords=["design", "ui", "visual", "component", "figma", "sketch", "palette", "typography", "icon", "layout"],
        tool="opencode",
        model="qwen3:8b",
        division="Design"
    )
}

# Keyword-to-tool mapping for quick classification
KEYWORD_TOOLS: Dict[str, str] = {
    # OpenCode agents
    "refactor": "opencode",
    "test": "opencode",
    "microbit": "opencode",
    "micro:bit": "opencode",
    "arduino": "opencode",
    "esp32": "opencode",
    "spiel": "opencode",
    "game": "opencode",
    "html": "opencode",
    "pwa": "opencode",
    "website": "opencode",
    "3d printing": "opencode",
    "elegoo": "opencode",
    "neptune": "opencode",
    "ai model": "opencode",
    "ollama": "opencode",
    "frontend": "opencode",
    "testing": "opencode",
    "level": "opencode",
    "ui design": "opencode",

    # Hermes (large projects)
    "plan project": "hermes",
    "project plan": "hermes",
    "architecture": "hermes",
    "architecture": "hermes",
    "large refactoring": "hermes",
    "large refactor": "hermes",
    "system design": "hermes",
    "plan project": "hermes",

    # Open Interpreter
    "create file": "interpreter",
    "create file": "interpreter",
    "open browser": "interpreter",
    "open browser": "interpreter",
    "desktop": "interpreter",
    "read pdf": "interpreter",
    "read pdf": "interpreter",
    "automation": "interpreter",
    "script": "interpreter",
    "command": "interpreter",

    # AI 3D Generator Pro
    "3d modell": "ai3d",
    "3d model": "ai3d",
    "image to 3d": "ai3d",
    "image to 3d": "ai3d",
    "stl": "ai3d",
    "print": "ai3d",
    "print": "ai3d",
    "mesh": "ai3d",
    "generate 3d": "ai3d",
    "blender": "ai3d",
    "cad": "ai3d"
}

def get_agent_for_prompt(prompt: str) -> Optional[Agent]:
    """Find best agent based on prompt keywords"""
    prompt_lower = prompt.lower()

    best_agent = None
    best_score = 0

    for agent_id, agent in AGENTS.items():
        score = 0
        for keyword in agent.keywords:
            if keyword in prompt_lower:
                score += 1
                # Exact match gets higher score
                if keyword == prompt_lower.strip():
                    score += 5

        if score > best_score:
            best_score = score
            best_agent = agent

    return best_agent

def get_tool_for_prompt(prompt: str) -> str:
    """Quick keyword-based tool detection"""
    prompt_lower = prompt.lower()

    for keyword, tool in KEYWORD_TOOLS.items():
        if keyword in prompt_lower:
            return tool

    # Default to opencode for coding-related prompts
    coding_keywords = ["code", "program", "function", "class", "bug", "error", "fix", "implement", "write"]
    if any(kw in prompt_lower for kw in coding_keywords):
        return "opencode"

    return "interpreter"  # Default fallback
