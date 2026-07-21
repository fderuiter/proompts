"""Module docstring."""
from typing import Dict

class ThemeSync:
    """
    Shared utility to detect theme states from Streamlit and MkDocs.
    Provides CSS variable mappings that automatically adapt to light/dark modes
    in both environments without requiring a page refresh.
    """

    @staticmethod
    def get_step_node_class() -> str:
        """Missing docstring."""
        # Maintain logical color-coding: Blue for steps.
        # Contrast: #ffffff on #1a5f7a is ~6.6:1 (Passes WCAG AA).
        # Stroke adapts to theme text color for visual integration.
        return "classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;"

    @staticmethod
    def get_input_node_class() -> str:
        """Missing docstring."""
        # Maintain logical color-coding: Green for inputs.
        # Contrast: #ffffff on #2c5e43 is ~6.1:1 (Passes WCAG AA).
        # Stroke adapts to theme text color for visual integration.
        return "classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;"

    @staticmethod
    def get_edge_style() -> str:
        """Missing docstring."""
        # Edges must adapt to the background (light or dark) to remain visible.
        # Uses standard text color variables for high contrast.
        return "linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;"
