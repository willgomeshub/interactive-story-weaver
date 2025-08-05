# Interactive Story Weaver (AI-Powered)

This repository hosts a personal project exploring the exciting intersection of **AI and interactive narrative generation**. The core idea is to build a user-friendly application where users can dive into dynamic stories, shaping the plot through their choices.

This application is a practical playground for:

* **Developing robust backend logic for AI interaction.**
* **Designing an intuitive user interface for narrative engagement.**
* **Experimenting with prompt engineering for varied story outcomes.**

The Interactive Story Weaver is an application that demonstrates the seamless integration of a Generative AI model to:

* **Create initial story prompts and beginnings.**
* **Dynamically expand narratives based on user input.**
* *(Future: Potentially generate visual elements/illustrations that match the story.)*

## Motivation and Tech Stack

The tech stack was chosen to challenge and improve my skills:

* **Backend (API):** Developed in **Python** using **FastAPI**. The choice of Python allows me to enter the AI and data ecosystem, and FastAPI offers a modern and performant way to build asynchronous APIs. This is also my first contact with Python development outside of college work.
* **Frontend (UI):** Built with **Next.js**, **TypeScript**, and **Tailwind CSS**. I opted for a more recent framework to explore the App Router, TypeScript typing, and the agility of a utility-first CSS framework. Here, I stayed a bit closer to what I already know from frontend with React, but still touching on tools I've never experienced before with Next.js and Tailwind CSS.
* **Database:** **MongoDB** was chosen for data persistence, using the flexibility of a document database to model the unstructured nature of stories and interactions. It also gives me experience with configuring and building a non-relational database from scratch. I had contact with MongoDB before, but it was more for querying an existing application. Thinking about how the database structure will be from scratch, considering the characteristics I learned from my previous MongoDB experience, is part of the learning objective.

## Project Architecture

The application follows a well-defined layered architecture, separating responsibilities to ensure scalability and easy maintenance:

* **Controller:** The entry layer, which handles HTTP requests (FastAPI).
* **Service:** Contains the main business logic.
* **Repository:** The data access layer, which interacts directly with MongoDB.

## Key Features

-   Interactive story generation based on user prompts.
-   Persistence of interactions and stories in a MongoDB database.
-   (Still in the conceptual phase) A versioning system that allows the user to track the main narrative path.

## How to Install and Run

To run this project, you will need to have **MongoDB** Python 3.12+ and Node.js 18+ installed.

The project is still in the early stages of development; in the future, I plan to create a script that automates and integrates the setup and execution into simpler steps.

### 1. Database Setup
I used Ubuntu 24.04 for this project, and below is a description of the installation process. If you are on a different system, please search for how to properly install MongoDB on your machine.
To configure the MongoDB database on your Ubuntu 24.04 machine, follow these steps:
1.  Clone the repository:
    ```bash
    git clone [your-repository-here]
    cd [your-project-folder]
    ```
2.  **Install prerequisites and MongoDB:**
    ```bash
    # Install the necessary tools
    sudo apt-get update
    sudo apt-get install -y gnupg curl

    # Import the MongoDB public GPG key
    curl -fsSL [https://www.mongodb.org/static/pgp/server-8.0.asc](https://www.mongodb.org/static/pgp/server-8.0.asc) | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-8.0.gpg

    # Add the MongoDB repository to your system
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] [https://repo.mongodb.org/apt/ubuntu](https://repo.mongodb.org/apt/ubuntu) noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list > /dev/null

    # Update and install MongoDB
    sudo apt-get update
    sudo apt-get install -y mongodb-org
    ```
3.  **Start the MongoDB service:**
    ```bash
    sudo systemctl enable --now mongod
    ```
4.  **Enable Access Control:**
    * Edit the MongoDB configuration file with `sudo nano /etc/mongod.conf`.
    * Add the line `authorization: enabled` with two spaces of indentation in the `security:` section. 
    * **CAUTION:** Indentation is important; do not use tabs, use spaces to match the other sections.
    ```yaml
    security:
      authorization: enabled
    ```
    * Save and close the file.
    * Restart the service for the change to take effect: `sudo systemctl restart mongod`.

5.  **Create the Database and Users:**
    * Access the MongoDB shell and run the following commands, replacing the credentials:
    ```bash
    mongosh
    > use admin
    > db.createUser({
    ...     user: "isw_admin",
    ...     pwd: "your_secure_password",
    ...     roles: [{ role: "root", db: "admin" }]
    ... })
    > use iws_db
    > db.createUser({
    ...     user: "isw_app_user",
    ...     pwd: "another_secure_password",
    ...     roles: [{ role: "readWrite", db: "iws_db" }]
    ... })
    > exit
    ```
6.  **Build the Connection String:**
    * Your connection URI should have the following format, with the database name in the path:
    ```
    mongodb://isw_app_user:another_secure_password@localhost:27017/iws_db?authSource=admin
    ```
### 2. Backend Setup

1.  Navigate to the `backend/` folder:
    ```bash
    cd [your-project-folder]/backend
    ```
2.  Create and activate the virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  Configure environment variables with the secrets script:
    ```bash
    ../scripts/backend/config_secrets.sh "your_mongodb_uri" "your_gemini_api_key"
    ```
4.  Run the FastAPI server:
    ```bash
    ../scripts/backend/run_server.sh
    ```

### 3. Frontend Setup

1.  Navigate to the `frontend/` folder:
    ```bash
    cd [your-project-folder]/frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Configure local environment variables in the `.env.local` file with your backend's URL:
    ```
    NEXT_PUBLIC_API_URL=http://localhost:8000
    ```
4.  Run the Next.js server:
    ```bash
    npm run dev
    ```

Access `http://localhost:3000` in your browser to see the frontend and the API call working.

## License

This project is licensed under the [MIT License](LICENSE).
