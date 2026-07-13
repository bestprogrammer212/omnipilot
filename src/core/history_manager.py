"""History and learning manager for OmniPilot"""
import json
import os
import time
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class ActionRecord:
    """Record of a single action"""
    timestamp: float
    user_prompt: str
    tool: str
    agent: Optional[str]
    model: str
    confidence: float
    reasoning: str
    success: Optional[bool] = None
    feedback: Optional[str] = None
    duration: Optional[float] = None

class HistoryManager:
    """Manages action history and learns user preferences"""

    def __init__(self, data_dir: Optional[str] = None):
        if data_dir is None:
            data_dir = os.path.expandvars(r"%APPDATA%\OmniPilot")

        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.history_file = self.data_dir / "history.json"
        self.preferences_file = self.data_dir / "preferences.json"
        self.stats_file = self.data_dir / "stats.json"

        self.history: List[ActionRecord] = []
        self.preferences: Dict = {}
        self.stats: Dict = {}

        self._load_all()

    def _load_all(self):
        """Load all persisted data"""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
                    self.history = [ActionRecord(**record) for record in data]
            except:
                self.history = []

        if self.preferences_file.exists():
            try:
                with open(self.preferences_file, 'r') as f:
                    self.preferences = json.load(f)
            except:
                self.preferences = {}

        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    self.stats = json.load(f)
            except:
                self.stats = {}

    def _save_all(self):
        """Save all data to disk"""
        with open(self.history_file, 'w') as f:
            json.dump([asdict(record) for record in self.history], f, indent=2)

        with open(self.preferences_file, 'w') as f:
            json.dump(self.preferences, f, indent=2)

        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)

    def add_action(self, record: ActionRecord):
        """Add a new action to history"""
        self.history.append(record)

        # Keep only last 1000 records
        if len(self.history) > 1000:
            self.history = self.history[-1000:]

        self._update_stats(record)
        self._save_all()

    def _update_stats(self, record: ActionRecord):
        """Update usage statistics"""
        tool = record.tool
        agent = record.agent or "none"

        if "tools" not in self.stats:
            self.stats["tools"] = {}
        if "agents" not in self.stats:
            self.stats["agents"] = {}

        # Tool usage count
        if tool not in self.stats["tools"]:
            self.stats["tools"][tool] = {"count": 0, "success": 0, "fail": 0}
        self.stats["tools"][tool]["count"] += 1

        if record.success is True:
            self.stats["tools"][tool]["success"] += 1
        elif record.success is False:
            self.stats["tools"][tool]["fail"] += 1

        # Agent usage count
        if agent not in self.stats["agents"]:
            self.stats["agents"][agent] = {"count": 0}
        self.stats["agents"][agent]["count"] += 1

    def get_recent_history(self, count: int = 10) -> List[ActionRecord]:
        """Get recent actions"""
        return self.history[-count:]

    def get_tool_preference(self, prompt_keywords: List[str]) -> Optional[str]:
        """Learn from history: which tool was used for similar prompts"""
        if not self.history:
            return None

        # Find similar prompts in history
        similar = []
        for record in self.history:
            record_words = set(record.user_prompt.lower().split())
            keyword_set = set(kw.lower() for kw in prompt_keywords)
            overlap = len(record_words & keyword_set)
            if overlap > 0:
                similar.append((overlap, record))

        if not similar:
            return None

        # Sort by overlap and return most common tool
        similar.sort(key=lambda x: x[0], reverse=True)
        top = similar[:20]

        tool_counts = {}
        for _, record in top:
            tool_counts[record.tool] = tool_counts.get(record.tool, 0) + 1

        if tool_counts:
            return max(tool_counts, key=tool_counts.get)

        return None

    def get_success_rate(self, tool: str) -> float:
        """Get success rate for a tool"""
        if "tools" not in self.stats or tool not in self.stats["tools"]:
            return 0.5  # Default 50%

        tool_stats = self.stats["tools"][tool]
        total = tool_stats.get("success", 0) + tool_stats.get("fail", 0)

        if total == 0:
            return 0.5

        return tool_stats["success"] / total

    def record_feedback(self, timestamp: float, success: bool, feedback: Optional[str] = None):
        """Record user feedback for an action"""
        for record in self.history:
            if record.timestamp == timestamp:
                record.success = success
                record.feedback = feedback
                self._update_stats(record)
                self._save_all()
                return True
        return False

    def get_stats_summary(self) -> Dict:
        """Get summary statistics"""
        total_actions = len(self.history)

        if total_actions == 0:
            return {"total": 0, "message": "No history yet"}

        tool_usage = {}
        for record in self.history:
            tool = record.tool
            tool_usage[tool] = tool_usage.get(tool, 0) + 1

        # Most used tool
        most_used = max(tool_usage, key=tool_usage.get) if tool_usage else None

        # Average confidence
        avg_confidence = sum(r.confidence for r in self.history) / total_actions

        # Success rate (for actions with feedback)
        with_feedback = [r for r in self.history if r.success is not None]
        success_rate = sum(1 for r in with_feedback if r.success) / len(with_feedback) if with_feedback else None

        return {
            "total_actions": total_actions,
            "most_used_tool": most_used,
            "tool_distribution": tool_usage,
            "average_confidence": round(avg_confidence, 2),
            "success_rate": round(success_rate, 2) if success_rate else None,
            "actions_with_feedback": len(with_feedback)
        }

    def clear_history(self):
        """Clear all history (with confirmation)"""
        self.history = []
        self.stats = {}
        self._save_all()
