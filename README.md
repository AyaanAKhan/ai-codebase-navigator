# CodeMind: AI Codebase Navigator

CodeMind is a backend foundation for an AI codebase navigation tool. It is designed to help developers search and understand repositories using natural language, semantic indexing, and API driven code exploration.

This repo is intentionally scoped around the FastAPI service layer. The goal is to show backend design, API structure, project documentation, and the planned architecture for an AI developer tool.

## Why This Project Matters

Large repositories are hard to understand when file names, function names, and documentation do not match the way developers ask questions. CodeMind approaches that problem by turning a codebase into searchable context that can be queried through an API.

## Current Features

- FastAPI backend with a clean starting point for API routes
- REST service structure for future repository indexing and search endpoints
- Architecture plan for semantic code search using embeddings
- Planned support for repository parsing, dependency exploration, and interactive visual navigation
- Docker ready project direction for reproducible local and cloud deployment

## Planned Architecture

```text
Developer query
      |
      v
FastAPI service
      |
      v
Repository parser -> chunking/indexing -> vector search
      |
      v
Ranked code results + explanations
      |
      v
Frontend dashboard or IDE extension
```

## Tech Stack

| Area | Tools |
|---|---|
| Backend | Python, FastAPI |
| AI Search | Embeddings, vector search design |
| Deployment | Docker, AWS ready architecture |
| Future UI | React, Three.js |

## Quick Start

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Repository Structure

```text
.
├── README.md
└── app/
    └── main.py
```

## Recruiter Notes

This project demonstrates my interest in AI developer tooling, backend APIs, and scalable software architecture. The next improvements would be repository ingestion, embedding based search, tests, Docker Compose, and a deployed demo.

## Future Improvements

- Add repository upload and GitHub URL ingestion
- Add AST based chunking for Python, JavaScript, TypeScript, Java, and C++
- Store embeddings in a vector database
- Add ranked semantic search endpoint
- Add unit tests and GitHub Actions CI
- Build a React dashboard for visual code exploration
