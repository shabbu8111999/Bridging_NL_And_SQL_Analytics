from typing import List, Dict, Any

def validate_data(rows: List[Dict[str, Any]]) -> Dict[str, str]:
    if rows is None:
        return {"error": "No data returned from query execution"}

    if len(rows) == 0:
        return {"warning": "Query executed successfully but returned no rows"}

    return {}
