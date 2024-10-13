import streamlit as st

st.set_page_config(layout= "wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sachethan")
    content = """
    Hi, I’m Sachethan, an 18-year-old from Bengaluru, studying at Global Academy of Technology. I have a passion for Python programming and aim to become a top machine learning engineer. I've already worked on a few exciting machine learning and deep learning projects, and I’m eager to take my skills to the next level and build innovative solutions.
    """
    st.info(content)



content2 = """
Below You can find some of the apps i have built in python
"""

st.write(content2)

