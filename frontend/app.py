import streamlit as st
import requests
from typing import List, Dict
import json

# Configure the page
st.set_page_config(page_title="StayAI", page_icon="✈️")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Replace the static user_id initialization with a text input
if "user_id" not in st.session_state:
    st.session_state.user_id = ""

# Add user_id input in sidebar
st.sidebar.text_input(
    "Enter User ID",
    key="user_id",
    placeholder="Enter your user ID",
    help="Please enter a unique identifier for your session",
)

# Ensure user_id is provided before allowing chat
if not st.session_state.user_id:
    st.warning("Please enter a User ID in the sidebar to start chatting")
    st.stop()

# API endpoint
API_URL = "http://localhost:8000"  # Adjust this according to your backend URL


def send_message(user_query: str, messages: List[Dict[str, str]]) -> str:
    """Send message to backend API and return the response"""
    payload = {
        "user_id": st.session_state.user_id,
        "user_query": user_query,
        "messages": [
            {"role": msg["role"], "content": msg["content"]} for msg in messages
        ],
    }

    try:
        response = requests.post(f"{API_URL}/chat", json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the backend: {str(e)}")
        return None


# Main UI
st.title("✈️ StayAI")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know about travel?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get bot response
    if response := send_message(prompt, st.session_state.messages):
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)

# Add a button to clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()
