from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

# LOADER
pdf_path = Path("nodejs.pdf")
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

# SPLITTER

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
    )

split_docs = text_splitter.split_documents(documents=docs)


# EMBEDDING
embedder = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key="GEMINI_API_KEY"
    )




        ## USE ONLY AT THE TIME OF THE INJECTION

# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333/",
#     collection_name="learning_langchain",
#     embedding = embedder
# )



# print("DOCS", len(docs))
# print("SPLIT",len(split_docs))

# vector_store.add_documents(documents=split_docs)
print("Injection Done")


## RETRIVING 

retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333/",
    collection_name="learning_langchain",
    embedding = embedder
)

relevant_chunks = retriver.similarity_search(
    query = "What is FS Module?"
)

print(relevant_chunks)

SYSTEM_PROMT = f"""
    You are an helpful AI Assistance who responds base on the available context.

    Context:
    {relevant_chunks}
"""


