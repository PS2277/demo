from dotenv import load_dotenv
import streamlit as st 
import os
import google.generativeai as genai 

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Function to get responses from the Gemini AI with a custom prompt
def get_gemini_response(question):
    prompt = f"You are a highly experienced veterinary doctor specializing in the care, treatment, and well-being of animals. Your expertise spans various species, including pets, livestock, and wildlife. When answering questions, provide accurate, compassionate, and detailed advice related to animal health, behavior, nutrition, and medical treatments. If the question is not related to veterinary care or animals, politely respond that your expertise is focused on animal-related topics.\n\nUser's question: {question}\nAnswer:"
    response = model.generate_content(prompt)
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Pet Chatbot")
st.header("PET CHATBOT")

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# User input
input = st.text_input("Ask a question about your pet:", key="input")

# When submit is clicked
if st.button("Send"):
    if input:
        # Get the AI response
        response = get_gemini_response(input)
        
        # Update conversation history
        st.session_state.conversation.append({"user": input, "bot": response})

# Display conversation history
for chat in st.session_state.conversation:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Pet Chatbot:** {chat['bot']}")

# Optionally, you can add a clear button to reset the conversation
if st.button("Clear conversation"):
    st.session_state.conversation = []
