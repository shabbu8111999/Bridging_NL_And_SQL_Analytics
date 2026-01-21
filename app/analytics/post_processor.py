import pandas as pd
from typing import List, Dict, Any

def process(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not rows:
        return {
            "row_count": 0,
            "columns": [],
            "preview": []
        }

    df = pd.DataFrame(rows)

    return {
        "row_count": int(len(df)),
        "columns": list(df.columns),
        "preview": df.head(10).to_dict(orient="records")
    }
