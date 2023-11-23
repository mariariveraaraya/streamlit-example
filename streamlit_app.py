import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Define the questions and answers
questions = {
    "What is 2 + 2?": {
        "1": False,
        "2": False,
        "3": False,
        "4": True
    },
    "What is 3 * 3?": {
        "6": False,
        "9": True,
        "12": False,
        "15": False
    }
}

# Create the quiz app
def quiz_app():
    st.title("Quiz App")
    for question, answers in questions.items():
        st.subheader(question)
        user_answer = st.radio("", list(answers.keys()))
        if st.button("Submit"):
            if answers[user_answer]:
                st.success("Correct!")
            else:
                st.error("Incorrect. Try again.")
