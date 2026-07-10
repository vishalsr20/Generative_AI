from mem0 import Memory
from google import genai
from groq import Groq



config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "models/gemini-embedding-001",
            "embedding_dims": 768
        },
    },
    "llm": {
        "provider": "gemini",
        "config": {"api_key": GEMINI_API_KEY, "model": "gemini-2.5-flash"}
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": QDRANT_HOST,
            "port": 6333,
            "embedding_model_dims": 768,
        },
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URL,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD
        },
    },
}

mem_client = Memory.from_config(config_dict=config)
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

USER_ID = "p123"

def chat(message):
    mem_result = mem_client.search(query=message, user_id=USER_ID)
    print(f"\n\nMEMORY:\n\n{mem_result}\n\n")

    memories = "\n".join([m["memory"] for m in mem_result.get("results", [])])

    SYSTEM_PROMPT = f"""
        You are a Memory-Aware Fact Extraction Agent, an advanced AI designed to
        systematically analyze input content, extract structured knowledge, and maintain an
        optimized memory store. Your primary function is information distillation
        and knowledge preservation with contextual awareness.

        Tone: Professional analytical, precision-focused, with clear uncertainty signaling

        Memory and Score:
        {memories}
    """

    # Call Gemini FIRST, so we actually have a result to use
    result = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nUser: {message}"
    )

    reply = result.text

    # Build the conversation turn AFTER we have the reply
    messages = [
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ]

    mem_client.add(messages, user_id=USER_ID)

    return reply


if __name__ == "__main__":
    while True:
        user_message = input(">> ")
        print("BOT:", chat(message=user_message))







