import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
import os

embedding_func = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path="vectorstore")
collection = chroma_client.get_or_create_collection("nephro", embedding_function=embedding_func)

VECTOR_DB_READY = False

def build_vectorstore():
    global VECTOR_DB_READY

    if VECTOR_DB_READY:
        return  

    pdf_path = "data/nephrology_reference.pdf"
    
    if not os.path.exists(pdf_path):
        print("PDF not found")
        return
    
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        if not text.strip():
            print("PDF contains no readable text")
            return
    except Exception as e:
        print("PDF read error:", e)
        return

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[str(i)])

    print("✅ Vector Store Ready!")
    VECTOR_DB_READY = True
    

def query_rag(query):
    build_vectorstore()
    return collection.query(query_texts=[query], n_results=2)["documents"]
