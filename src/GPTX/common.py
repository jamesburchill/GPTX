# Common GPTX Code

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
