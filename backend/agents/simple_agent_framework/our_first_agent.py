import json
import requests
from abc import ABC, abstractmethod
from backend.llms.groq_llm.inference import GroqInference

SERPER_API_KEY = "85171ec5a4a96963cef76093924898f738744fd9"
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
        system_prompt = '''
        You are a summarization agent that condenses web content into clear and user-friendly summaries.

        instructions:
        1. keep the first few lines brief and introductory.
        '''

        user_prompt = f"""
        Here are some search result snippets:
    
        {snippets}

        Please summarize this content in a concise and easy-to-read manner.
        """

        messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ]
    
        response = llm.generate_response(messages)
        return response


if __name__ == "__main__":
    tool = BrowserTool()
    while True :
        query = input("enter the query or enter [exit]")
        if query.lower() == exit:
            break
        results = tool.search(query)
        snippets = tool.get_snippets_from_search_results(results)
        summary = tool.summarize_snippets(snippets)
        print(summary)
