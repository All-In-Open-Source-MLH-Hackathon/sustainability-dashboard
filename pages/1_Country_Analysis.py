import pandas as pd
import streamlit as st
import plotly.express as px

selected_insurer = st.sidebar.selectbox("Select Country", ["Kenya"])

st.title(f"Kenya Analysis - {selected_insurer}")

selected_year = st.sidebar.selectbox("Select year", [2023, 2022, 2021, 2020, 2019])

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Rank",
        "1",
        delta=None,
        delta_color="normal",
        help=None,
        label_visibility="visible",
    )

with col2:
    st.metric(
        "Sustainability Index",
        "98%",
        delta=None,
        delta_color="normal",
        help=None,
        label_visibility="visible",
    )


co1, col2 = st.columns(2)

gpis = [
    {"total": 1000000, "category": "Forest"},
    {"total": 2000000, "category": "Shrubs"},
    {"total": 600000, "category": "Water"},
    {"total": 21200, "category": "Urban areas"},
]
gpis_df = pd.DataFrame(gpis)

st.title(f"Land Coverage Analysis")

fig = px.pie(
    gpis_df,
    values="total",
    names="category",
)

st.plotly_chart(fig, use_container_width=True)


