import logging
from langchain.prompts import ChatPromptTemplate


chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant helping a customer support team."),
        ("human", """
Your task is to classify a support ticket.

Definitions:
HIGH RISK:
- Unauthorized transactions
- Fraud
- Account takeover
- Money debited without user intent
- Security-related issues

MEDIUM RISK:
- Refund delays
- Failed payments
- Duplicate charges (pending resolution)

LOW RISK:
- Informational billing questions
- How long does refund take
- Payment status explanations

CONFIDENCE 
- a number between 0 and 1 indicating how safe it is to auto-handle.
{format_instructions}

Ticket:
\"\"\"{ticket_text}\"\"\"
""")
    ])

logging.debug('chat_prompt generated successfully!!')
