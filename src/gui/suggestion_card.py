"""Suggestion card widget for OmniPilot - shows recommended tool/agent/model"""
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class SuggestionCard(QFrame):
    """Card showing a tool suggestion with launch button"""

    launch_requested = pyqtSignal(str, str, str)  # tool, agent, model

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("suggestionCard")
        self._setup_ui()
        self._current_tool = None
        self._current_agent = None
        self._current_model = None

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)

        # Header row: Tool name + confidence
        header = QHBoxLayout()

        self.tool_label = QLabel("Waiting for analysis...")
        self.tool_label.setObjectName("suggestionTool")
        header.addWidget(self.tool_label)

        header.addStretch()

        self.confidence_label = QLabel("")
        self.confidence_label.setObjectName("suggestionConfidence")
        header.addWidget(self.confidence_label)

        layout.addLayout(header)

        # Agent tag (if applicable)
        self.agent_label = QLabel("")
        self.agent_label.setObjectName("suggestionAgent")
        self.agent_label.setVisible(False)
        layout.addWidget(self.agent_label)

        # Model info
        self.model_label = QLabel("")
        self.model_label.setObjectName("suggestionModel")
        layout.addWidget(self.model_label)

        # Reasoning
        self.reasoning_label = QLabel("")
        self.reasoning_label.setObjectName("suggestionReasoning")
        self.reasoning_label.setWordWrap(True)
        layout.addWidget(self.reasoning_label)

        # Spacer
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Action buttons
        buttons = QHBoxLayout()

        self.change_btn = QPushButton("⚙️ Change")
        self.change_btn.setObjectName("secondaryButton")
        self.change_btn.setToolTip("Manually select different tool")
        self.change_btn.clicked.connect(self._on_change)
        buttons.addWidget(self.change_btn)

        buttons.addStretch()

        self.launch_btn = QPushButton("🚀 Launch")
        self.launch_btn.setObjectName("primaryButton")
        self.launch_btn.setToolTip("Start the selected tool")
        self.launch_btn.clicked.connect(self._on_launch)
        self.launch_btn.setEnabled(False)
        buttons.addWidget(self.launch_btn)

        layout.addLayout(buttons)

    def set_suggestion(self, tool: str, agent: str = None, model: str = None, 
                       confidence: float = 0.0, reasoning: str = ""):
        """Update card with new suggestion"""
        self._current_tool = tool
        self._current_agent = agent
        self._current_model = model

        # Tool name
        tool_names = {
            "opencode": "OpenCode",
            "hermes": "Hermes Agent",
            "interpreter": "Open Interpreter",
            "ai3d": "AI 3D Generator Pro"
        }
        self.tool_label.setText(f"🎯 {tool_names.get(tool, tool)}")

        # Confidence
        if confidence > 0:
            conf_emoji = "🟢" if confidence > 0.8 else "🟡" if confidence > 0.5 else "🔴"
            self.confidence_label.setText(f"{conf_emoji} {confidence:.0%}")
        else:
            self.confidence_label.setText("")

        # Agent
        if agent:
            self.agent_label.setText(f"👤 {agent}")
            self.agent_label.setVisible(True)
        else:
            self.agent_label.setVisible(False)

        # Model
        if model:
            self.model_label.setText(f"🧠 Model: {model}")
        else:
            self.model_label.setText("")

        # Reasoning
        if reasoning:
            self.reasoning_label.setText(f"💡 {reasoning}")
        else:
            self.reasoning_label.setText("")

        self.launch_btn.setEnabled(True)

    def clear(self):
        """Clear suggestion"""
        self._current_tool = None
        self._current_agent = None
        self._current_model = None
        self.tool_label.setText("Waiting for analysis...")
        self.confidence_label.setText("")
        self.agent_label.setVisible(False)
        self.model_label.setText("")
        self.reasoning_label.setText("")
        self.launch_btn.setEnabled(False)

    def set_loading(self, loading: bool):
        """Show loading state"""
        self.launch_btn.setEnabled(not loading)
        self.change_btn.setEnabled(not loading)
        if loading:
            self.tool_label.setText("🔄 Analyzing...")

    def _on_launch(self):
        """Emit launch signal"""
        if self._current_tool:
            self.launch_requested.emit(
                self._current_tool,
                self._current_agent or "",
                self._current_model or ""
            )

    def _on_change(self):
        """Show manual selection dialog"""
        # TODO: Implement manual tool selection dialog
        pass
