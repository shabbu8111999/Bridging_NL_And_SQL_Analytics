from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.workflows.analytics_flow import run_analytics
from app.utils.logger import get_logger


logger = get_logger()

app = FastAPI(
    title="Query-Bridge",
    description = "An API to bridge natural language queries to SQL analytics.",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_analytics(request: QueryRequest):
    try:
        result = run_analytics(request.question)
        return result
    except Exception as e:
        logger.exception("Analytics Pipeline failed.")
        raise HTTPException(status_code=500, detail=str(e))