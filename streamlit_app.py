import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome
"""

# Define the questions and answers
questions = {
"1. How do you access the Quest platform?": {
    "a) portal.azure.com": True,
    "b) portal.quest.com": False,
    "c) portal.synapse.com": False,
    "d) portal.access.quest": False
},
    "2. How is access organized in the platform?": {
        "a) By resource groups": True,
        "b) By permission levels": False,
        "c) By user roles": False,
        "d) By data types": False
    }
}
# Create the quiz app
def quiz_app():
    st.title("Quiz App")
    if "score" not in st.session_state:
        st.session_state.score = 0
    for i, (question, answers) in enumerate(questions.items()):
        st.subheader(question)
        user_answer = st.radio("", list(answers.keys()), key=f"question_{i}")
        if st.button("Submit", key=f"button_{i}"):
            if answers[user_answer]:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error("Incorrect. Try again.")
    grade = (st.session_state.score / len(questions)) * 100
    st.write(f"Your grade is {grade}%")

# Run the app
if __name__ == "__main__":
    quiz_app()
