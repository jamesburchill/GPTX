# Common GPTX Code
import datetime
import os
import time

import openai
from dotenv import load_dotenv

# VARIABLES --------------------------------------------------------------------------------

cost_per_token = (0.002 / 1000)

TRUE_VALUES = ('t', 'T', 'true', 'True', 'TRUE', True, 'y', 'Y', 'yes', 'Yes', 'YES', 1)
FALSE_VALUES = ('f', 'F', 'false', 'False', 'FALSE', False, 'n', 'N', 'no', 'No', 'NO', 0)

HOME = os.environ.get('HOME')

# FUNCTIONS --------------------------------------------------------------------------------


def print_in_chunks(text, MAXLENGTH=80):
    """
    Chops up the text into MAXLENGTH chunks.
    """
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
    """
    Gets the OpenAI API from the .env file and stores it for later use.
    """
    try:
        load_dotenv()  # Load all the ENV variables into your os enviroment.
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Get your API key from an environment variable
    except:
        return False
    else:
        return True


def log(msg):
    """
    Simple logging routine.
    """
    logmsg = '\n' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + "\n" + str(msg) + '\n'
    with open(HOME + '/.tmp/log', 'a') as logfile:
        logfile.write(logmsg)