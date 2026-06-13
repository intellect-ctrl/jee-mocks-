
import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide", page_title="JEE Advanced Test")

# --- 2. QUESTION BANK ---
questions = [
    {
        "id": 1,
        "text": "Let f(x) be continuous on [a, c] and differentiable in (a, c)...",
        "options": ["k > (c-a)f(b)", "k < (c-a)f(b)", "k = (c-a)f(b)", "k < 2(c-a)f(b)"],
        "answer": "k > (c-a)f(b)"
    },
    {
        "id": 2,
        "text": "Let f(x) = x^2 + mx + n + 2... Rolle's Theorem at x = 4/3...",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    }
]

# --- 3. SESSION STATE ---
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- 4. TIMER & UI ---
st.title("JEE Advanced Mock Test")
elapsed = time.time() - st.session_state.start_time
remaining = max(0, 1800 - elapsed) # 30 min timer
st.sidebar.metric("Time Remaining", f"{int(remaining//60)}:{int(remaining%60):02d}")

# --- 5. QUESTION DISPLAY ---
for q in questions:
    st.write(f"### Q.{q['id']}: {q['text']}")
    # Radio button for answering
    choice = st.radio("Choose Option:", q['options'], key=f"q{q['id']}", index=None)
    st.session_state.user_answers[q['id']] = choice
    st.divider()

# --- 6. SUBMISSION & ANALYSIS ---
if st.button("Final Submit Test"):
    score = 0
    for q in questions:
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 4
        elif st.session_state.user_answers.get(q['id']) is not None:
            score -= 1
    
    st.balloons()
    st.header(f"Your Total Score: {score} / {len(questions) * 4}")
    st.write("Analysis: Precise evaluation based on JEE marking (+4/-1).")
    
