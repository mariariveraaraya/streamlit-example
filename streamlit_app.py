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
    correct_answers = 0
    for question, answers in questions.items():
        st.subheader(question)
        user_answer = st.radio("", list(answers.keys()))
        if st.button("Submit"):
            if answers[user_answer]:
                st.success("Correct!")
                correct_answers += 1
            else:
                st.error("Incorrect. Try again.")
    if st.button("Calculate Grade"):
        grade = (correct_answers / len(questions)) * 100
        st.write(f"Your grade is {grade}%")

# Run the app
if __name__ == "__main__":
    quiz_app()
