from langchain.output_parsers import PydanticOutputParser
from app.schema import TicketClassification

parser = PydanticOutputParser(
         pydantic_object = TicketClassification
)

