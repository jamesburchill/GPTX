# Common GPTX Code

import os
import openai
from dotenv import load_dotenv

# VARIABLES

cost_per_token = (0.002 / 1000)


# FUNCTIONS

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


def get_api_key():
    try:
        load_dotenv()  # Load all the ENV variables into your os enviroment.
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Get your API key from an environment variable
    except:
        return False
    else:
        return True
