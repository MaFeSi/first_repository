import streamlit as st
from hugchat.login import Login
from hugchat import hugchat

st.title("Hugging Chat 💬🤗")


@st.cache_resource
def connect_to_hugging_face():
    hf_email = st.secrets['email']
    hf_pass = st.secrets['password']

    # connect to hugging face
    sign = Login(hf_email, hf_pass)
    cookies = sign.login()

    return cookies

def generate_response(prompt):
    cookies = connect_to_hugging_face()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt)

# user message
prompt = st.chat_input("Enter a Prompt")

if prompt:
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            st.write(response)