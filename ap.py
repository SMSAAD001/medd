import streamlit as st
import openai

# Set your OpenAI API key here (or use environment variables)
openai.api_key = "your-openai-api-key"

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("💬 Chat with GPT")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")
if user_input:
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get GPT response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # or "gpt-4"
                    messages=st.session_state.messages,
                )
                reply = response['choices'][0]['message']['content']
            except Exception as e:
                reply = f"❌ Error: {e}"

            st.markdown(reply)
            # Save assistant reply to session
            st.session_state.messages.append({"role": "assistant", "content": reply})
