from app.llm.text_to_sql import generate_sql
from app.validation.sql_validator import validate_sql
from app.validation.guardrails import enforce_guardrails
from app.database.executor import execute_query
from app.validation.data_validator import validate_data
from app.analytics.post_processor import process
from app.analytics.summarizer import summarize

def run_analytics(question: str):
    """
    End-to-end pipeline:
    natural language question → SQL → execution → processed analytics result
    """

    try:
        sql = generate_sql(question)

        enforce_guardrails(sql)
        validate_sql(sql)

        rows = execute_query(sql)
        warnings = validate_data(rows)

        processed = process(rows)
        summary = summarize(processed)

        return {
            "question": question,
            "sql": sql,
            "summary": summary,
            "data": processed,
            "warnings": warnings
        }

    except Exception as e:
        return {
            "question": question,
            "error": str(e)
        }
