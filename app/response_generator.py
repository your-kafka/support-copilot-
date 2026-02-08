import logging
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

logger = logging.getLogger("copilot")

def draft_response(ticket_text: str, context: str):

    prompt = PromptTemplate(
    template = """
   You are a customer support assistant.

   Use ONLY the information below to answer.
   If the answer is not present, say the issue will be reviewed.

   Context:
   {context}

   Ticket:
   \"\"\"{ticket_text}\"\"\"

   Write a polite, concise support response.
   """,input_variables=['context','ticket_text'])

    try:
        model = ChatGroq(
            model_name="openai/gpt-oss-120b",
            temperature=0.3,
            max_tokens=200
        )
        
        chain = prompt | model

        logger.debug("Invoking response drafting chain")

        response = chain.invoke({
            "ticket_text": ticket_text,
            "context": context
        })

        logger.debug("Draft response generated successfully")

        return response.content

    except Exception:
        logger.exception("Response drafting failed")
        return None
