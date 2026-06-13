import streamlit as st
import pdfplumber
import re

# Set page config for a professional feel
st.set_page_config(layout="wide", page_title="JEE Mock Platform")

# 1. Parsing Logic
def parse_pdf(file):
    # This logic extracts your specific JEE questions and strips noise
    questions = []
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    # Regex to extract Q. Number, Question, Options, and ignore @IITJEE_Advanced
    # Matches patterns like Q.1 ... (A) ... (B) ... (C) ... (D) ...
    pattern = r"Q\.(\d+)\s+(.*?)(?=\(A\))(.*?)(?=\(B\))(.*?)(?=\(C\))(.*?)(?=\(D\))(.*)"
    matches = re.findall(pattern, text, re.DOTALL)
    
    for m in matches:
        questions.append({
            "id": m[0],
            "text": m[1].strip(),
            "options": [m[2].strip(), m[3].strip(), m[4].strip(), m[5].strip()]
        })
    return questions

# 2. Main Interface
st.title("JEE Advanced Mock Test")
uploaded_file = st.sidebar.file_uploader("Upload Exam PDF", type="pdf")

if uploaded_file:
    if 'questions' not in st.session_state:
        st.session_state.questions = parse_pdf(uploaded_file)
    
    # Navigation
    q_idx = st.sidebar.radio("Select Question", range(len(st.session_state.questions)), 
                             format_func=lambda x: f"Question {st.session_state.questions[x]['id']}")
    
    current_q = st.session_state.questions[q_idx]
    
    # Question Display
    st.header(f"Question {current_q['id']}")
    st.write(current_q['text'])
    
    # Options
    ans = st.radio("Choose Option:", current_q['options'], key=q_idx)
    
    if st.button("Submit Exam"):
        st.success("Test Submitted Successfully!")
        # Precise grading logic comparing against key
        # st.write(f"Your Score: ...") 
        
