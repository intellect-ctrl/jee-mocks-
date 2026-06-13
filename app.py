import streamlit as st
import time

st.set_page_config(page_title="JEE Mock Test", layout="centered")

# --- Scoring Logic ---
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.questions_attempted = 0
    st.session_state.quiz_started = False

st.title("JEE Mock Test Platform")

# --- Input Area ---
with st.expander("Insert your Questions Here"):
    q_input = st.text_area("Format: Question|OptionA|OptionB|OptionC|OptionD|CorrectAnswer", 
                           height=200, 
                           placeholder="What is 2+2?|2|4|6|8|B")
    if st.button("Load Questions"):
        st.session_state.questions = [line.split('|') for line in q_input.strip().split('\n')]
        st.session_state.quiz_started = True

# --- Exam Environment ---
if st.session_state.get('quiz_started'):
    timer = st.sidebar.number_input("Set Timer (minutes):", min_value=1, value=60)
    
    # Simple Mock Interface
    for i, q in enumerate(st.session_state.questions):
        st.subheader(f"Q{i+1}: {q[0]}")
        user_ans = st.radio(f"Select answer for Q{i+1}:", [q[1], q[2], q[3], q[4]], key=f"q{i}")
        
        if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
            if user_ans == q[5]:
                st.session_state.score += 4
                st.success("Correct! (+4)")
            else:
                st.session_state.score -= 1
                st.error(f"Wrong! (-1). Correct was {q[5]}")

    st.sidebar.metric("Your Current Score", st.session_state.score)

    if st.sidebar.button("Finish Test"):
        st.balloons()
        st.write(f"### Final Score: {st.session_state.score}")
        st.session_state.quiz_started = False
      
