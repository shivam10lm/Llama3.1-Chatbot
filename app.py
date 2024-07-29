import os
import gradio as gr
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def chat_with_groq(user_input, additional_info=None):
    messages = [
        {
            "role": "user",
            "content": user_input,
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content


iface = gr.ChatInterface(
    fn=chat_with_groq,
    title="Groq Chatbot",
    description="Ask Anything"
)

if __name__ == "__main__":
    iface.launch()