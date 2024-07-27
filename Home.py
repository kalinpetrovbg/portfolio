import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.jpg", width=500)

with col2:
    st.title("Kalin Petrov")
    content = """
    I'm just a regular Python developer.
    """
    st.info(content)

main_content = """
Below you can find some of the apps I have build in Python.
"""
st.write(main_content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.scv", sep=";")
with col3:
    for index, row in df.iterrows():
        if row["id"] % 2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.write("images/" + row['image'])
            st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df.iterrows():
        if row["id"] % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.write("images/" + row['image'])
            st.write(f"[Source Code]({row['url']})")
