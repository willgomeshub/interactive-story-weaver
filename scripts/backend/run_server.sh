#!/bin/bash

# --- Run the FastAPI server ---

# Check if the virtual environment is active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is active. Starting server..."
    # Run the server in a way that allows it to be stopped with Ctrl+C
    uvicorn main:app --reload
else
    echo "Error: Virtual environment is not active. Please run 'source venv/bin/activate' first."
    exit 1
fi
