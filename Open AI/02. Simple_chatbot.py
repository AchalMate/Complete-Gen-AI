from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(messages, model="gpt-4.1-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

# Chat history
messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = chat_completion(messages)

    print("Bot:", response)

    messages.append({"role": "assistant", "content": response})