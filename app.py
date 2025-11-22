import streamlit as st
from agents.receptionist_agent import receptionist_flow
from agents.clinical_agent import clinical_flow
from utils.logger import log

st.title("🏥 Post-Discharge AI Assistant")
session = st.session_state

if "patient" not in session:
    name = st.text_input("Enter your name:")
    if st.button("Submit Name"):
        patient, reply = receptionist_flow(name)
        session.patient = patient
        st.write(reply)
        log(f"Receptionist: {reply}")

else:
    question = st.text_input("Describe your problem:")
    if st.button("Ask Doctor"):
        if session.patient is None:
            st.error("Please enter a valid patient name first.")
        else:
            reply = clinical_flow(session.patient, question)
            st.write(reply)
            log(f"Clinical Agent: {reply}")
