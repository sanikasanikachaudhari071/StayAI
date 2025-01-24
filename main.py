import uvicorn
from backend.conversation.chat import chat_with_travel_assistant
from backend.memory.chroma_memory.add_data import add_pdf_to_chroma
from backend.memory.mem0_memory.try_mem0 import add_memory_in_mem0, extract_relevant_memories
from backend.agents.simple_agent_framework.browser_agent import BrowserTool
from backend.agents.simple_agent_framework.browser_agent import BrowserAgent
from backend.app.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    # add_pdf_to_chroma(
    #     pdf_path="/Users/arkajitdatta/Documents/projects/springboard/embedding/pdfs/jaipur_wiki.pdf"
    # )
    # chat_with_travel_assistant()
    
    # tool = BrowserTool()
    # results = tool.search("Give me some information about places to visit in Jaipur")
    # snippets = tool.get_snippets_from_search_results(results)
    # summary = tool.summarize_snippets(snippets)
    # print(summary)
    
    # agent = BrowserAgent()
    # agent.run("Make an plan for a 10 days trip to Bangalore")