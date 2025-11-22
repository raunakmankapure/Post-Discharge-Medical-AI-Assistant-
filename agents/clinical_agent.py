from utils.rag import query_rag
from utils.web_search import web_search

def clinical_flow(patient, question):
    result = query_rag(question)
    if result and result[0]:
        return f"📘 Based on nephrology reference:\n{result[0][0]}"

    return web_search(question)
