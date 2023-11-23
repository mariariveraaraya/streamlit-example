# Import the necessary library
import streamlit as st

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
    },
    "3. Why would you access Synapse using Azure Data Studio instead of the browser?": {
        "a) Azure Data Studio provides a rich SQL editor with syntax highlighting and IntelliSense": True,
        "b) Azure Data Studio allows you to manage your data and your code in the same environment": True,
        "c) Azure Data Studio supports the use of notebooks, which can contain live code, visualizations, and narrative text": True,
        "d) Azure Data Studio requires less internet bandwidth than the browser": False
    }
}

# Create the quiz app
def quiz_app():
    st.title("Quiz App")
    if "score" not in st.session_state:
        st.session_state.score = 0
    user_answers = {}
    for i, (question, answers) in enumerate(questions.items()):
        st.subheader(question)
        user_answers[question] = {option: st.checkbox(option, key=f"{i}_{option}") for option in answers.keys()}
    if all(any(answers.values()) for answers in user_answers.values()) and st.button("Submit"):
        for question, answers in user_answers.items():
            correct = all(answers[option] == questions[question][option] for option in answers.keys())
            if correct:
                st.session_state.score += 1
        grade = (st.session_state.score / len(questions)) * 100
        st.write(f"Your grade is {grade}%")

# Run the app
if __name__ == "__main__":
    quiz_app()
