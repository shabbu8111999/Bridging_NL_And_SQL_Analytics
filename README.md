# Bridging_NL_And_SQL_Analytics


## Execution Flow
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
