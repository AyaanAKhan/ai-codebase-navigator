# CodeMind – AI Codebase Navigator

CodeMind is a semantic search tool designed to help developers explore and understand large codebases more easily.
It uses vector embeddings to power semantic search and provides a 3D dashboard for interactive navigation.

## Features

- **Semantic search**: Query your codebase using natural language or code snippets and receive context-aware results.
- **3D React dashboard**: Visualize your project structure and explore files and dependencies in an intuitive interface built with React and Three.js.
- **FastAPI backend**: A lightweight API server that handles search requests, indexes code, and serves results via REST endpoints.
- **Containerized deployment**: Easily run the entire application locally or on the cloud using Docker and AWS.

## Tech Stack

- Frontend: [React](https://reactjs.org/), [Three.js](https://threejs.org/)
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Containerization: [Docker](https://www.docker.com/)
- Cloud: AWS (optional)

## Quick Start (Backend)

This repository includes a minimal FastAPI backend to get you started.

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn

# Run the API server
uvicorn app.main:app --reload

# Visit http://127.0.0.1:8000 to see the welcome message
```

The frontend implementation (React + Three.js) is not included in this skeleton. You can create a separate
`frontend/` directory for your React application and serve it as needed.

## Folder Structure

```
github_projects/ai-codebase-navigator/
├── README.md        # Project overview and setup instructions
└── app/
    └── main.py      # Minimal FastAPI server skeleton
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the search algorithms,
extend the frontend, or add new features.