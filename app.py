import streamlit as st
from helper import pipeline, plag_detection

st.title('Plagarism Detection')

option = st.selectbox(
    "Choose your input method",
    ("Upload files", "Paste text")
)

if option == "Upload files":
    col1, col2 = st.columns(2)

    with col1:
        source_file = st.file_uploader("Upload Source File", type="txt", key="source_file")
    with col2:
        answer_file = st.file_uploader("Upload Answer File", type="txt", key="answer_file")
    
    if st.button("Check Plagiarism"):
        if source_file and answer_file:
            source_text = source_file.read().decode("utf-8")
            answer_text = answer_file.read().decode("utf-8")
            
            if source_text == answer_text:
                st.subheader("Same text")
            
            else:
                features = pipeline(answer_text, source_text)
                pred1 = plag_detection(features)
                if pred1 == 1:
                    st.subheader("Plagiarism Detected!")
                elif pred1 == 0:
                    st.subheader("No Plagiarism Detected")
        else:
            st.error("Please upload both source and answer files.")

elif option == "Paste text":
    col1, col2 = st.columns(2)

    with col1:
        source_text = st.text_area("Paste Source Text", height=200, key="source_text")
    with col2:
        answer_text = st.text_area("Paste Answer Text", height=200, key="answer_text")
    
    if st.button("Check Plagiarism"):
        if source_text and answer_text:
            
            
            if source_text == answer_text:
                st.subheader("Same text")
            
            else:
                features = pipeline(answer_text, source_text)
                pred1 = plag_detection(features)
                if pred1 == 1:
                    st.subheader("Plagiarism Detected!")
                elif pred1 == 0:
                    st.subheader("No Plagiarism Detected")
                elif pred1 == -1:
                    st.subheader("Same text")
        else:
            st.error("Please paste both source and answer texts.")