"""Input widget for OmniPilot - prompt entry area"""
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QTextEdit, 
    QPushButton, QLabel, QProgressBar
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QKeyEvent

class PromptInputWidget(QFrame):
    """Main input widget for entering prompts"""

    submit_prompt = pyqtSignal(str)
    analyze_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("inputFrame")
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)

        # Header
        header = QHBoxLayout()

        self.title_label = QLabel("What do you want to do?")
        self.title_label.setObjectName("contextTitle")
        header.addWidget(self.title_label)

        header.addStretch()

        self.char_count = QLabel("0 chars")
        self.char_count.setObjectName("contextValue")
        header.addWidget(self.char_count)

        layout.addLayout(header)

        # Text input
        self.text_input = QTextEdit()
        self.text_input.setObjectName("promptInput")
        self.text_input.setPlaceholderText(
            "Describe what you want to do...\n"
            "Examples:\n"
            "• Create a micro:bit game with collision detection\n"
            "• Build a PWA with camera and OCR\n"
            "• Generate a 3D model of a dragon for printing\n"
            "• Refactor my authentication code"
        )
        self.text_input.setMaximumHeight(120)
        self.text_input.textChanged.connect(self._on_text_changed)
        layout.addWidget(self.text_input)

        # Buttons row
        buttons = QHBoxLayout()

        self.analyze_btn = QPushButton("🔍 Analyze")
        self.analyze_btn.setObjectName("secondaryButton")
        self.analyze_btn.setToolTip("Analyze context and suggest tools")
        self.analyze_btn.clicked.connect(self.analyze_requested.emit)
        buttons.addWidget(self.analyze_btn)

        buttons.addStretch()

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setObjectName("secondaryButton")
        self.clear_btn.clicked.connect(self.clear)
        buttons.addWidget(self.clear_btn)

        self.submit_btn = QPushButton("🚀 Launch")
        self.submit_btn.setObjectName("primaryButton")
        self.submit_btn.setToolTip("Ctrl+Enter to submit")
        self.submit_btn.clicked.connect(self._on_submit)
        buttons.addWidget(self.submit_btn)

        layout.addLayout(buttons)

        # Progress bar (hidden by default)
        self.progress = QProgressBar()
        self.progress.setObjectName("progressBar")
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

    def _on_text_changed(self):
        """Update character count"""
        text = self.text_input.toPlainText()
        self.char_count.setText(f"{len(text)} chars")

        # Enable submit if text is not empty
        self.submit_btn.setEnabled(len(text.strip()) > 0)

    def _on_submit(self):
        """Emit submit signal with prompt text"""
        text = self.text_input.toPlainText().strip()
        if text:
            self.submit_prompt.emit(text)

    def keyPressEvent(self, event: QKeyEvent):
        """Handle Ctrl+Enter shortcut"""
        if event.key() == Qt.Key.Key_Return and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self._on_submit()
        else:
            super().keyPressEvent(event)

    def get_prompt(self) -> str:
        """Get current prompt text"""
        return self.text_input.toPlainText().strip()

    def clear(self):
        """Clear input"""
        self.text_input.clear()
        self.progress.setVisible(False)

    def set_loading(self, loading: bool, message: str = ""):
        """Show/hide loading state"""
        self.submit_btn.setEnabled(not loading)
        self.analyze_btn.setEnabled(not loading)
        self.text_input.setReadOnly(loading)

        if loading:
            self.progress.setVisible(True)
            self.progress.setRange(0, 0)  # Indeterminate
            if message:
                self.title_label.setText(message)
        else:
            self.progress.setVisible(False)
            self.progress.setRange(0, 100)
            self.title_label.setText("What do you want to do?")

    def set_analyzing(self, analyzing: bool):
        """Show analyzing state"""
        if analyzing:
            self.analyze_btn.setText("Analyzing...")
            self.analyze_btn.setEnabled(False)
        else:
            self.analyze_btn.setText("🔍 Analyze")
            self.analyze_btn.setEnabled(True)
