import sqlparse

FORBIDDEN_KEYWORDS = {
    "INSERT", "UPDATE", "DELETE", "DROP",
    "ALTER", "TRUNCATE", "CREATE", "REPLACE"
}

def validate_sql(sql: str) -> None:
    sql = sql.strip()

    # 1. Parse
    parsed = sqlparse.parse(sql)
    if not parsed or len(parsed) != 1:
        raise ValueError("Only single SQL statements are allowed")

    stmt = parsed[0]

    # 2. Must start with SELECT
    first_token = stmt.token_first(skip_cm=True)
    if not first_token or first_token.value.upper() != "SELECT":
        raise ValueError("Only SELECT queries are allowed")

    # 3. Reject forbidden keywords anywhere
    for token in stmt.flatten():
        if token.is_keyword:
            if token.value.upper() in FORBIDDEN_KEYWORDS:
                raise ValueError(f"Forbidden SQL keyword detected: {token.value}")
