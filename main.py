import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from utils import clean_text
from portfolio import Portfolio


def create_streamlit_app(llm, portfolio, clean_text):
    st.title('📧 Cold Email Generator')
    url_input = st.text_input('Enter a URL for a job posting:')
    submit_button = st.button('Generate cold email...')

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)
            portfolio.load_portfolio()

            for job in jobs:
                skills = job.get('skills', [])
                print(skills)
                des = portfolio.query_descriptions(skills)
                email = llm.write_mail(job, des)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)