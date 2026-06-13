import streamlit as st
import time

# Question Bank (Insert your questions here)
questions = [
    {
        "q": "Let f(x) be continuous on [a, c] and differentiable in (a, c)...",
        "options": ["k > (c-a)f(b)", "k < (c-a)f(b)", "k = (c-a)f(b)", "k < 2(c-a)f(b)"],
        "answer": "k > (c-a)f(b)"
    },
    {
        "q": "Let f(x) = x^2 + mx + n + 2... Rolle's Theorem at x = 4/3...",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    }
]

st.set_page_config(layout="wide")
st.title("JEE Advanced Mock Test")

# Timer Logic
if 'timer' not in st.session_state:
    st.session_state.timer = 1800 # 30 minutes in seconds

# Display Timer
mins, secs = divmod(st.session_state.timer, 60)
st.sidebar.metric("Time Remaining", f"{mins:02d}:{secs:02d}")

# State for answers
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Quiz Interface
for i, q in enumerate(questions):
    st.subheader(f"Q.{i+1}")
    choice = st.radio(q['q'], q['options'], key=f"q{i}")
    st.session_state.answers[i] = choice

if st.button("Submit & Analyze"):
    score = 0
    for i, q in enumerate(questions):
        if st.session_state.answers[i] == q['answer']:
            score += 4
        else:
            score -= 1
    st.success(f"Test Finished! Your Score: {score}")
    
