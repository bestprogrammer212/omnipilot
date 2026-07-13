"""Main window for OmniPilot - the central orchestrator UI"""
import sys
import os
import threading
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QSystemTrayIcon, QMenu, QApplication,
    QMessageBox, QSplitter, QFrame, QScrollArea, QStatusBar
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt6.QtGui import QIcon, QAction, QFont, QKeySequence, QShortcut

from .style import get_theme
from .input_widget import PromptInputWidget
from .context_panel import ContextPanel
from .suggestion_card import SuggestionCard
from .history_view import HistoryView

from ..core.context_scanner import ContextScanner
from ..core.llm_classifier import LLMClassifier, ClassificationResult
from ..core.tool_launcher import ToolLauncher, LaunchConfig
from ..core.three_d_handler import ThreeDHandler
from ..core.history_manager import HistoryManager, ActionRecord

class ContextScanThread(QThread):
    """Background thread for scanning desktop context"""
    context_ready = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, scanner: ContextScanner):
        super().__init__()
        self.scanner = scanner
        self.running = True

    def run(self):
        try:
            context = self.scanner.get_full_context()
            self.context_ready.emit(context)
        except Exception as e:
            self.error.emit(str(e))

    def stop(self):
        self.running = False

class ClassificationThread(QThread):
    """Background thread for LLM classification"""
    classification_ready = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, classifier: LLMClassifier, prompt: str, context: dict):
        super().__init__()
        self.classifier = classifier
        self.prompt = prompt
        self.context = context

    def run(self):
        try:
            result = self.classifier.classify(self.prompt, self.context)
            self.classification_ready.emit(result)
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    """Main application window for OmniPilot"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("OmniPilot 🤖")
        self.setMinimumSize(900, 700)

        # Initialize components
        self.context_scanner = ContextScanner()
        self.llm_classifier = LLMClassifier(model="phi4")
        self.tool_launcher = ToolLauncher()
        self.three_d_handler = ThreeDHandler()
        self.history_manager = HistoryManager()

        self.current_context = {}
        self.current_classification = None

        # Setup UI
        self._setup_ui()
        self._setup_tray()
        self._setup_shortcuts()
        self._apply_theme()

        # Start context scanning
        self._start_context_scan()

        # Periodic context refresh
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self._start_context_scan)
        self.refresh_timer.start(5000)  # Every 5 seconds

    def _setup_ui(self):
        """Setup main UI layout"""
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Title bar
        title_bar = self._create_title_bar()
        main_layout.addWidget(title_bar)

        # Main content area with splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left panel: Context + History
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(16)
        left_layout.setContentsMargins(16, 16, 8, 16)

        # Context panel
        self.context_panel = ContextPanel()
        left_layout.addWidget(self.context_panel)

        # History view
        self.history_view = HistoryView()
        self.history_view.action_selected.connect(self._on_history_selected)
        self.history_view.feedback_given.connect(self._on_feedback)
        left_layout.addWidget(self.history_view)

        # Load history
        recent = self.history_manager.get_recent_history(20)
        self.history_view.set_history([{
            "timestamp": r.timestamp,
            "user_prompt": r.user_prompt,
            "tool": r.tool,
            "agent": r.agent,
            "model": r.model,
            "confidence": r.confidence,
            "reasoning": r.reasoning
        } for r in recent])

        left_layout.addStretch()
        splitter.addWidget(left_panel)

        # Right panel: Input + Suggestion
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(16)
        right_layout.setContentsMargins(8, 16, 16, 16)

        # Input widget
        self.input_widget = PromptInputWidget()
        self.input_widget.submit_prompt.connect(self._on_submit)
        self.input_widget.analyze_requested.connect(self._on_analyze)
        right_layout.addWidget(self.input_widget)

        # Suggestion card
        self.suggestion_card = SuggestionCard()
        self.suggestion_card.launch_requested.connect(self._on_launch)
        right_layout.addWidget(self.suggestion_card)

        # 3D workflow info (hidden by default)
        self.three_d_info = self._create_3d_info()
        self.three_d_info.setVisible(False)
        right_layout.addWidget(self.three_d_info)

        right_layout.addStretch()
        splitter.addWidget(right_panel)

        # Set splitter sizes (40% left, 60% right)
        splitter.setSizes([360, 540])
        main_layout.addWidget(splitter)

        # Status bar
        self.status_bar = QStatusBar()
        self.status_bar.setObjectName("statusBar")
        self.setStatusBar(self.status_bar)

        self.status_ollama = QLabel("⚪ Ollama")
        self.status_bar.addWidget(self.status_ollama)

        self.status_memory = QLabel("💾 RAM: —")
        self.status_bar.addWidget(self.status_memory)

        self.status_active = QLabel("🔴 Idle")
        self.status_bar.addWidget(self.status_active)

        # Check Ollama status periodically
        self.ollama_timer = QTimer()
        self.ollama_timer.timeout.connect(self._check_ollama)
        self.ollama_timer.start(3000)
        self._check_ollama()

    def _create_title_bar(self) -> QFrame:
        """Create title bar with app info"""
        frame = QFrame()
        frame.setObjectName("titleBar")

        layout = QHBoxLayout(frame)
        layout.setSpacing(12)
        layout.setContentsMargins(16, 12, 16, 12)

        # App icon/title
        title_layout = QVBoxLayout()
        title_layout.setSpacing(2)

        title = QLabel("🤖 OmniPilot")
        title.setObjectName("appTitle")
        title_layout.addWidget(title)

        subtitle = QLabel("AI Tool Orchestrator for HP OmniBook X Flip")
        subtitle.setObjectName("appSubtitle")
        title_layout.addWidget(subtitle)

        layout.addLayout(title_layout)
        layout.addStretch()

        # Top buttons
        self.settings_btn = QPushButton("⚙️")
        self.settings_btn.setObjectName("secondaryButton")
        self.settings_btn.setFixedSize(36, 36)
        self.settings_btn.setToolTip("Settings")
        layout.addWidget(self.settings_btn)

        self.minimize_btn = QPushButton("🗕️")
        self.minimize_btn.setObjectName("secondaryButton")
        self.minimize_btn.setFixedSize(36, 36)
        self.minimize_btn.setToolTip("Minimize to tray")
        self.minimize_btn.clicked.connect(self.hide)
        layout.addWidget(self.minimize_btn)

        return frame

    def _create_3d_info(self) -> QFrame:
        """Create 3D generation info panel"""
        frame = QFrame()
        frame.setObjectName("contextPanel")

        layout = QVBoxLayout(frame)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 16, 16, 16)

        title = QLabel("🎨 3D Generation Workflow")
        title.setObjectName("contextTitle")
        layout.addWidget(title)

        steps = QLabel(
            "1. Upload photo or enter prompt\n"
            "2. Select model (TripoSR = fast, Stable Fast 3D = quality)\n"
            "3. Generate 3D model\n"
            "4. Export as STL for 3D printing\n"
            "5. Import to Cura/PrusaSlicer\n"
            "6. Slice for Elegoo Neptune 4 Pro\n"
            "7. Print!"
        )
        steps.setObjectName("suggestionReasoning")
        layout.addWidget(steps)

        self.three_d_export_btn = QPushButton("📁 Open AI 3D Generator Pro")
        self.three_d_export_btn.setObjectName("primaryButton")
        self.three_d_export_btn.clicked.connect(self._open_3d_app)
        layout.addWidget(self.three_d_export_btn)

        return frame

    def _setup_tray(self):
        """Setup system tray icon"""
        self.tray = QSystemTrayIcon(self)
        self.tray.setToolTip("OmniPilot - AI Orchestrator")

        # Create icon (fallback to text if no icon file)
        icon = QIcon.fromTheme("applications-system")
        if not icon.isNull():
            self.tray.setIcon(icon)

        # Tray menu
        tray_menu = QMenu()

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)

        tray_menu.addSeparator()

        quick_prompt = QAction("Quick Prompt...", self)
        quick_prompt.setShortcut("Ctrl+Shift+O")
        quick_prompt.triggered.connect(self._show_quick_prompt)
        tray_menu.addAction(quick_prompt)

        tray_menu.addSeparator()

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self._quit_app)
        tray_menu.addAction(quit_action)

        self.tray.setContextMenu(tray_menu)
        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

    def _setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        # Ctrl+Shift+O - Show app
        shortcut = QShortcut(QKeySequence("Ctrl+Shift+O"), self)
        shortcut.activated.connect(self.show)

        # Ctrl+Enter - Submit (handled in input widget)
        # Esc - Minimize to tray
        esc_shortcut = QShortcut(QKeySequence("Esc"), self)
        esc_shortcut.activated.connect(self.hide)

    def _apply_theme(self):
        """Apply dark theme stylesheet"""
        self.setStyleSheet(get_theme("dark"))

    def _start_context_scan(self):
        """Start background context scanning"""
        self.context_panel.set_scanning(True)

        self.scan_thread = ContextScanThread(self.context_scanner)
        self.scan_thread.context_ready.connect(self._on_context_ready)
        self.scan_thread.error.connect(self._on_context_error)
        self.scan_thread.start()

    def _on_context_ready(self, context: dict):
        """Handle context scan completion"""
        self.current_context = context
        self.context_panel.update_context(context)
        self.context_panel.set_scanning(False)

        # Update memory status
        sys_info = context.get("system_info", {})
        if sys_info:
            mem = sys_info.get("memory_percent", 0)
            self.status_memory.setText(f"💾 RAM: {mem:.0f}%")

    def _on_context_error(self, error: str):
        """Handle context scan error"""
        self.context_panel.set_error(error)
        self.context_panel.set_scanning(False)

    def _on_analyze(self):
        """Analyze prompt with context"""
        prompt = self.input_widget.get_prompt()
        if not prompt:
            return

        self.input_widget.set_analyzing(True)
        self.suggestion_card.set_loading(True)
        self.status_active.setText("🟡 Analyzing...")

        # Use LLM classification
        self.classify_thread = ClassificationThread(
            self.llm_classifier, prompt, self.current_context
        )
        self.classify_thread.classification_ready.connect(self._on_classification_ready)
        self.classify_thread.error.connect(self._on_classification_error)
        self.classify_thread.start()

    def _on_submit(self):
        """Handle prompt submission"""
        prompt = self.input_widget.get_prompt()
        if not prompt:
            return

        # If no classification yet, analyze first
        if not self.current_classification:
            self._on_analyze()
            return

        # Launch the suggested tool
        self._launch_tool(self.current_classification)

    def _on_classification_ready(self, result: ClassificationResult):
        """Handle classification result"""
        self.current_classification = result

        self.suggestion_card.set_suggestion(
            tool=result.tool,
            agent=result.agent,
            model=result.model,
            confidence=result.confidence,
            reasoning=result.reasoning
        )

        self.input_widget.set_analyzing(False)
        self.status_active.setText("🟢 Ready to launch")

        # Show 3D info if AI 3D Generator Pro is suggested
        self.three_d_info.setVisible(result.tool == "ai3d")

    def _on_classification_error(self, error: str):
        """Handle classification error"""
        self.suggestion_card.clear()
        self.input_widget.set_analyzing(False)
        self.status_active.setText(f"🔴 Error: {error}")

        # Fallback to keyword classification
        from ..agents.tool_registry import get_tool_for_prompt, get_agent_for_prompt
        tool = get_tool_for_prompt(self.input_widget.get_prompt())
        agent = get_agent_for_prompt(self.input_widget.get_prompt())

        model_map = {
            "hermes": "devstral:24b",
            "opencode": "qwen3:8b",
            "interpreter": "phi4",
            "ai3d": None
        }

        self.suggestion_card.set_suggestion(
            tool=tool,
            agent=agent.name if agent else None,
            model=model_map.get(tool),
            confidence=0.5,
            reasoning=f"Fallback classification (LLM error: {error})"
        )

    def _on_launch(self, tool: str, agent: str, model: str):
        """Launch the selected tool"""
        prompt = self.input_widget.get_prompt()

        self.status_active.setText(f"🟡 Launching {tool}...")

        # Create launch config
        config = LaunchConfig(
            tool=tool,
            model=model if model else None,
            agent=agent if agent else None,
            prompt=prompt
        )

        # Get project path from context
        if self.current_context.get("active_project"):
            config.working_dir = self.current_context["active_project"].get("path")

        # Launch in background thread
        launch_thread = threading.Thread(
            target=self._launch_tool_thread,
            args=(config, prompt)
        )
        launch_thread.start()

    def _launch_tool_thread(self, config: LaunchConfig, prompt: str):
        """Launch tool in background thread"""
        success = self.tool_launcher.launch(config)

        # Record in history
        record = ActionRecord(
            timestamp=time.time(),
            user_prompt=prompt,
            tool=config.tool,
            agent=config.agent,
            model=config.model or "default",
            confidence=self.current_classification.confidence if self.current_classification else 0.5,
            reasoning=self.current_classification.reasoning if self.current_classification else "Manual launch",
            success=success
        )

        self.history_manager.add_action(record)

        # Update UI
        # Note: This should be done via signal, but for simplicity:
        self.status_active.setText("🟢 Ready" if success else "🔴 Launch failed")

    def _open_3d_app(self):
        """Open AI 3D Generator Pro"""
        self.three_d_handler.launch_app()

    def _on_history_selected(self, data: dict):
        """Handle history item selection"""
        prompt = data.get("user_prompt", "")
        self.input_widget.text_input.setPlainText(prompt)

    def _on_feedback(self, timestamp: float, success: bool, feedback: str):
        """Handle user feedback"""
        self.history_manager.record_feedback(timestamp, success, feedback)

    def _check_ollama(self):
        """Check Ollama server status"""
        if self.tool_launcher.is_ollama_running():
            self.status_ollama.setText("🟢 Ollama")
        else:
            self.status_ollama.setText("🔴 Ollama")

    def _tray_activated(self, reason):
        """Handle tray icon activation"""
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()

    def _show_quick_prompt(self):
        """Show quick prompt dialog from tray"""
        self.show()
        self.input_widget.text_input.setFocus()

    def _quit_app(self):
        """Quit application"""
        self.tool_launcher.shutdown_all()
        self.tray.hide()
        QApplication.quit()

    def closeEvent(self, event):
        """Override close to minimize to tray"""
        event.ignore()
        self.hide()
        self.tray.showMessage(
            "OmniPilot",
            "Running in background. Press Ctrl+Shift+O to show.",
            QSystemTrayIcon.MessageIcon.Information,
            3000
        )
