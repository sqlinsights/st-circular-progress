import os
import streamlit.components.v1 as components
from streamlit import session_state as _ss

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
        if f"cp_{self.key}" not in _ss:
            _ss[f"cp_{self.key}"] = self.value
        if self.size not in ["small", "medium", "large"]:
            raise CircularProgressBarError("Size must be small, medium or large")
        if len(self.label) > 50:
            raise CircularProgressBarError("Label can't be longer than 50 characters")
        if self.value < 0 or self.value > 100:
            raise CircularProgressBarError("Value must be between 0 and 100")
        component_value = _st_circular_progress_component(
            label=self.label,
            value=_ss[f"cp_{self.key}"],
            size=self.size,
            color=self.color,
            track_color=self.track_color,
            key=self.key,
        )
        return component_value

    def update_value(self, progress):
        _ss[f"cp_{self.key}"] = progress


if not _RELEASE:
    import streamlit as st
    import pandas as pd
    import numpy as np

    st.title("Circular Progress Component")

    def calculate_progress():
        if "slider" in st.session_state:
            cp.update_value(progress=st.session_state["slider"])

    columns = st.columns((1, 2))

    with columns[0]:
        cp = CircularProgress(
            value=0,
            label="Progress Indicator",
            size="Large",
            key="circular_progress_total",
        )
        cp.st_circular_progress()
    with columns[1]:
        st.slider(
            "Change progress to",
            min_value=0,
            max_value=100,
            on_change=calculate_progress,
            key="slider",
        )

    data = [
        ["Feature #126", 55],
        ["Feature #95", 100],
        ["Feature #134", 24],
        ["Feature #77", 98],
        ["Feature #98", 32],
    ]
    project_data = pd.DataFrame(data=data, columns=["Project Name", "Completion"])
    project_data["color"] = project_data.apply(
        lambda x: "red"
        if x["Completion"] < 25
        else "orange"
        if x["Completion"] < 75
        else "green",
        axis=1,
    )

    widgets = {}
    dashboard = st.columns(5)
    for k, v in project_data.iterrows():
        with dashboard[k]:
            widgets[k] = CircularProgress(
                value=v["Completion"],
                label=v["Project Name"],
                size="Medium",
                key=f"dsh_{k}",
                color=v["color"],
            ).st_circular_progress()
