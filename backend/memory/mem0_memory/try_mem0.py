import os

from backend.llms.groq_llm.inference import GroqInference
from backend.utils.json_utils import (
    pre_process_the_json_response,
    load_object_from_string,
)
from mem0 import Memory

config = {
    "llm": {
        "provider": "groq",
        "config": {
            "model": "llama-3.3-70b-versatile",
            "temperature": 0.1,
            "max_tokens": 1000,
        },
    },
    "embedder": {
        "provider": "huggingface",
        "config": {"model": "multi-qa-MiniLM-L6-cos-v1", "embedding_dims": 384},
    },
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "mem0_collection",
            "path": "mem0_db",
        },
    },
}

mem0 = Memory.from_config(config)


def add_memory_in_mem0(query, user_id):
    """User Query and User ID should be provided to add a memory in mem0.
        - User query should be processed to extract the relevant memories from it.
        - The memories should be stored in mem0.
    Args:
        query (str): User query
        user_id (str): User ID
    """

    # Process the query to extract the relevant memories
    relevant_memories = _extract_relevant_memories(query)

    print("\n=== Extracted Memories ===")
    if isinstance(relevant_memories, list):
        print("\nMemories:")
        for i, memory in enumerate(relevant_memories, 1):
            print(f"  {i}. {memory}")
    else:
        print("\nMemories:")
        for i, memory in enumerate(relevant_memories, 1):
            print(f"  {i}. {memory}")
    print("\n" + "=" * 24 + "\n")

    # Add the memories to mem0
    for memory in relevant_memories:
        print(memory)
        mem0.add(memory, user_id=user_id)


def extract_relevant_memories(query, user_id) -> list[str]:
    return [memory["memory"] for memory in mem0.search(query, user_id=user_id)]


def _extract_relevant_memories(query) -> list[str]:
    """Extract the relevant memories from the query.
    Args:
        query (str): User query
    """

    llm = GroqInference()

    system_prompt = """
    You are an expert information extractor. You are given a user query and you need to extract the relevant memories from it.
    For example, if the user query is "I am working on improving my tennis skills. Suggest some online courses.", the relevant memories are "improving tennis skills" and "online courses".
    
    Instructions:
    1. Extract the relevant memories from the user query.
    2. Don't assume any information. Just extract the memories from the user query.
    3. Give the response in the provided JSON FORMAT
    
    The JSON FORMAT is:
    ```json
    {
        "reasoning": "Reasoning for the memories extracted",
        "memories": ["memory1", "memory2", "memory3"]
    }
    ```
    """

    user_prompt = f"""
    User Query: {query}
    
    Note: Only give the JSON as the response.
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = llm.generate_response(messages)
    pre_processed_response = pre_process_the_json_response(response)
    response_object = load_object_from_string(pre_processed_response)

    if response_object is None:
        raise Exception("Failed to extract the relevant memories from the user query.")

    return response_object["memories"]


if __name__ == "__main__":
    add_memory_in_mem0(
        "I am working on improving my tennis skills. Suggest some online courses.",
        "alice",
    )
    extract_relevant_memories("what was the game i searched for last time?", "alice")
