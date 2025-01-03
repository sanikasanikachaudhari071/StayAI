from backend.memory.chroma_memory.retrieve_data import query_chroma
from backend.llms.groq_llm.inference import GroqInference
from backend.memory.mem0_memory.try_mem0 import (
    extract_relevant_memories,
    add_memory_in_mem0,
)
from backend.utils.json_utils import pre_process_the_json_response, load_object_from_string

groq_llm = GroqInference()


def print_section(title: str = "", content: str = "", separator: str = "=") -> None:
    print(f"\n{separator * 80}")
    if title:
        print(f"\n{title}")
        print(f"{'-' * 80}")
    if content:
        print(f"\n{content}\n")
    if separator == "=":
        print(f"{separator * 80}")


def chat_with_travel_assistant():
    system_prompt = """
    You are an assistant who's job is to answer the question of the user based on the data being
    retrieved from the knowledge source.
    
    With each user query, you will be given a list of documents that are relevant to the user query.
    From the list of the documents, you need to find the most relevant answer and give that answer to the user. 
    
    You need to act as a travel expert and answer like you are conversing with the user.
    
    Instructions:
    1. Try to answer the question from the documents, try to keep the answer BRIEF and CONCISE.
    2. Then try to ask some follow up questions to the user to get more information.
    3. If relevant memories are found, use them to answer the user query accordingly. It might help you answer the user query better with the help of the memories.
    """

    messages = [{"role": "system", "content": system_prompt}]
    print("\n" + "=" * 80)
    user_id: str = input("\n👤 Who is the user?.....    ")
    print_section()

    while True:
        user_query: str = input("\n🤔 Ask your question: ")
        print_section()
        
        memories: list[str] = extract_relevant_memories(user_query, user_id)
        print_section("📚 Memories:", memories or "No relevant memories found.")
        
        rephrased_query: str = rephrase_user_query(user_query, memories)
        print_section("📚 Rephrased Query:", rephrased_query)
        
        documents: str = query_chroma(
            rephrased_query, collection_name="travel_data", n_results=3
        )
        

        print_section("📚 Knowledge Source:", documents)
        

        messages.append(
            {
                "role": "user",
                "content": f"""
            USER QUERY: {user_query}
            
            RELEVANT MEMORIES:
            {memories}
            
            RELEVANT DOCUMENTS:
            {documents}
            """,
            }
        )

        assistant_answer: str = groq_llm.generate_response(messages)
        print_section("✨ Travel Assistant:", assistant_answer)

        # Add the assistant answer to mem0
        add_memory_in_mem0(user_query, user_id)
        messages.append({"role": "assistant", "content": assistant_answer})


def rephrase_user_query(query, memories) -> str:
    """
    Rephrase the user query to make it more specific and relevant.
    """

    llm = GroqInference()

    memories = "\n".join(memories)  
    
    system_prompt = """
    You are an expert in rephrasing user queries. You are given a user query and some relevant memories.
    You need to rephrase the user query to make it more specific and relevant according to the memory.
    
    Instructions:
    1. Don't assume any information. Just rephrase the user query to make it more specific and relevant according to the memory..
    2. Give the response in the provided JSON FORMAT
    
    JSON FORMAT:
    ```json
    {
        "rephrased_query": "Rephrased user query"
    }
    ```
    """

    user_prompt = f"""
    User Query: {query}
    
    RELEVANT MEMORIES:
    {memories}
    
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

    return response_object["rephrased_query"]