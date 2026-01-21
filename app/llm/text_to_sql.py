from langchain_core.prompts import PromptTemplate
from app.llm.client import get_llm
from app.config.prompts import TEXT_TO_SQL_PROMPT
from app.llm.schema_reasoner import get_schema_context

def generate_sql(question: str) -> str:
    schema = get_schema_context()
    if not schema:
        raise RuntimeError("Schema context is empty")

    prompt = PromptTemplate(
        input_variables=["schema", "question"],
        template=TEXT_TO_SQL_PROMPT
    )

    response = get_llm().predict(
        prompt.format(schema=schema, question=question)
    ).strip()

    if not response.lower().startswith("select"):
        raise ValueError("LLM did not return a valid SELECT query")

    return response
