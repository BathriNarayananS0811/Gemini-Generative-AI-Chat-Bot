import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from streamlit import markdown

# Load environment variables from a .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI with the API key
genai.configure(api_key=api_key)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    # Send a message to the chat model and get a response
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app layout
st.title("Gemini AI Chat")

# Prompt user for input through the Streamlit interface
user_input = st.text_input("Enter Any Prompt:")

if user_input:
    # Get the response from the generative AI model
    response = get_gemini_response(user_input)
    
    # Display the response in Markdown format
    for i in response:
        st.markdown(i.text)
