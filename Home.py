import streamlit as st
import pandas as pd
import os
from send_email import send_email

st.set_page_config(layout="wide", page_title="Sachethan's Portfolio")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home Page
if page == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/photo.png", width=250)

    with col2:
        st.title("Sachethan")
        st.subheader("Exploring Python & Machine Learning | Always Learning")

        content = """
Hi, I’m Sachethan, a 19-year-old from Bengaluru with a strong passion for Python programming and machine learning. 
I build real-world applications that bridge the gap between theory and execution. My goal is to master the evolving 
tech landscape and contribute innovative solutions across diverse domains.
"""
        st.write(content)

    # Skills & Technologies
    st.subheader("🚀 Skills & Technologies")
    skills = ["Python", "Machine Learning", "Data Science", "Pandas", "NumPy","flask",
               "Streamlit"]
    st.write(", ".join(skills))

    # Achievements & Certifications
    st.subheader("Certifications🏆")

    certificates = {
        "Python Mega Course": "https://drive.google.com/file/d/1tIxUX_dz6qsJuCxB3Xj7bS0fZ1AmQjtZ/view?usp=sharing",
    }

    for cert, link in certificates.items():
        st.markdown(f'[📜 {cert}]({link})', unsafe_allow_html=True)

    # Featured Projects
    st.subheader("🔹 Featured Projects")

    df = pd.read_csv("data.csv", sep=";")  # Load project data

    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    with col3:
        for index, row in df[:3].iterrows():  # Display first 3 projects
            st.header(row["title"])
            st.write(row["description"])
            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index, row in df[3:6].iterrows():  # Display next 3 projects
            st.header(row["title"])
            st.write(row["description"])
            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")








# Projects Page
elif page == "Projects":
    st.title("Projects")
    df = pd.read_csv("data.csv", sep=";")
    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    with col3:
        for index, row in df[:7].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index, row in df[6:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")


#Projects Page
elif page == "Projects":
    st.title("💻 My Projects")
    st.write("Explore the projects I've worked on, covering Python, Machine Learning, and more!")

    df = pd.read_csv("data.csv", sep=";")  # Load projects from CSV

    col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

    with col1:
        for index, row in df[:len(df) // 2].iterrows():  # Display half projects in first column
            st.header(row["title"])
            st.write(row["description"])

            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            else:
                st.error(f"Image {row['image']} not found.")

            st.write(f"[🔗 Source Code]({row['url']})")

    with col2:
        for index, row in df[len(df) // 2:].iterrows():  # Display remaining projects in second column
            st.header(row["title"])
            st.write(row["description"])

            image_path = "images/" + row["image"]
            if os.path.exists(image_path):
                st.image(image_path)
            else:
                st.error(f"Image {row['image']} not found.")

            st.write(f"[🔗 Source Code]({row['url']})")



elif page == "Contact":
    st.header("Contact Me")

    with st.form(key="email_forms"):
        user_email = st.text_input("Your email address")
        raw_message = st.text_area("Your message")
        message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {raw_message}
    """
        button = st.form_submit_button("Submit")
        print(button)
        if button:
            send_email(message)
            st.info("Your email was sent successfully")


# Call-to-Action

    st.write("Let's collaborate or discuss tech!")

    col5, col6 = st.columns(2)

    with col5:
        st.write("🔗 [GitHub](https://github.com/Sachethanv)")

    with col6:
        st.write("💼 [LinkedIn](https://www.linkedin.com/in/sachethan-v-68bbb1269/)")
