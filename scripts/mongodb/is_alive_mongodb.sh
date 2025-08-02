#!/bin/bash

# --- Checks if MongoDB is running and returns a clear message ---

if sudo systemctl is-active --quiet mongod; then
    echo "MongoDB service is active."
    exit 0 # Returns 0 (success)
else
    echo "MongoDB service is inactive."
    exit 1 # Returns 1 (error/failure)
fi