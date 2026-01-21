from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.workflows.analytics_flow import run_analytics
from app.utils.logger import get_logger
from app.utils.exceptions import AnalyticsError


logger = get_logger()

app = FastAPI(
    title="Query-Bridge",
    description="API that converts natural language questions into SQL analytics.",
    version="1.0.0"
)

# -------------------- Request Model --------------------

class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        description="Natural language analytics question"
    )

# -------------------- Response Model --------------------

class QueryResponse(BaseModel):
    question: str
    sql: str | None = None
    summary: str | None = None
    data: dict | None = None
    warnings: dict | None = None
    error: str | None = None

# -------------------- Health Check --------------------

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Query-Bridge API is running",
        "docs": "/docs"
    }

# -------------------- Main Endpoint --------------------

@app.post("/query", response_model=QueryResponse)
def query_analytics(request: QueryRequest):
    logger.info("Received analytics query")

    try:
        result = run_analytics(request.question)

        logger.info("Analytics query executed successfully")

        # Ensure response always matches QueryResponse
        return QueryResponse(**result)

    except AnalyticsError as e:
        logger.warning(f"Analytics error: {e}")

        return QueryResponse(
            question=request.question,
            error=str(e)
        )

    except ValueError as e:
        logger.warning(f"Validation error: {e}")

        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

    except Exception as e:
        logger.exception("Unexpected failure in analytics pipeline")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
