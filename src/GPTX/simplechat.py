import os
import openai
import pandas

from dotenv import load_dotenv

load_dotenv()   # Load all the ENV variables into your os enviroment.
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get your API key from an environment variable


# --------------------------------------------------------------------------------


MAXLENGTH = 80
conversation = []
cost_per_token = (0.002 / 1000)
total_tokens = 0


# --------------------------------------------------------------------------------


def print_in_chunks(text):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) > MAXLENGTH:
            lines.append(current_line.strip())
            current_line = ''
        current_line += word + ' '
    lines.append(current_line.strip())
    for line in lines:
        print(line)


# --------------------------------------------------------------------------------


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
    # if len(reply) > MAXLENGTH and contains_no_punctuation():
    #     print_in_chunks(reply)
    # else:
    # print(reply)
    print(reply + "\n")

print("\nThis conversation used {} tokens and cost ${:.5f}".format(total_tokens, cost_per_token * total_tokens))