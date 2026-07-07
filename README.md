# ✉️ Local AI Email Assistant

A simple AI-powered email writing assistant built with **Streamlit** and **Ollama**.  
The application runs entirely **locally**, allowing users to generate or rewrite emails in different tones without sending data to external APIs.

---

## ✨ Features

- 🤖 Generate emails using a local LLM
- 🎭 Multiple writing tones
  - Professional
  - Friendly
  - Casual
  - Formal
  - Persuasive
- 💻 100% local inference with Ollama
- 🎨 Clean and simple Streamlit interface
- 🔒 No cloud API required

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama
- Llama 3.2 (1B)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/TPTTN1707/local-ai-email-assistant.git

cd local-ai-email-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2:1b
```

Start the Ollama server:

```bash
ollama serve
```

---

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ⚠️ Notes

- Make sure **Ollama** is running before launching the application.
- The current implementation uses **llama3.2:1b**, but you can switch to any model supported by Ollama.
- Performance depends on your hardware and the selected model.

---

## 🔮 Future Improvements

- Copy email to clipboard
- Email templates
- Conversation history
- Custom prompts
- Streaming response
- Support for multiple local models
- Better error handling

---

## ⭐ Acknowledgements

- Streamlit
- Ollama
- Meta Llama