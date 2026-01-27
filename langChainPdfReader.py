from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
file_path = ("./nodejs.pdf")

loader = PyPDFLoader(file_path=file_path)
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(documents=docs)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key="GEMINI_API_KEY"
    )

# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="learning_langchain",
#     embedding= embeddings
# )


# vector_store.add_documents(documents=split_docs)
# print("DOCS",len(docs))
# print("SPLIT",len(split_docs))

print("Injection done!")

relevent_chunks = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embeddings
)

search_result = relevent_chunks.similarity_search(
    query="What is FS Module?"
)

print("Relevent Chunks",search_result)

SYSTEM_PROMPT = """
You are the helpful AI Assistant who respond base of the available context.

Context:
{relevent_chunks}
"""
