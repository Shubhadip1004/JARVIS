import requests
import random


def get_random_joke(is_online):
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if is_online and response.status_code == 200:
        joke = response.json()["joke"]
        setup = joke.split("?")[0] + "?"
        punchline = joke.split("?")[1].strip() if "?" in joke else ""
        return [setup, punchline] 
    else:
        jokes = [
                ["Why did the computer show up at work late?", "It had a hard drive."],
                ["Why do programmers prefer dark mode?", "Because light attracts bugs."],
                ["Why did the developer go broke?", "Because he used up all his cache."],
                ["Why do Java developers wear glasses?", "Because they don't see sharp."],
                ["Why did the programmer quit his job?", "Because he didn’t get arrays."],
                ["Why was the computer cold?", "It forgot to close its Windows."],
                ["Why did the PowerPoint presentation cross the road?", "To get to the other slide."],
                ["What do you call 8 hobbits?", "A hobbyte."],
                ["Why do Python programmers wear braces?", "Because they can’t C."],
                ["Why was the JavaScript developer sad?", "Because he didn’t know how to ‘null’ his feelings."],
                ["Why did the coder always carry a pencil?", "In case he needed to draw a stack."],
                ["Why did the Boolean go to therapy?", "Because it had too many true/false issues."],
                ["Why do programmers hate nature?", "It has too many bugs."],
                ["Why did the database administrator leave his wife?", "She had one-to-many relationships."],
                ["Why did the AI cross the road?", "To optimize the chicken’s path."],
                ["Why was the developer so calm?", "Because he had good exception handling."],
                ["Why did the smartphone need glasses?", "It lost all its contacts."],
                ["Why did the web developer stay poor?", "Because he used up all his cache on coffee."],
                ["Why do computers hate the ocean?", "Because of all the bytes."],
                ["Why did the network engineer get promoted?", "Because he had great connections."]
            ]

        return random.choice(jokes)

# print(get_random_joke())
