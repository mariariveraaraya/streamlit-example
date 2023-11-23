import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome
"""

# Define the questions and answers
questions = {
"1. How do you access the QESD platform?": {
    "a) portal.azure.com": True,
    "b) portal.quest.com": False,
    "c) portal.synapse.com": False,
    "d) portal.access.quest": False
},
    "2. How is access organized in the platform?": {
        "a) By resource groups": True,
        "b) By permission levels": True,
        "c) By user roles": False,
        "d) By data types": False
    }
}
# Create the quiz app
# Create the quiz app
def quiz_app():
    st.title("Quiz App")
    user_answers = {}
    for i, (question, answers) in enumerate(questions.items()):
        st.subheader(question)
        user_answers[question] = st.radio("", list(answers.keys()), key=f"question_{i}")
    if None not in user_answers.values():
        if st.button("Submit"):
            score = sum(questions[question][answer] for question, answer in user_answers.items())
            if score == len(questions):
                st.success("All answers are correct!")
            else:
                st.error(f"You got {score} out of {len(questions)} correct.")

# Run the app
if __name__ == "__main__":
    quiz_app()
