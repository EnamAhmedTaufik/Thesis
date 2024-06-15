#Literature review papers from my undergraduate thesis
<p align="center">
    <img src="https://media.wired.com/photos/63a11855a12918bc073554af/master/pass/02_Mind-your-language.jpg" alt="Illustration: Scott Balmer, Wired" width="600"/>
</p>

This project showcases the literature review papers from my undergraduate thesis using a simple web app built with Streamlit.

[View demo](https://communalviolence.streamlit.app/)

## Files Included
- `papers.csv`: A CSV file containing the details of the foundational papers, including title, authors, summary, link, year of publication, dataset, method, and limitation.
- `papers.py`: The Streamlit application code to display and search through the papers.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EnamAhmedTaufik/Thesis.git
   cd thesis

2. **Install the required dependencies:**:
   Ensure you have Python installed. It's recommended to use a virtual environment.
   ```bash
   pip install streamlit pandas
   
3. **Run the Streamlit app:**:
   ```bash
   streamlit run papers.py

4. View the app:
   The app will open in your default web browser.
   
## Customizing for Your Own Domain Topics

You can use this code to create a similar web app for papers in your own domain topics by updating the papers.csv file.

1. Update the CSV file:
Replace the content of papers.csv with your own data. Ensure the CSV file includes the following columns: Paper, Authors, Summary, Link, and Year.

2. Run the app:
After updating the CSV file, run the Streamlit app again using the command:
   ```bash
   streamlit run papers.py

