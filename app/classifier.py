import logging
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.exceptions import OutputParserException
from app.schema import TicketClassification
from app.prompt import chat_prompt
from app.pydantic_output_parser import parser

load_dotenv()

logger = logging.getLogger("copilot")
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def classify_ticket(ticket_text: str):

    try:
        model = ChatGroq(
            model_name="openai/gpt-oss-120b",
            temperature=0.0,
            max_tokens=200
        )
        logger.debug('api called successfully')
        
        chain = chat_prompt | model | parser

        result = chain.invoke({
            "ticket_text": ticket_text,
            "format_instructions": parser.get_format_instructions()
        })
        logger.debug('chain executed successfully ')

        return result.model_dump_json()
        

    except OutputParserException:
        logger.error(
            "LLM output parsing failed. Raw output: %s"
        )

    except Exception:
        logger.exception("Unexpected error in classify_ticket")

    # Safe fallback
    return TicketClassification(
        category="billing" if "payment" in ticket_text.lower() else "general",
        risk="high",
        confidence=0.0
    )