"""History view widget for OmniPilot - shows recent actions"""
from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
    QListWidget, QListWidgetItem, QPushButton, 
    QSpacerItem, QSizePolicy, QMenu
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction
from datetime import datetime

class HistoryView(QFrame):
    """Displays history of past actions with feedback options"""

    action_selected = pyqtSignal(dict)  # Emits action data when clicked
    feedback_given = pyqtSignal(float, bool, str)  # timestamp, success, feedback

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("historyPanel")
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 16, 16, 16)

        # Header
        header = QHBoxLayout()

        self.title_label = QLabel("📜 History")
        self.title_label.setObjectName("contextTitle")
        header.addWidget(self.title_label)

        header.addStretch()

        self.count_label = QLabel("0 actions")
        self.count_label.setObjectName("contextValue")
        header.addWidget(self.count_label)

        layout.addLayout(header)

        # History list
        self.history_list = QListWidget()
        self.history_list.setObjectName("historyList")
        self.history_list.setMaximumHeight(200)
        self.history_list.itemClicked.connect(self._on_item_clicked)
        self.history_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.history_list.customContextMenuRequested.connect(self._show_context_menu)
        layout.addWidget(self.history_list)

        # Stats row
        stats = QHBoxLayout()

        self.success_label = QLabel("✅ 0")
        self.success_label.setObjectName("contextHighlight")
        self.success_label.setToolTip("Successful actions")
        stats.addWidget(self.success_label)

        self.fail_label = QLabel("❌ 0")
        self.fail_label.setObjectName("contextHighlight")
        self.fail_label.setStyleSheet("color: #f85149;")
        self.fail_label.setToolTip("Failed actions")
        stats.addWidget(self.fail_label)

        stats.addStretch()

        self.clear_btn = QPushButton("🗑️ Clear")
        self.clear_btn.setObjectName("dangerButton")
        self.clear_btn.clicked.connect(self._on_clear)
        stats.addWidget(self.clear_btn)

        layout.addLayout(stats)

    def add_action(self, action_data: dict):
        """Add a new action to history"""
        timestamp = action_data.get("timestamp", 0)
        tool = action_data.get("tool", "unknown")
        agent = action_data.get("agent")
        prompt = action_data.get("user_prompt", "No prompt")
        confidence = action_data.get("confidence", 0)

        # Format time
        dt = datetime.fromtimestamp(timestamp)
        time_str = dt.strftime("%H:%M")

        # Format text
        tool_emoji = {
            "opencode": "💻",
            "hermes": "🧠",
            "interpreter": "🖥️",
            "ai3d": "🎨"
        }.get(tool, "❓")

        agent_str = f" ({agent})" if agent else ""
        text = f"{tool_emoji} [{time_str}] {tool}{agent_str}: {prompt[:50]}..."

        # Create item
        item = QListWidgetItem(text)
        item.setData(Qt.ItemDataRole.UserRole, action_data)

        # Color based on confidence
        if confidence > 0.8:
            item.setForeground(Qt.GlobalColor.green)
        elif confidence < 0.5:
            item.setForeground(Qt.GlobalColor.yellow)

        self.history_list.insertItem(0, item)

        # Update count
        self.count_label.setText(f"{self.history_list.count()} actions")

    def update_feedback(self, timestamp: float, success: bool):
        """Update item appearance based on feedback"""
        for i in range(self.history_list.count()):
            item = self.history_list.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if data and data.get("timestamp") == timestamp:
                emoji = "✅" if success else "❌"
                text = item.text()
                # Add emoji prefix if not present
                if not text.startswith(("✅", "❌")):
                    item.setText(f"{emoji} {text}")
                break

        self._update_stats()

    def _update_stats(self):
        """Update success/fail counters"""
        success = 0
        fail = 0

        for i in range(self.history_list.count()):
            text = self.history_list.item(i).text()
            if text.startswith("✅"):
                success += 1
            elif text.startswith("❌"):
                fail += 1

        self.success_label.setText(f"✅ {success}")
        self.fail_label.setText(f"❌ {fail}")

    def _on_item_clicked(self, item: QListWidgetItem):
        """Emit action data when item clicked"""
        data = item.data(Qt.ItemDataRole.UserRole)
        if data:
            self.action_selected.emit(data)

    def _show_context_menu(self, position):
        """Show context menu for history item"""
        item = self.history_list.itemAt(position)
        if not item:
            return

        data = item.data(Qt.ItemDataRole.UserRole)
        if not data:
            return

        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 8px;
            }
            QMenu::item {
                color: #c9d1d9;
                padding: 8px 24px;
                border-radius: 6px;
            }
            QMenu::item:hover {
                background-color: #21262d;
            }
        """)

        # Success action
        success_action = QAction("✅ Mark Success", self)
        success_action.triggered.connect(lambda: self._give_feedback(data, True))
        menu.addAction(success_action)

        # Fail action
        fail_action = QAction("❌ Mark Failed", self)
        fail_action.triggered.connect(lambda: self._give_feedback(data, False))
        menu.addAction(fail_action)

        menu.addSeparator()

        # Copy prompt
        copy_action = QAction("📋 Copy Prompt", self)
        copy_action.triggered.connect(lambda: self._copy_prompt(data))
        menu.addAction(copy_action)

        # Relaunch
        relaunch_action = QAction("🚀 Relaunch", self)
        relaunch_action.triggered.connect(lambda: self._relaunch(data))
        menu.addAction(relaunch_action)

        menu.exec(self.history_list.mapToGlobal(position))

    def _give_feedback(self, data: dict, success: bool):
        """Give feedback for an action"""
        timestamp = data.get("timestamp", 0)
        self.feedback_given.emit(timestamp, success, "")
        self.update_feedback(timestamp, success)

    def _copy_prompt(self, data: dict):
        """Copy prompt to clipboard"""
        prompt = data.get("user_prompt", "")
        from PyQt6.QtWidgets import QApplication
        clipboard = QApplication.clipboard()
        clipboard.setText(prompt)

    def _relaunch(self, data: dict):
        """Relaunch the same action"""
        # TODO: Implement relaunch logic
        pass

    def _on_clear(self):
        """Clear all history"""
        self.history_list.clear()
        self.count_label.setText("0 actions")
        self.success_label.setText("✅ 0")
        self.fail_label.setText("❌ 0")

    def set_history(self, actions: list):
        """Load history from list of action records"""
        self.history_list.clear()
        for action in reversed(actions):  # Newest first
            self.add_action(action)
        self._update_stats()
