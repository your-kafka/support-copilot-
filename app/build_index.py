from rag_pipeline import build_vector
import logging

logger = logging.getLogger("copilot")
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


#creating vectors 
build_vector()
logger.debug('faiss index created successfully ')
