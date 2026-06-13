import streamlit as st
import pdfplumber
import re

st.set_page_config(layout="wide", page_title="JEE Mock Platform")

def parse_pdf(file):
    questions = []
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    # Regex to extract Q. Number, Question, and Options
    pattern = r"Q\.(\d+)\s+(.*?)(?=\(A\))(.*?)(?=\(B\))(.*?)(?=\(C\))(.*?)(?=\(D\))(.*)"
    matches = re.findall(pattern, text, re.DOTALL)
    
    for m in matches:
        questions.append({
            "id": m[0],
            "text": m[1].strip(),
            "options": [m[2].strip(), m[3].strip(), m[4].strip(), m[5].strip()]
        })
    return questions

st.title("JEE Advanced Mock Test")
uploaded_file = st.sidebar.file_uploader("Upload Exam PDF", type="pdf")

if uploaded_file:
    if 'questions' not in st.session_state:
        st.session_state.questions = parse_pdf(uploaded_file)
    
    q_idx = st.sidebar.radio("Select Question", range(len(st.session_state.questions)), 
                             format_func=lambda x: f"Question {st.session_state.questions[x]['id']}")
    
    current_q = st.session_state.questions[q_idx]
    
    st.header(f"Question {current_q['id']}")
    st.write(current_q['text'])
    
    st.radio("Choose Option:", current_q['options'], key=q_idx)
    
    if st.button("Submit Exam"):
        st.success("Test Submitted Successfully!")
        
