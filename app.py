import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
 
load_dotenv()
 
# Configure Streamlit page settings
st.set_page_config(
    page_title="TerraformScript-Generator Chatbot",
    page_icon="robot_face",
    layout="centered",
)
 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
 
# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')
 
 
# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
 
# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
 
st.title("TerraformScript-Generator Chatbot")
 
# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
 
# Input field for user's message
user_prompt = st.chat_input("Type your message here")
if user_prompt:
 
    st.chat_message("user").markdown(user_prompt)
 
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
 
    with st.chat_message("assistant"):      
        st.markdown(gemini_response.text)


