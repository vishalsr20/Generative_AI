from fastapi import FastAPI
from fastapi import HTTPException
from models.request import AgentRequest
from agents.planner import create_plan
from agents.executor import execute_plan
from services.document_service import create_word_document
from agents.reflection import review_document
from agents.improver import improve_document
from services.gemini_services import generate_response

app = FastAPI(
    title="Autonomous AI Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent is running."
    }


@app.post("/agent")
def run_agent(request: AgentRequest):

    plan = create_plan(request.request)

    document = execute_plan(request.request,plan)
    reflection = review_document(document)

    if reflection["status"] == "FAIL":
        document = improve_document(
            document,
            reflection["feedback"]
        )
    filePath = create_word_document(document)
    return {
        "plan": plan,
        "reflection":reflection,
        "file":filePath
    }