from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
import gradio as gr
import os

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Add it in Hugging Face Secrets.")

client = genai.Client(api_key=api_key)

# --- Load LinkedIn PDF text ---
reader = PdfReader("me/linkedin.pdf")
linkedin_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin_text += text + "\n"

# --- Load summary text ---
with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

# --- Load resume text ---
resume_reader = PdfReader("me/resume.pdf")
resume_text = ""
for page in resume_reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"

name = "Aadam Ahmed"

system_prompt = f"""You are acting as {name}. You are answering questions on {name}'s website,
particularly questions related to {name}'s career, background, skills, and experience.
Your responsibility is to represent {name} for interactions on the website as faithfully as possible.
You are given a summary of {name}'s background, LinkedIn profile, and resume which you can use to answer questions.
Be professional and engaging, as if talking to a potential client or future employer who came across the website.
If you don't know the answer, say so.
Any questions about any other topic should be redirected to talking about {name}'s career and background.

## Summary:
{summary}

## LinkedIn Profile:
{linkedin_text}

## Resume:
{resume_text}

With this context, please chat with the user, always staying in character as {name}.
"""

def chat(message, history):
    conversation = ""
    for user_msg, assistant_msg in history:
        if user_msg:
            conversation += f"User: {user_msg}\n"
        if assistant_msg:
            conversation += f"{name}: {assistant_msg}\n"

    conversation += f"User: {message}\n"

    full_prompt = system_prompt + "\n\nConversation so far:\n" + conversation

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
    )

    return response.text

demo = gr.ChatInterface(
    fn=chat,
    title="Chat with Aadam",
    description="Ask me about my background, skills, and experience."
)

if __name__ == "__main__":
    demo.launch()
