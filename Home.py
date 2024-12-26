import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sachethan")
    content = """
     Hi, I’m Sachethan, an 18-year-old from Bengaluru with a strong passion for Python programming and machine learning. I have hands-on experience with a variety of projects, ranging from predictive models to automation solutions. While I continuously strive to expand my knowledge and tackle new challenges, I also focus on building practical, real-world applications that bridge the gap between theory and execution. I’m committed to mastering the ever-evolving tech landscape and look forward to contributing innovative solutions across diverse domains.
    """
    st.info(content)

content2 = """
Below You can find some of the apps I have built in Python:
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        
        image_path = "images/" + row["image"]
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.error(f"Image {row['image']} not found.")
        
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        
        image_path = "images/" + row["image"]
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.error(f"Image {row['image']} not found.")
        
        st.write(f"[Source Code]({row['url']})")
