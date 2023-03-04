import os
import openai

from GPTX.common import cost_per_token

from dotenv import load_dotenv

load_dotenv()   # Load all the ENV variables into your os enviroment.
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get your API key from an environment variable

conversation = []
cost_per_token = (0.002 / 1000)
total_tokens = 0

system_msg = input("What type of AI would you like to create?\n")

conversation.append ({"role": "system", "content": system_msg})

print("Ready. Type quit() when done.")

while True:
    msg = input("YOU: ")
    if "quit()" in msg:
        break
    conversation.append ({"role": "user", "content": msg})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    reply = response["choices"][0]["message"]["content"]
    total_tokens += response['usage']['total_tokens']

    conversation.append({"role": "assistant", "content": reply})
    print(reply + "\n")

print("\nThis conversation used {} tokens and cost ${:.5f}".format(total_tokens, cost_per_token * total_tokens))