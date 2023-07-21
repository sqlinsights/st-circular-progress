import os
import streamlit.components.v1 as components
import streamlit as st

_RELEASE = True


if not _RELEASE:
    _st_circular_progress_component = components.declare_component(
        "st_circular_progress",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_circular_progress_component = components.declare_component(
        "st_circular_progress", path=build_dir
    )


class CircularProgressBarError(Exception):
    pass


class CircularProgress:
    """
    - Use a callback function to update the value.
    - Keep label under 50 characters
    - Size must be small, medium or large
    - Colors can be hex codes or human friendly
    - Value must be between 0 and 100
    """

    def __init__(
        self,
        label: str,
        value: int = None,
        size: str = "medium",
        track_color: str = "lightgray",
        color: str = "blue",
        key: str = None,
    ):
        self.value = value
        self.size = size.lower()
        self.label = label
        self.track_color = track_color
        self.color = color
        self.key = key or label

    def st_circular_progress(self):
        if f"cp_{self.key}" not in st.session_state:
            st.session_state[f"cp_{self.key}"] = self.value
        if self.size not in ["small", "medium", "large"]:
            raise CircularProgressBarError("Size must be small, medium or large")
        if len(self.label) > 50:
            raise CircularProgressBarError("Label can't be longer than 50 characters")
        if self.value < 0 or self.value > 100:
            raise CircularProgressBarError("Value must be between 0 and 100")
        component_value = _st_circular_progress_component(
            label=self.label,
            value=st.session_state[f"cp_{self.key}"],
            size=self.size,
            color=self.color,
            track_color=self.track_color,
            key=self.key,
        )
        return component_value

    def update_value(self, progress):
        st.session_state[f"cp_{self.key}"] = progress
