moments_dict = {
    "Beg": {
        "text": "\nWelcome to my story of science!\nYou will use the number keys to make choices as you learn about Archimedes.",
        "prompt": "Are you ready?\n1: Yes!\n2: Yes.\nPS: Don't forget to press enter. Also, you can press e to exit.\n\n",
        "choices": ["Test", "Test"]
    },
    "Test": {
        "text": "\nthis is a test text.",
        "prompt": "this is a test prompt.\n1: Back to beginning.\n\n",
        "choices": ["Beg"]
    }
}

class Moment:
    def __init__(self, moment_name):
        self.text = moments_dict[moment_name]['text']
        self.prompt = moments_dict[moment_name]['prompt']
        self.choices = moments_dict[moment_name]['choices']

    def run(self):
        print(self.text)

        usr_input = input(self.prompt)

        if usr_input == 'e':
            exit()

        while True:
            try:
                choice_index = int(input(self.prompt)) - 1

                if choice_index >= 0 and choice_index < len(self.choices):
                    next_moment = Moment(self.choices[choice_index])
                    next_moment.run()
                    break
                else:
                    print("\nINVALID INPUT :(\n") 
            except ValueError:
                print("\nINVALID INPUT :(\n") 

if __name__ == "__main__":
    beginning = Moment("Beg")
    beginning.run()