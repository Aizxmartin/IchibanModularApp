
import streamlit as st
import pandas as pd

st.title("📏 Module 4: Comp Filtering by Above Grade SF")

uploaded = st.file_uploader("Upload cleaned comp file (CSV)", type=["csv"])
subject_ag_sf = st.number_input("Enter Subject Above Grade Finished SF", min_value=0)

if uploaded and subject_ag_sf > 0:
    df = pd.read_csv(uploaded)
    if "ag_sf" not in df.columns or "net_price" not in df.columns:
        st.error("CSV must include 'ag_sf' and 'net_price' fields.")
    else:
        lower = 0.85 * subject_ag_sf
        upper = 1.10 * subject_ag_sf
        filtered = df[(df["ag_sf"] >= lower) & (df["ag_sf"] <= upper)].copy()
        filtered.sort_values(by="net_price", inplace=True)

        st.success(f"{len(filtered)} comps retained within 85–110% range.")
        st.dataframe(filtered)

        filtered.to_csv("filtered_comps.csv", index=False)
        st.download_button("Download Filtered Comps CSV", data=filtered.to_csv(index=False), file_name="filtered_comps.csv")
