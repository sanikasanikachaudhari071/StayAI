# StayAI

An intelligent assistant for hospitality services, powered by AI Agents and modern Retrieval-Augmented Generation (RAG) systems.

## Overview

StayAI is designed to enhance the hospitality experience by providing automated, intelligent assistance for both guests and service providers. It leverages advanced AI technologies to deliver personalized support and streamline operations.

## Features

- 🤖 AI-powered guest assistance
- 📚 Intelligent information retrieval
- 🏨 Hospitality-specific knowledge base
- 💬 Natural language interaction
- 🔄 Real-time service coordination
- 📊 Analytics and insights

## Getting Started

### Getting started with the repository

1. Fork the repository

2. Clone the repository
```bash
git clone <your-forked-repo-url>
```
3. Install the dependencies
a. Install Python Packages
```bash
# Navigate to project directory
cd StayAI

# Create the python environment
python3.10 -m venv .venv

# activate the environment
linux/max
    source .venv/bin/activate
windows
    .venv/Scripts/Activate

# Install Python dependencies
pip install -r requirements.txt
```

b. Set Up CrewAI
```bash
# Navigate to CrewAI directory
cd backend/agents/stay_ai_crew

# copy the env_template.txt file to .env
cp env_template.txt .env

# Run CrewAI setup
crewai run
```

c. Configure Environment Variables
Copy the env_template.txt file to .env and replace the place-your-key with your actual keys
```bash
# Copy environment template
cp env_template.txt .env
```
    

    

5. Start the application

Run the streamlit app
```bash
# Make sure you are in the root directory
streamlit run frontend/app.py
```

Run the FastAPI server
```bash
# Make sure you are in the root directory
python main.py
```

NOTE: Make sure you have both the streamlit app and the FastAPI server running.

### Prerequisites
 - Python (v3.9 or v3.10)
 - Streamlit
 - FastAPI
 - CrewAI
 - Langchain
 - Langchain-community
 - Langchain-text-splitters
 - ChromaDB
 - Mem0AI
 - Groq

