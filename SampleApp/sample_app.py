import streamlit as st
from st_circular_progress import CircularProgress
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
st.subheader("Sizes")
sizes_columns = st.columns(4)
with sizes_columns[0]:
    small = CircularProgress(
        value=50,
        label="Small Variation",
        size="small",
        key="small_cp",
    ).st_circular_progress()
with sizes_columns[1]:
    small = CircularProgress(
        value=50,
        label="Medium Variation",
        size="medium",
        key="medium_cp",
    ).st_circular_progress()
with sizes_columns[2]:
    small = CircularProgress(
        value=50,
        label="Large Variation",
        size="large",
        key="large_cp",
    ).st_circular_progress()
with sizes_columns[3]:
    small = CircularProgress(
        value=50,
        label="Color Variations",
        size="large",
        key="colored_cp",
        color="#F63366",
        track_color="#F0F2F6",
    ).st_circular_progress()
