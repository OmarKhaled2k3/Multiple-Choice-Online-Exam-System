import os

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

'''
from openai import OpenAI
client = OpenAI(api_key="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")
messages = [
        {"role": "system", "content": "You are a helpful assistant."}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

    reply = completion.choices[0].message
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    
'''
