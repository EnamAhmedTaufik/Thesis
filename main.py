import streamlit as st
import pandas as pd

# Load the CSV file
file_path = 'ComVio - ForPaperReview.csv'
papers_df = pd.read_csv(file_path)
papers_df = papers_df.dropna()
papers = papers_df.to_dict(orient='records')

st.title("Communal Violence Thesis Literature Review")
st.write("Group Members: Abdullah, Enam, Tashik, Nihal.")

# Add a banner image
st.image("https://media.wired.com/photos/63a11855a12918bc073554af/master/pass/02_Mind-your-language.jpg", use_column_width=True)
# Centered caption
st.markdown('<p style="text-align: center;">Illustration: Scott Balmer, Wired</p>', unsafe_allow_html=True)

# Search bars
search_title = st.text_input("Search papers by title")
search_year = st.selectbox("Filter papers by year", options=[None] + sorted(papers_df['Published Year'].astype(int).unique()))

# # Filtering based on search terms
filtered_papers = papers
if search_title:
    filtered_papers = [paper for paper in filtered_papers if search_title.lower() in paper["Paper"].lower()]
if search_year:
    filtered_papers = [paper for paper in filtered_papers if paper["Year"] == search_year]

# Display filtered papers
for paper in filtered_papers:
    st.header(paper["Paper Title"])
    st.subheader(paper["Dataset"].upper())
    st.markdown(f'Focus Area: <p  style="font-size:20px;">{paper["Focus Area"].upper()}</p>', unsafe_allow_html=True)
    st.markdown(f'Limitation: <p style="font-size:20px;">{paper["Limitation"].upper()}</p>', unsafe_allow_html=True)
    st.markdown(f"[Read more]({paper['Paper Drive Link']})")

# Add a footer
footer = """
    <style>
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <footer>
        <p>Made with ♥︎ by Enam</p>
    </footer>
"""

st.markdown(footer, unsafe_allow_html=True)