# Streamlit Circular Progress Component
> Author: Carlos D. Serrano

## Installation and Usage Sample:

### Install using PIP
```
pip install st-circular-progress
```
## Updating Values
This widget uses session states and there are two ways of refreshing its state:
- Use a callback function on your widget causing the change (not the circular progress)
- Use Re-Run to reload
### Sample Code

```python

import streamlit as st
from st_circular_progress import CircularProgress

st.title("Circular Progress Component")


def calculate_progress() -> int:
    return (
        abs(10 * sum([v for k, v in st.session_state.items() if "check" in k.lower()]))
        + 10
    )

columns = st.columns(2)

with columns[0]:
    cp = CircularProgress(
        value=0,
        label="Rules acknowledgement",
        size="Large",
        key="circular_progress_total",
    )
    cp.st_circular_progress()
with columns[1]:
    for i in range(10):
        st.checkbox(
            f"Acknowledge Rule {i}",
            key=f"check{i}",
            on_change=cp.update_value,
            args=[calculate_progress()],
        )

```

## Sample App 
[Click Here for a sample app](https://st-circular-progress-demo.streamlit.app)