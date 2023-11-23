import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome
"""
# Import the necessary library
import streamlit as st

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
    score = 0
    for i, (question, answers) in enumerate(questions.items()):
        st.subheader(question)
        user_answer = st.radio("", list(answers.keys()), key=f"question_{i}")
        if st.button("Submit", key=f"button_{i}"):
            if answers[user_answer]:
                st.success("Correct!")
                score += 1
            else:
                st.error("Incorrect. Try again.")
    grade = (score / len(questions)) * 100
    st.write(f"Your grade is {grade}%")
    if grade >= 80:
        st.write("Congratulations, you passed!")
    else:
        st.write("Sorry, you did not pass.")

# Run the app
if __name__ == "__main__":
    quiz_app()
