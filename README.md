# Bridging_NL_And_SQL_Analytics


## Execution Flow
<pre>
User Question
   ↓
FastAPI (/query)
   ↓
Analytics Workflow
   ↓
Schema Loader
   ↓
LLM (Text → SQL)
   ↓
SQL Validator (SELECT only)
   ↓
Query Executor
   ↓
Data Validator
   ↓
Post Processing
   ↓
Natural Language Summary
   ↓
API Response
</pre>

---

## Project Structure
<pre>
bridging_nl_sql_analytics/
│
├── app/
│   ├── main.py                 # Entry point (API / UI)
│
│   ├── config/
│   │   ├── settings.py         # DB, LLM configs
│   │   └── prompts.py          # Prompt templates
│
│   ├── database/
│   │   ├── connection.py       # DB connection
│   │   ├── schema_loader.py    # Load schema info
│   │   └── executor.py         # Run SQL safely
│
│   ├── llm/
│   │   ├── client.py           # OpenAI / LLM wrapper
│   │   ├── text_to_sql.py      # NL → SQL logic
│   │   └── schema_reasoner.py  # Schema understanding
│
│   ├── validation/
│   │   ├── sql_validator.py    # Safety checks
│   │   ├── data_validator.py   # Result validation
│   │   └── guardrails.py       # Rules & policies
│
│   ├── analytics/
│   │   ├── post_processor.py   # Aggregations
│   │   ├── summarizer.py       # NL explanation
│   │   └── visualizer.py       # Charts (optional)
│
│   ├── workflows/
│   │   └── analytics_flow.py   # End-to-end pipeline
│
│   └── utils/
│       ├── logger.py
│       └── exceptions.py
│
├── tests/
│   ├── test_text_to_sql.py
│   ├── test_query_safety.py
│   └── test_workflow.py
│
├── requirements.txt
├── README.md
└── .env
</pre>