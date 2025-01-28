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

##Installation

### Getting started with the repository

1. Clone the repository
```bash
git clone https://github.com/sanikasanikachaudhari071/StayAI
```
2. Install the dependencies
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
*You need to take api key from:
 -- Jina ai
 --Groq 
 --serper api key

3. Install Dependencies:
'''bash
pip install -r requirements.txt
'''
    
4. Start the application

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

### Project Structure

StayAI/
│
├── backend/                    
│   ├── app/                     
│   │   ├── api.py               
│   │   ├── models.py            
│   ├── conversation/           
│   │   ├── chat.py              
│   ├── memory/                 
│   │   ├── chroma_memory/       
│   │   │   ├── add_data.py      
│   │   │   └── retrieve_data.py  
│   │   ├── mem0_memory/      
│   │       ├── try_mem0.py     
│   ├── llms/                    
│   │   ├── groq_llm/           
│   │   │   └── inference.py           
│   │
│   ├── embeddings/              
│   │   ├── base_embedding.py   
│   │   ├── jina_embedding.py             
│   │
│   ├── agents/                 
│   │   ├── simple_agent_framework/
│   │   │   ├── browser_agent.py               
│   │
│   ├── utils/                  
│   │   ├── json_utils.py                         
│   │
│   └── main.py                 
│
├── frontend/                   
│   ├── app.py           
│
├── .env                        
├── requirements.txt                             
└── README.md  

### Dependencies
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

### Contributing

1.Fork the Repository
2. Create a New Branch:
''' bash 
git checkout -b feature/YourFeature
'''
3.Commit your changes:
''' bash 
git commit -m "add your message here"
'''
4.Push to the branch:
''' bash
git push origin feature/YourFeature
'''
5.Open a Pull request



