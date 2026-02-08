from pydantic import BaseModel
from typing import Literal

class TicketRequest(BaseModel):
    ticket_text: str
    
class TicketClassification(BaseModel):
    category : Literal['billing','general','account','technical']
    risk : Literal['high','low','medium']
    confidence : float