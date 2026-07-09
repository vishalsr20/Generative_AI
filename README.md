# Generative_AI

A collection of experiments exploring Generative AI concepts — LLM integrations (Gemini, OpenAI-compatible APIs, Ollama), Retrieval-Augmented Generation (RAG) for PDFs, embeddings, tokenization, and simple AI agents.

## 📁 Structure
- **RAGS/** – PDF Reader RAG implementation
- **chatgemini.py / geminiChat.py** – Google Gemini chat scripts
- **compatibility_openAi.py** – OpenAI-compatible API wrapper
- **ollama_api.py** – Local LLM via Ollama
- **docker-compose.yml / docker.compose.db.yml** – Docker setup for Ollama & DB
- **embedding.py** – Text embedding generation
- **tokenization.py** – Tokenization utilities
- **langChainPdfReader.py** – PDF reading/processing with LangChain
- **nodejs.pdf** – Sample PDF for RAG testing
- **weather_agent.py / weather_agent_grok.py / practice_weather_agent.py** – Weather agent implementations
- **script.js** – Supporting JS utility
- **requirements.txt** – Python dependencies

## 🚀 Getting Started

```bash
git clone https://github.com/vishalsr20/Generative_AI.git
cd Generative_AI
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

(Optional) Run Ollama locally:
```bash
docker-compose -f docker-compose.yml up -d
docker-compose -f docker.compose.db.yml up -d
```

## 📖 Usage

```bash
python chatgemini.py              # Chat with Gemini
python langChainPdfReader.py       # PDF Reader RAG
python weather_agent.py           # Run weather agent
python embedding.py               # Generate embeddings
```

## 📦 Tech Stack
Python · LangChain · Ollama · Google Gemini API · OpenAI-compatible APIs · Docker

## 🤝 Contributing
Personal learning repo — suggestions and PRs welcome!

## 📄 License
No license specified yet.
```

Create a `.env` file:
