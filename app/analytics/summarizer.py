def summarize(processed: dict) -> str:
    row_count = processed.get("row_count", 0)
    columns = processed.get("columns", [])

    if row_count == 0:
        return "The query executed successfully but returned no results."

    return f"Returned {row_count} rows with columns {columns}"
