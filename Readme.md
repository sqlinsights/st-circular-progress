# Streamlit Circular Progress Component
> Author: Carlos D. Serrano

## Installation and Usage Sample:

### Install using PIP
```
pip install st-circular-progress
```
## Creating an instance
Each circular slider must be initialized by calling the CircularProgress class, which requires the following attributes:
- Label
- Value
- Key
- size [optional] defaults to "medium"
- track_color [optional] defaults to "lightgray"
- color [optional] defaults to "blue"

**Example**
```python
my_circular_progress = CircularProgress(
    label="Sample Bar",
    value=55,
    key="my_circular_progress").st_circular_progress()
```
or 

```python
my_circular_progress = CircularProgress(
    label="Sample Bar",
    value=55,
    key="my_circular_progress")

my_circular_progress.st_circular_progress()
```

## Updating Values
This widget uses session states and there are two ways of refreshing its state:
- Use a callback function on your widget causing the change (not the circular progress)
- Use Re-Run to reload

An `update_value()` function has been provided to facilitate updating the value of a pre-defined `CircularProgress`

**Example**
```python
my_circular_progress.update_values(progress=100)
```
### Sample Code

```python

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


```

## Sample App 
[Click Here for a sample app](https://st-circular-progress-demo.streamlit.app)

