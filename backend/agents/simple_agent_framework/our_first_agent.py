import json
import os
import requests
from abc import ABC, abstractmethod

from backend.llms.groq_llm.inference import GroqInference

SERPER_API_KEY = "<YOUR_SERPER_API_KEY>"
llm = GroqInference()

class OurFirstAgent:
    def __init__(self):
        pass

    def run(self, query):
        pass

    def call_llm(self, query):
        pass

    def _run_tool(self, tool_name, tool_input):
        pass


class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, input):
        pass


class BrowserTool(Tool):
    def __init__(self):
        super().__init__("browsertool", "This is a tool to browse the web")

    def execute(self, input):
        pass

    def search(self, query):
        """Do a search on the web

        Args:
            query (str): The query to search for
        """
        url = "https://google.serper.dev/search"
        payload = json.dumps(
            {
                "q": query,
            }
        )
        headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def get_snippets_from_search_results(self, results):
        """Parse the search results

        Args:
            results (dict): The search results
        """
        organic_answers = results.get("organic", [])
        snippets = [answer.get("snippet", "") for answer in organic_answers]
        return "\n".join(snippets)

    def summarize_snippets(self, snippets: str) -> str:
        """Summarize the snippets

        Args:
            snippets (str): The snippets to summarize
        """
        
        # TODO: Use the LLM to summarize the snippets
        system_prompt = ""
        user_prompt = ""
        
        
        return ""

if __name__ == "__main__":
    tool = BrowserTool()
    results = tool.search("Give me some information about places to visit in Jaipur")
    snippets = tool.get_snippets_from_search_results(results)
    summary = tool.summarize_snippets(snippets)
    print(summary)
