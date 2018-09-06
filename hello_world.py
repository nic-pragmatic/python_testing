import re

def hello_world():
    return 'hello world'


def input_number(message):
    while True:
        user_input = str(message)
        p = re.compile("^[-+]?[0-9]+$")
        m = p.match(user_input)
        if m:
            return int(user_input)
        else:
            raise(Exception)
