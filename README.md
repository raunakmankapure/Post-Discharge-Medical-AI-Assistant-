🏥 Post-Discharge AI Assistant

A Streamlit-based application featuring a two-agent system to provide specialized post-hospitalization support and information to patients.

This prototype is designed to demonstrate a sequential, context-aware conversational flow, ensuring patient identity and specific medical context are established before answering health-related queries using a specialized internal knowledge base.

✨ Features

Two-Phase Interaction: Starts with patient identification (Receptionist Agent) before proceeding to medical Q&A (Clinical Agent).

Patient Verification: Safely retrieves patient records and primary diagnosis from a local JSON database (data/patients.json).

Retrieval-Augmented Generation (RAG): Uses a persistent ChromaDB vector store to ground answers in a specific medical PDF reference (data/nephrology_reference.pdf).

Web Search Fallback: If RAG fails to provide relevant information, the system falls back to a simulated general web search to address external queries.

Activity Logging: Records all agent interactions to an auditable log file (logs/interactions.log).

🛠️ Project Structure

The project is organized into logical modules:

.
├── app.py                      # Main Streamlit application and UI
├── agents/
│   ├── clinical_agent.py       # Logic for handling medical questions (RAG/Web Search)
│   └── receptionist_agent.py   # Logic for patient identification and verification (DB Lookup)
├── data/
│   ├── patients.json           # Mock patient records (Name, Diagnosis)
│   └── nephrology_reference.pdf# Internal knowledge base for RAG
├── utils/
│   ├── db.py                   # Utilities for safe patient data retrieval
│   ├── logger.py               # Configures and logs agent interactions
│   ├── rag.py                  # Handles ChromaDB vector store creation and queries
│   └── web_search.py           # Placeholder for live web search functionality
└── logs/
    └── interactions.log        # Audit log of all conversational messages


🚀 Getting Started

Prerequisites

To run this application, you will need Python installed, along with the required libraries.

# Example dependencies, assuming Python 3.9+
pip install streamlit chromadb PyPDF2


Running the Application

Prepare the Vector Store (Initial Setup):

Ensure your medical reference PDF is placed in data/nephrology_reference.pdf.

The rag.py utility will automatically build the ChromaDB vector store upon the first execution.

Start the Streamlit App:

streamlit run app.py


Interact:

Open the link provided by Streamlit (usually http://localhost:8501).

Phase 1: Enter a patient name (must match a record in data/patients.json).

Phase 2: Ask a medical question.

👥 Agent Interaction Flow

User Enters Name $\rightarrow$ app.py calls receptionist_agent.py

Receptionist Agent $\rightarrow$ Calls utils/db.py to verify identity.

Identity Confirmed $\rightarrow$ User is shown diagnosis and prompted for a question.

User Asks Question $\rightarrow$ app.py calls clinical_agent.py

Clinical Agent $\rightarrow$

Attempt 1: Calls utils/rag.py. If results are found, an internal answer is returned.

Attempt 2: If RAG fails, calls utils/web_search.py (placeholder) for an external lookup.

All Interactions $\rightarrow$ Logged via utils/logger.py.
