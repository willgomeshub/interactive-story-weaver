#!/bin/bash

# --- Checks and Starts MongoDB with flags ---

# Function to display help
show_help() {
    echo "Usage: ./scripts/mongodb/status_mongodb.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -s, --start     Starts the MongoDB service if it is inactive."
    echo "  -n, --no-pager  Shows MongoDB status with the --no-pager flag, i.e., without locking the terminal."
    echo "  -h, --help      Displays this help message."
    echo ""
    echo "If no option is provided, the script will display the status keeping the terminal locked."
}

# Checks if MongoDB is active
is_active() {
    sudo systemctl is-active --quiet mongod
}

should_start=false
no_pager=false

# The first argument of getopts is an option string
# 'snh' means it accepts the flags -s, -n, and -h
while getopts "snh" opt; do
    case "$opt" in
    s)
        # Logic for the -s flag
        should_start=true
        ;;
    n)
        # Logic for the -n flag
        no_pager=true
        ;;
    h)
        # Logic for the -h flag
        show_help
        exit 0
        ;;
    *)
        # Logic for invalid flag
        echo "Invalid option: -$OPTARG"
        show_help
        exit 1
        ;;
    esac
done

# If the -s or --start flag is provided, start the MongoDB service if it is inactive
if $should_start && ! is_active; then
    echo "MongoDB service is inactive. Starting..."
    sudo systemctl start mongod
    sleep 2 # Waits 2 seconds to ensure the service has time to start
    echo ""
fi

# Displays the status of the MongoDB service
if $no_pager; then
    echo "Showing MongoDB status without pager:"
    sudo systemctl status mongod --no-pager
else
    echo "Showing MongoDB status:"
    sudo systemctl status mongod
fi

exit 0