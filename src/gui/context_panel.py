"""Context panel for OmniPilot - shows desktop and project context"""
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
    QGridLayout, QScrollArea, QWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class ContextPanel(QFrame):
    """Displays current desktop and project context"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("contextPanel")
        self._setup_ui()
        self._clear_context()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 16, 16, 16)

        # Header
        header = QHBoxLayout()
        self.header_label = QLabel("📁 Context")
        self.header_label.setObjectName("contextTitle")
        header.addWidget(self.header_label)
        header.addStretch()

        self.refresh_label = QLabel("Scanning...")
        self.refresh_label.setObjectName("contextValue")
        self.refresh_label.setVisible(False)
        header.addWidget(self.refresh_label)

        layout.addLayout(header)

        # Context grid
        self.grid = QGridLayout()
        self.grid.setSpacing(8)
        self.grid.setColumnStretch(1, 1)

        # Row 0: Active Window
        self.grid.addWidget(self._create_label("Active Window:", "contextItem"), 0, 0)
        self.active_window_label = self._create_value_label("Detecting...")
        self.grid.addWidget(self.active_window_label, 0, 1)

        # Row 1: Active Project
        self.grid.addWidget(self._create_label("Project:", "contextItem"), 1, 0)
        self.project_label = self._create_value_label("Scanning...")
        self.grid.addWidget(self.project_label, 1, 1)

        # Row 2: Project Type
        self.grid.addWidget(self._create_label("Type:", "contextItem"), 2, 0)
        self.project_type_label = self._create_value_label("—")
        self.grid.addWidget(self.project_type_label, 2, 1)

        # Row 3: Git Branch
        self.grid.addWidget(self._create_label("Git Branch:", "contextItem"), 3, 0)
        self.git_branch_label = self._create_value_label("—")
        self.grid.addWidget(self.git_branch_label, 3, 1)

        # Row 4: Recent Files
        self.grid.addWidget(self._create_label("Recent Files:", "contextItem"), 4, 0)
        self.recent_files_label = self._create_value_label("—")
        self.recent_files_label.setWordWrap(True)
        self.grid.addWidget(self.recent_files_label, 4, 1)

        # Row 5: System Info
        self.grid.addWidget(self._create_label("System:", "contextItem"), 5, 0)
        self.system_label = self._create_value_label("Scanning...")
        self.grid.addWidget(self.system_label, 5, 1)

        layout.addLayout(self.grid)
        layout.addStretch()

    def _create_label(self, text: str, obj_name: str) -> QLabel:
        """Create a styled label"""
        label = QLabel(text)
        label.setObjectName(obj_name)
        return label

    def _create_value_label(self, text: str) -> QLabel:
        """Create a value label with highlight style"""
        label = QLabel(text)
        label.setObjectName("contextHighlight")
        label.setWordWrap(True)
        return label

    def _clear_context(self):
        """Reset all context fields"""
        self.active_window_label.setText("—")
        self.project_label.setText("—")
        self.project_type_label.setText("—")
        self.git_branch_label.setText("—")
        self.recent_files_label.setText("—")
        self.system_label.setText("—")

    def update_context(self, context: dict):
        """Update context display with new data"""
        # Active window
        if context.get("active_window"):
            aw = context["active_window"]
            title = aw.get("title", "Unknown")[:50]
            proc = aw.get("process", "Unknown")
            self.active_window_label.setText(f"{title} ({proc})")
        else:
            self.active_window_label.setText("—")

        # Active project
        if context.get("active_project"):
            ap = context["active_project"]
            name = ap.get("name", "Unknown")
            path = ap.get("path", "")
            self.project_label.setText(f"{name}")
            self.project_label.setToolTip(path)

            # Project type
            ptype = ap.get("type", "unknown")
            self.project_type_label.setText(ptype.upper())

            # Git branch
            branch = ap.get("git_branch")
            if branch:
                self.git_branch_label.setText(f"🌿 {branch}")
            else:
                self.git_branch_label.setText("—")

            # Recent files
            recent = ap.get("recent_files", [])
            if recent:
                files_text = ", ".join(recent[:5])
                self.recent_files_label.setText(files_text)
            else:
                self.recent_files_label.setText("—")
        else:
            self.project_label.setText("—")
            self.project_type_label.setText("—")
            self.git_branch_label.setText("—")
            self.recent_files_label.setText("—")

        # System info
        sys_info = context.get("system_info", {})
        if sys_info:
            cpu = sys_info.get("cpu_percent", 0)
            mem = sys_info.get("memory_percent", 0)
            disk = sys_info.get("disk_usage", 0)
            self.system_label.setText(f"CPU: {cpu:.0f}% | RAM: {mem:.0f}% | Disk: {disk:.0f}%")
        else:
            self.system_label.setText("—")

    def set_scanning(self, scanning: bool):
        """Show scanning indicator"""
        self.refresh_label.setVisible(scanning)
        if scanning:
            self.refresh_label.setText("Scanning...")

    def set_error(self, error: str):
        """Show error state"""
        self.active_window_label.setText(f"⚠️ {error}")
        self.active_window_label.setStyleSheet("color: #f85149;")
