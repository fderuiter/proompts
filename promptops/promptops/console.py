import os
import sys

class SemanticConsole:
    def __init__(self):
        # Environment sensitivity
        self.is_ci = os.environ.get('CI') == 'true'
        self.is_tty = sys.stdout.isatty()
        self.simplified = self.is_ci or not self.is_tty

        self.emoji_map = {
            "✅": "[SUCCESS]",
            "❌": "[ERROR]",
            "⚠️": "[WARNING]",
            "ℹ️": "[INFO]",
            "📝": "[EDIT]",
            "▶️": "[RUN]",
            "☁️": "[CLOUD]",
            "🔄": "[SYNC]",
        }

    def format_text(self, text: str) -> str:
        for emoji, semantic in self.emoji_map.items():
            if emoji in text:
                if self.simplified:
                    text = text.replace(emoji, semantic)
                else:
                    text = text.replace(emoji, f"{semantic} {emoji}")
        return text

    def section(self, label: str):
        label = self.format_text(label)
        if self.simplified:
            print(f"Section: {label}")
        else:
            print(f"Section: {label}")
            print("\u2500" * 40)

    def print(self, text: str, **kwargs):
        print(self.format_text(str(text)), **kwargs)

console = SemanticConsole()
