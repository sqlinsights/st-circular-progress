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
