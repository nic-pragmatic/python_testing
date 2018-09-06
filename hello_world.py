def hello_world():
    return 123


def input_number(message):
    while True:
        try:
            user_input = int(message)
        except:
            raise Exception("Not an integer! Try again.")
        else:
            return user_input
