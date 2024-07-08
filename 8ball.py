import random


class Magic8Ball:
    def __init__(self):
        self.responses = [
            "Really? You're asking me that?",
            "Why ask me a question you already know the answer for?",
            "Sure, why not?",
            "You have got to be joking.",
            "Even God doesn't know that.",
            "Ask me again in an hour.",
            "I don't understand the question. Try again.",
            "Ha! Not a chance.",
            "In your dreams!",
            "Right. Sure. Uh-hum.",
            "Wouldn't that be nice?",
            "No. Just, no."
            "Maybe, if you happen to find a magic genie.",
            "I wouldn't be on it"
        ]
        

    def shake(self):
        return random.choice(self.responses)
def main():
    magic_8_ball = Magic8Ball()
    print("Welcome to the Magic 8 Ball!")
    while True:
        question = input("Ask the Magic 8 Ball a question -- or type 'quit' to exit: \n")
        if question.lower() == 'quit':
            break
        else:
            print("The Magic 8 Ball says:  ", magic_8_ball.shake())
            

if __name__ == "__main__":
    main()
