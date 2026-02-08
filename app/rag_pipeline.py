import os 
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings

data_dir = 'data/knowledge_base'
vector_db_path = 'data/faiss_index'

#load embedding model 
embeddings = HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2" 
)

def build_vector():
    documents = []

    for file in os.listdir(data_dir):
        if file.endswith('.txt'):
            loader = TextLoader(os.path.join(data_dir,file))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50
    )

    chunks = splitter.split_documents(documents)
    
    vector_store = FAISS.from_documents(chunks,embeddings)
    vector_store.save_local(vector_db_path)

def load_vector_store():
    return FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)

def retrieve_context(query:str,k:int=3) -> str:
    vectorstore = load_vector_store()
    docs = vectorstore.similarity_search(query,k=k)
    
    return "\n\n".join(doc.page_content for doc in docs)
