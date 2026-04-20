# AI Portfolio Chatbot

An AI-powered chatbot that answers questions about my background using my resume, LinkedIn, and professional summary.

Built with Python and the OpenAI API, this chatbot is deployed using Hugging Face Spaces and embedded into my portfolio website to create an interactive experience for recruiters and visitors.

---

## Live Demo

- Live App: [https://aadamahmed.netlify.app]

---

## Preview

<img width="1440" height="788" alt="Screenshot 2026-04-20 at 12 54 23 AM" src="https://github.com/user-attachments/assets/d43ad65d-e1f7-43a4-b082-6f034864a9f7" />


---

## How It Works

1. User asks a question in the chatbot  
2. Resume and LinkedIn PDFs are read and converted into text using PyPDF  
3. A system prompt defines how the chatbot should respond and stay on-topic  
4. The user question + extracted content are sent to the OpenAI model  
5. The model generates a response based on my background and experience  

---

## Features

- Answers questions about my experience, skills, and projects  
- Uses resume and LinkedIn content as context  
- Maintains conversation history for better responses  
- Redirects off-topic questions back to my background  
- Embedded directly into my portfolio website  

---

## Tech Stack

- Python  
- OpenAI API (GPT-4o-mini)  
- Gradio (chat interface)  
- PyPDF (PDF text extraction)  
- Hugging Face Spaces (deployment)


---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-portfolio-chatbot
cd ai-portfolio-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a .env file
```bash
OPENAI_API_KEY=your_api_key_here
```

### 4. 4. Run the application
```bash
python app.py
```

