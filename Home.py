import streamlit as st #Streamlit is used to create the web interface.
import pandas as pd


st.set_page_config(layout= "wide")#This sets the layout of the page to be "wide", allowing more space for columns and content to be displayed side by side.

col1, col2 = st.columns(2)#This function creates two equal-width columns, col1 and col2, for placing content side by side.


#with col1: This ensures that the content inside this block is placed in the left column (col1).
#st.image("images/photo.png"): This loads and displays an image (e.g., your profile photo) from the specified path
#(images/photo.png).


with col1:
    st.image("images/photo.png")



#with col2: Content in this block is placed in the right column (col2).
#st.title("Sachethan"): Displays the title "Sachethan".
#content: A multi-line string that contains the introductory profile content about you.
#st.info(content): Displays the content text in an info box (styled for emphasis).




with col2:
    st.title("Sachethan")
    content = """
    Hi, I’m Sachethan, an 18-year-old from Bengaluru, studying at Global Academy of Technology. I have a passion for Python programming and aim to become a top machine learning engineer. I've already worked on a few exciting machine learning and deep learning projects, and I’m eager to take my skills to the next level and build innovative solutions.
    """
    st.info(content)


content2 = """
Below You can find some of the apps I have built in Python:
"""

st.write(content2)



#st.columns([1.5, 0.5, 1.5]): Creates three columns:
#col3 and col4 are wider (1.5 units each) for displaying app details.
#empty_col is a narrow empty column (0.5 units wide) to create space between the two columns.



col3,empty_col ,  col4 = st.columns([1.5, 0.5 , 1.5])
df = pd.read_csv("data.csv", sep=";")
#Reads a CSV file (data.csv) that contains details about your Python apps.
#The sep=";" indicates that the values are separated by semicolons.


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])  # Access the title as a column in the DataFrame
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])  # Access the title as a column in the DataFrame
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

#for index, row in df[:10].iterrows(): Iterates over the first 10 rows of the DataFrame (df) to display details
# of the first 10 apps.

#st.header(row["title"]): Displays the app's title from the DataFrame column title.

#st.write(row["description"]): Displays the app's description from the DataFrame column description.

#st.image("images/" + row["image"]): Displays an image related to the app, stored in the image column of the DataFrame.
# It appends the image name from the CSV file to the "images/" folder path.

#st.write(f"[Source Code]({row['url']})"): Displays a clickable link to the app’s source code by
# fetching the URL from the url column in the CSV file.