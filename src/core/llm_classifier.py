"""LLM-based intelligent classification for OmniPilot"""
import json
import requests
from typing import Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class ClassificationResult:
    tool: str
    agent: Optional[str]
    model: str
    confidence: float
    reasoning: str
    suggested_prompt: Optional[str] = None

class LLMClassifier:
    """Uses local Ollama LLM for intelligent prompt classification"""

    def __init__(self, ollama_url: str = "http://localhost:11434", model: str = "phi4"):
        self.ollama_url = ollama_url
        self.model = model
        self.api_generate = f"{ollama_url}/api/generate"

    def _call_ollama(self, prompt: str, system: str = None, format_json: bool = True) -> str:
        """Call local Ollama instance"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 500
            }
        }

        if system:
            payload["system"] = system

        if format_json:
            payload["format"] = "json"

        try:
            response = requests.post(self.api_generate, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Ollama not running. Start with: ollama serve")
        except Exception as e:
            raise RuntimeError(f"LLM call failed: {e}")

    def classify(self, user_prompt: str, context: Dict) -> ClassificationResult:
        """Classify user prompt with context awareness"""

        system_prompt = """You are an AI orchestrator for a development environment. 
Analyze the user request and desktop context, then select the best tool and agent.

Available tools:
- opencode: Coding agent with specialist roles. Best for: writing code, refactoring, tests, web development, games, embedded systems (micro:bit, Arduino, ESP32), code review, 3D printing design
- hermes: Autonomous coding agent with memory. Best for: large project planning, system architecture, complex refactoring across many files
- interpreter: General-purpose desktop assistant. Best for: file creation, browser automation, desktop control, reading documents, running commands
- ai3d: 3D model generator. Best for: generating 3D models from images or text, creating STL files for 3D printing, mesh generation

Available agents for opencode:
- game-developer: Games, game mechanics, collision detection, pygame, HTML5 canvas, Unity, Godot
- web-developer: PWAs, HTML, CSS, JavaScript, React, Vue, websites, service workers
- embedded-developer: micro:bit, Arduino, ESP32, sensors, GPIO, circuits, firmware
- code-reviewer: Code review, bug fixing, security analysis, performance optimization
- 3d-designer: 3D printing, Elegoo Neptune, Cura, PrusaSlicer, STL, mesh optimization
- ai-engineer: Local AI, Ollama, LLMs, model deployment, embeddings
- frontend-developer: React, Vue, Angular, UI components, TypeScript, Tailwind
- testing-engineer: Unit tests, integration tests, QA, Cypress, Selenium, pytest
- level-designer: Game levels, maps, layout, pacing, encounters, tilemaps
- ui-designer: Visual design, components, Figma, design systems, typography

Models:
- qwen3:8b: Best for coding tasks, fast, good at multiple languages
- devstral:24b: Best for complex agentic tasks, large context, refactoring
- phi4: Best for quick tasks, general purpose, low resource usage

Respond in JSON format only."""

        context_str = json.dumps(context, indent=2, ensure_ascii=False)

        classification_prompt = f"""User request: "{user_prompt}"

Desktop context:
{context_str}

Analyze:
1. What is the user trying to accomplish?
2. What type of project is active (if any)?
3. What tool is best suited?
4. What agent (if opencode) is most appropriate?
5. What model should be used?

Respond in this exact JSON format:
{{
    "tool": "opencode|hermes|interpreter|ai3d",
    "agent": "game-developer|web-developer|embedded-developer|code-reviewer|3d-designer|ai-engineer|frontend-developer|testing-engineer|level-designer|ui-designer|null",
    "model": "qwen3:8b|devstral:24b|phi4",
    "confidence": 0.0-1.0,
    "reasoning": "Brief explanation in English",
    "suggested_prompt": "Optional improved prompt for the target tool"
}}"""

        try:
            response = self._call_ollama(classification_prompt, system_prompt)
            result = json.loads(response)

            return ClassificationResult(
                tool=result.get("tool", "opencode"),
                agent=result.get("agent") if result.get("agent") != "null" else None,
                model=result.get("model", "qwen3:8b"),
                confidence=float(result.get("confidence", 0.5)),
                reasoning=result.get("reasoning", "No reasoning provided"),
                suggested_prompt=result.get("suggested_prompt")
            )
        except (json.JSONDecodeError, KeyError) as e:
            # Fallback to keyword-based classification
            return self._fallback_classify(user_prompt, context)
        except RuntimeError:
            # Ollama not available, use fallback
            return self._fallback_classify(user_prompt, context)

    def _fallback_classify(self, user_prompt: str, context: Dict) -> ClassificationResult:
        """Fallback keyword-based classification when LLM is unavailable"""
        from ..agents.tool_registry import get_tool_for_prompt, get_agent_for_prompt

        tool = get_tool_for_prompt(user_prompt)
        agent = get_agent_for_prompt(user_prompt)

        model_map = {
            "hermes": "devstral:24b",
            "opencode": "qwen3:8b",
            "interpreter": "phi4",
            "ai3d": None
        }

        return ClassificationResult(
            tool=tool,
            agent=agent.name if agent else None,
            model=model_map.get(tool, "qwen3:8b"),
            confidence=0.6,
            reasoning=f"Fallback classification based on keywords. Tool: {tool}, Agent: {agent.name if agent else 'none'}"
        )

    def enhance_prompt(self, user_prompt: str, classification: ClassificationResult) -> str:
        """Enhance user prompt with context for the target tool"""

        if classification.suggested_prompt:
            return classification.suggested_prompt

        # Add agent context if opencode
        if classification.tool == "opencode" and classification.agent:
            return f"[Using {classification.agent} agent] {user_prompt}"

        return user_prompt
