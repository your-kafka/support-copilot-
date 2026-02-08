from fastapi import FastAPI
from app.schema import TicketRequest
from app.classifier import classify_ticket
from app.response_generator import draft_response
from app.decision_engine import decide_action
from app.rag_pipeline import load_vector_store
from app.rag_pipeline import retrieve_context
import logging
import json 

logger = logging.getLogger("copilot")
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

app = FastAPI(title = 'AI support copilot MVP')

logger.debug('vector db loading')
load_vector_db = load_vector_store()
logger.debug('vector db loaded successfully ')


@app.get('/')
def check():
    return {'status':'running'}

@app.post("/ticket")
def process_ticket(request: TicketRequest):
    classification = classify_ticket(request.ticket_text)
    classification_dict = json.loads(classification)    #convert to python dict
    action = decide_action(classification_dict)
    
    response = None 

    if action == "auto_reply":

        context = retrieve_context(request.ticket_text,k=3)
        logger.debug('context retrieved from database')

        response = draft_response(request.ticket_text, context)
        logger.debug('response generated successfully')
    
        return {
        "classification": classification_dict,
        "action": action,
        "draft_response": response}


 
