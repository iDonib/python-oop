from cmd import PROMPT


prompt = "\nTell me something, and i will "
prompt += "repeat back"
prompt += "enter quit to exit "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
