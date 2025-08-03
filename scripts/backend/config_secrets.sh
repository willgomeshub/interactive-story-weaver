#!/bin/bash

# --- Configure project secrets and environment variables ---

show_help() {
    echo "Usage: ./scripts/backend/config_secrets.sh <MONGODB_URI> <GEMINI_API_KEY>"
    echo ""
    echo "Arguments:"
    echo "  <MONGODB_URI>     The full MongoDB connection string."
    echo "  <GEMINI_API_KEY>  Your Gemini API key."
    echo ""
    echo "Example:"
    echo "  ./scripts/backend/config_secrets.sh 'mongodb://user:pass@localhost:27017' 'YOUR_API_KEY'"
}

# Check if the help flag is provided
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    show_help
    exit 0
fi

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Error: Incorrect number of arguments."
    show_help
    exit 1
fi

MONGODB_URI=$1
GEMINI_API_KEY=$2

echo "Configuring .env file..."

# Create a .env file in the backend folder
cat > backend/.env << EOL
# --- Environment Variables ---
# This file is used to store sensitive information.
# DO NOT commit this file to Git.

MONGODB_URI="${MONGODB_URI}"
GEMINI_API_KEY="${GEMINI_API_KEY}"
EOL

echo ".env file created successfully in the 'backend' folder."
echo "Remember to add '.env' to your .gitignore file if you haven't already."

exit 0