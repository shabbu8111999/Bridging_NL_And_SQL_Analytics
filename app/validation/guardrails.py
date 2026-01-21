def enforce_guardrails(sql: str) -> None:
    forbidden = {
        "INSERT", "UPDATE", "DELETE",
        "DROP", "ALTER", "TRUNCATE", "CREATE"
    }

    sql_upper = sql.upper()

    for word in forbidden:
        if f" {word} " in f" {sql_upper} ":
            raise ValueError(f"Forbidden SQL operation detected: {word}")
