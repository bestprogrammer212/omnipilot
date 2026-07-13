"""OmniPilot Dark Theme Stylesheet"""

DARK_THEME = """
QMainWindow {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
}

/* Title bar */
QFrame#titleBar {
    background-color: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 12px 16px;
}

QLabel#appTitle {
    color: #58a6ff;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

QLabel#appSubtitle {
    color: #8b949e;
    font-size: 12px;
    font-weight: 400;
}

/* Input area */
QFrame#inputFrame {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 16px;
    margin: 8px 16px;
}

QTextEdit#promptInput {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 12px;
    font-size: 14px;
    line-height: 1.5;
    selection-background-color: #58a6ff;
}

QTextEdit#promptInput:focus {
    border: 1px solid #58a6ff;
}

QTextEdit#promptInput::placeholder {
    color: #484f58;
}

/* Buttons */
QPushButton#primaryButton {
    background-color: #238636;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 14px;
    font-weight: 600;
    min-height: 36px;
}

QPushButton#primaryButton:hover {
    background-color: #2ea043;
}

QPushButton#primaryButton:pressed {
    background-color: #1a7f37;
}

QPushButton#primaryButton:disabled {
    background-color: #30363d;
    color: #484f58;
}

QPushButton#secondaryButton {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
    min-height: 32px;
}

QPushButton#secondaryButton:hover {
    background-color: #30363d;
    border-color: #8b949e;
}

QPushButton#secondaryButton:pressed {
    background-color: #484f58;
}

QPushButton#dangerButton {
    background-color: #da3633;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}

QPushButton#dangerButton:hover {
    background-color: #f85149;
}

/* Context panel */
QFrame#contextPanel {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 16px;
    margin: 8px 16px;
}

QLabel#contextTitle {
    color: #8b949e;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

QLabel#contextItem {
    color: #c9d1d9;
    font-size: 13px;
    padding: 4px 0;
}

QLabel#contextValue {
    color: #58a6ff;
    font-size: 13px;
    font-weight: 500;
}

QLabel#contextHighlight {
    color: #7ee787;
    font-size: 13px;
    font-weight: 500;
}

/* Suggestion card */
QFrame#suggestionCard {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 16px;
    margin: 4px 16px;
}

QFrame#suggestionCard:hover {
    border-color: #58a6ff;
    background-color: #1c2128;
}

QLabel#suggestionTool {
    color: #58a6ff;
    font-size: 14px;
    font-weight: 600;
}

QLabel#suggestionAgent {
    color: #a371f7;
    font-size: 12px;
    font-weight: 500;
    background-color: #388bfd1a;
    border-radius: 4px;
    padding: 2px 8px;
}

QLabel#suggestionModel {
    color: #8b949e;
    font-size: 11px;
}

QLabel#suggestionConfidence {
    color: #7ee787;
    font-size: 12px;
    font-weight: 500;
}

QLabel#suggestionReasoning {
    color: #8b949e;
    font-size: 12px;
    line-height: 1.4;
}

/* History panel */
QFrame#historyPanel {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 16px;
    margin: 8px 16px;
}

QListWidget#historyList {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    color: #c9d1d9;
    font-size: 13px;
    padding: 8px;
    outline: none;
}

QListWidget#historyList::item {
    padding: 8px 12px;
    border-radius: 6px;
    margin: 2px 0;
}

QListWidget#historyList::item:hover {
    background-color: #21262d;
}

QListWidget#historyList::item:selected {
    background-color: #388bfd1a;
    border: 1px solid #58a6ff;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #0d1117;
    width: 8px;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background-color: #30363d;
    border-radius: 4px;
    min-height: 32px;
}

QScrollBar::handle:vertical:hover {
    background-color: #484f58;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #0d1117;
    height: 8px;
    border-radius: 4px;
}

QScrollBar::handle:horizontal {
    background-color: #30363d;
    border-radius: 4px;
    min-width: 32px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #484f58;
}

/* Status bar */
QFrame#statusBar {
    background-color: #161b22;
    border-top: 1px solid #30363d;
    padding: 8px 16px;
}

QLabel#statusLabel {
    color: #8b949e;
    font-size: 12px;
}

QLabel#statusOnline {
    color: #3fb950;
    font-size: 12px;
    font-weight: 500;
}

QLabel#statusOffline {
    color: #f85149;
    font-size: 12px;
    font-weight: 500;
}

/* Progress indicator */
QProgressBar {
    border: none;
    border-radius: 4px;
    background-color: #21262d;
    height: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #58a6ff;
    border-radius: 4px;
}

/* Tooltips */
QToolTip {
    background-color: #161b22;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 12px;
}

/* Menu */
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
    font-size: 13px;
}

QMenu::item:hover {
    background-color: #21262d;
}

QMenu::separator {
    height: 1px;
    background-color: #30363d;
    margin: 8px 0;
}

/* Dialog */
QDialog {
    background-color: #0d1117;
    color: #c9d1d9;
}

QLineEdit {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 13px;
}

QLineEdit:focus {
    border: 1px solid #58a6ff;
}

QComboBox {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 13px;
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    selection-background-color: #388bfd1a;
}
"""

LIGHT_THEME = """
/* Light theme - inverted colors */
QMainWindow {
    background-color: #ffffff;
    color: #24292f;
    font-family: 'Segoe UI', 'SF Pro Display', -apple-system, sans-serif;
}

QFrame#titleBar {
    background-color: #f6f8fa;
    border-bottom: 1px solid #d0d7de;
}

QLabel#appTitle {
    color: #0969da;
}

/* ... (rest follows same pattern with light colors) ... */
"""

def get_theme(theme_name: str = "dark") -> str:
    """Get theme stylesheet"""
    if theme_name == "dark":
        return DARK_THEME
    elif theme_name == "light":
        return LIGHT_THEME
    else:
        return DARK_THEME
