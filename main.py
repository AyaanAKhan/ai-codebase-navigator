"""Minimal FastAPI server for CodeMind backend.

This module defines a simple FastAPI application with a single root endpoint.  It serves as a starting
point for building out the full CodeMind backend.  The final application may include endpoints for
semantic search, code indexing, authentication, and more.
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured application instance.
    """
    app = FastAPI(title="CodeMind Backend", version="0.1.0")

    @app.get("/")
    async def read_root() -> dict[str, str]:
        """Root endpoint that returns a simple status message.

        Returns:
            dict[str, str]: A dictionary containing a welcome message.
        """
        return {"message": "Welcome to the CodeMind API. This backend is under construction."}

    return app


app = create_app()