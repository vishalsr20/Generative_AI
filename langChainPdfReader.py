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
    api_key="GEMINI_API_KEY"
    )

user_query = input("< ")
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
    query=user_query,
    k=3

)

# print("Relevent Chunks",search_result)



def format_docs_as_passage(docs):
    passages = []
    for i, doc in enumerate(docs, start=1):
        page = doc.metadata.get("page", "N/A")
        passages.append(
            f"[Passage {i} | Page {page}]\n{doc.page_content.strip()}"
        )
    return "\n\n".join(passages)


context_passage = format_docs_as_passage(search_result)


SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer the question strictly using the given context.
If the answer is not present in the context, say "I don't know".

Context:
{relevent_chunks}
"""