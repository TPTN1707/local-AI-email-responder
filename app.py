import streamlit as st
import ollama

# Page Configuration
st.set_page_config(page_title="Local AI Email Assistant", page_icon=":robot_face: ✉️", layout="centered")

st.title("✉️ Local AI Email Assistant")

# User Input Section
tone = st.selectbox(
    "Select the tone of the email:", 
    ["Professional", "Friendly", "Casual", "Formal", "Persuasive"])

user_input = st.text_area("Enter your email content here:", height=150)

# Validation
if st.button("Generate Email"):
    if not user_input.strip():
        st.error("Please enter some content to generate the email.")
    else:
        # Call the Ollama API to generate the email
        try:
            response = ollama.generate_email(content=user_input, tone=tone)
            st.success("Email generated successfully!")
            st.subheader("Generated Email:")
            st.text_area("", value=response, height=200)
        except Exception as e:
            st.error(f"An error occurred while generating the email: {e}")

# The Prompt
system_prompt = f"""
You are an expert corporate communicator. Rewrite the notes into a well-structured email.
Tone: {tone}.
No explainations, just the email.
"""

# Model Call
try:
    response = ollama.chat(
        model = "llama3.2:1b",
        messages= [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    st.info(response["messages"]["content"])

except Exception as e:
    st.error(f"Error: {e}. Is Ollama running? Please ensure the Ollama server is up and running.")

