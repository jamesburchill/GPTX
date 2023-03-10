import openai

from common import cost_per_token, get_api_key


def chatbot():

    if not get_api_key():
        return False

    conversation = []
    total_tokens = 0

    system_msg = input("What type of AI would you like to create?\n")

    conversation.append({"role": "system", "content": system_msg})

    print("Ready. Type quit() when done.")

    while True:
        msg = input("YOU: ")
        if "quit()" in msg:
            break
        conversation.append({"role": "user", "content": msg})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
        reply = response["choices"][0]["message"]["content"]
        total_tokens += response['usage']['total_tokens']

        conversation.append({"role": "assistant", "content": reply})
        print(reply + "\n")

    print("\nThis conversation used {} tokens and cost ${:.5f}".format(total_tokens, cost_per_token * total_tokens))

    return True


if __name__ == '__main__':
    chatbot()
