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

## Installation

### Getting Started with the Repository

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sanikasanikachaudhari071/StayAI
   ```
2. **Install Dependencies**

   a. **Install Python Packages**
   ```bash
   # Navigate to project directory
   cd StayAI

   # Create the Python environment
   python3.10 -m venv .venv

   # Activate the environment
   # For Linux/Mac
   source .venv/bin/activate
   # For Windows
   .venv/Scripts/Activate
   ```

   b. **Set Up CrewAI**
   ```bash
   # Navigate to CrewAI directory
   cd backend/agents/stay_ai_crew

   # Copy the env_template.txt file to .env
   cp env_template.txt .env

   # Run CrewAI setup
   crewai run
   ```

   c. **Configure Environment Variables**
   - Copy the `env_template.txt` file to `.env` and replace the placeholders with your actual keys.
   ```bash
   cp env_template.txt .env
   ```
   - You need to obtain API keys from:
     - Jina AI
     - Groq
     - Serper API

3. **Install Additional Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Application**
   - Run the Streamlit app:
   ```bash
   # Make sure you are in the root directory
   streamlit run frontend/app.py
   ```

   - Run the FastAPI server:
   ```bash
   # Make sure you are in the root directory
   python main.py
   ```

   **Note:** Ensure that both the Streamlit app and the FastAPI server are running simultaneously.

## Project Structure

```
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
```

## Dependencies

- **Python** (v3.9 or v3.10)
- **Streamlit**
- **FastAPI**
- **CrewAI**
- **Langchain**
- **Langchain-community**
- **Langchain-text-splitters**
- **ChromaDB**
- **Mem0AI**
- **Groq**

## Contributing

1. **Fork the Repository**
2. **Create a New Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add your message here"
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

You can contactme on [Sanika Chaudhari](sanikachaudhari071@gmail.com)

## Acknowledgments

- Thanks to all contributors and the open-source community for their support and resources.



