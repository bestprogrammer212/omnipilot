"""Tests for LLM classifier"""
import unittest
from src.core.llm_classifier import LLMClassifier, ClassificationResult
from src.agents.tool_registry import get_agent_for_prompt, get_tool_for_prompt

class TestKeywordClassification(unittest.TestCase):
    """Test keyword-based fallback classification"""

    def test_game_detection(self):
        """Detect game-related prompts"""
        prompts = [
            "Create a micro:bit game",
            "Build a flappy bird clone",
            "Make a platformer in Python",
        ]
        for prompt in prompts:
            tool = get_tool_for_prompt(prompt)
            agent = get_agent_for_prompt(prompt)
            self.assertEqual(tool, "opencode")
            self.assertIsNotNone(agent)
            self.assertEqual(agent.name, "Game Developer")

    def test_web_detection(self):
        """Detect web-related prompts"""
        prompts = [
            "Create a PWA with camera",
            "Build a responsive website",
            "Make a React app",
        ]
        for prompt in prompts:
            tool = get_tool_for_prompt(prompt)
            agent = get_agent_for_prompt(prompt)
            self.assertEqual(tool, "opencode")
            self.assertIsNotNone(agent)
            self.assertEqual(agent.name, "Web Developer")

    def test_3d_detection(self):
        """Detect 3D/printing prompts"""
        prompts = [
            "Generate a 3D model of a dragon",
            "Create STL file for printing",
            "Make a figurine for Elegoo Neptune",
        ]
        for prompt in prompts:
            tool = get_tool_for_prompt(prompt)
            self.assertEqual(tool, "ai3d")

    def test_hermes_detection(self):
        """Detect large project prompts"""
        prompts = [
            "Plan a complete project architecture",
            "Design system for microservices",
            "Refactor entire codebase",
        ]
        for prompt in prompts:
            tool = get_tool_for_prompt(prompt)
            self.assertEqual(tool, "hermes")

    def test_interpreter_detection(self):
        """Detect general task prompts"""
        prompts = [
            "Create a file on desktop",
            "Open browser and search",
            "Read this PDF document",
        ]
        for prompt in prompts:
            tool = get_tool_for_prompt(prompt)
            self.assertEqual(tool, "interpreter")

class TestLLMClassification(unittest.TestCase):
    """Test LLM-based classification (requires Ollama)"""

    def setUp(self):
        self.classifier = LLMClassifier(model="phi4")

    def test_classify_with_context(self):
        """Test classification with context"""
        context = {
            "active_project": {
                "name": "MyGame",
                "type": "python",
                "path": "C:/Users/Test/Documents/MyGame"
            }
        }

        try:
            result = self.classifier.classify("Add collision detection to player", context)
            self.assertIn(result.tool, ["opencode", "hermes", "interpreter", "ai3d"])
            self.assertIsInstance(result.confidence, float)
            self.assertGreaterEqual(result.confidence, 0)
            self.assertLessEqual(result.confidence, 1)
        except RuntimeError:
            self.skipTest("Ollama not available")

if __name__ == "__main__":
    unittest.main()
