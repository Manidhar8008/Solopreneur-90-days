# Technology Decision Matrix

Choose technology according to the customer problem.

| Need | Default starting point | Upgrade when |
|---|---|---|
| Script / automation | Python | Reuse or scale justifies packaging |
| API | FastAPI | Traffic or complexity demands more |
| Web UI | React + TypeScript | Product requirements justify another frontend |
| Database | PostgreSQL | Data scale or architecture requires specialization |
| Semantic search | pgvector | Retrieval scale requires a dedicated vector system |
| Local AI | Ollama / local models | Quality, latency, or economics require another provider |
| Workflow automation | n8n / scripts | Reliability or productization requires a dedicated service |
| Hosting | Simple managed deployment | Usage, compliance, or economics justify deeper infrastructure |

**Customer problem → required capability → simplest reliable technology → evidence → scale.**

Never reverse this into: interesting technology → find a problem.
