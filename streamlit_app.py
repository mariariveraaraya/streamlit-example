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
def quiz_app():
    st.title("Quiz App")
    for question, answers in questions.items():
        st.subheader(question)
        user_answer = st.radio("", list(answers.keys()), key=question)

    user_answers = {question: {option: st.checkbox(option, key=f"{question}_{option}") for option in answers.keys()} for question, answers in questions.items()}
    if st.button("Submit") and all(any(answers.values()) for answers in user_answers.values()):
        score = sum(all(user_answers[question][option] == correct for option, correct in answers.items()) for question, answers in questions.items())
        grade = (score / len(questions)) * 100
        st.write(f"Your grade is {grade}%")

# Run the app
if __name__ == "__main__":
    quiz_app()
