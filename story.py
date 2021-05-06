from sys import exit
from enum import Enum

class MomentsEnum(Enum):
    INTRO = 1
    BEG = 2
    BEG_CONT = 3
    WEARING_CROWN = 4
    WEIGHING_METALS = 5
    BATHTUP = 6

moments_dict = {
    MomentsEnum.INTRO: {
        "text": "\nWelcome to my story of science!\nYou will use the number keys to make choices as you learn about Archimedes,\nthe most famous mathematician of ancient Greece.\n",
        "prompt": "Are you ready?\n1: Yes!\n2: Yes.\nPS: Don't forget to press enter. Also, you can press e to exit.\n\n",
        "choices": [MomentsEnum.BEG, MomentsEnum.BEG]
    },
    MomentsEnum.BEG: {
        "text": "\nKing Hiero II of Syracuse had a golden crown made for himself.\nHe gave a local goldsmith an adequate amount of gold to produce the crown,\nbut suspected that the crown made was impure,\nwith the goldsmith taking some of the gold for himself.\n",
        "prompt": "1: continue.\n\n",
        "choices": [MomentsEnum.BEG_CONT]
    },
    MomentsEnum.BEG_CONT: {
        "text": "\nFollowing his suspicion, he tasked Archimedes with testing the purity of his crown.\nArchimedes had to answer a question,\nthe question of how he would accomplish this.\n",
        "prompt": "When do you think he came up with an answer?\n1: when wearing the King's crown.\n2: when wearing some gold and silver.\n3: in a bathtub.\n\n",
        "choices": [MomentsEnum.INTRO, MomentsEnum.INTRO, MomentsEnum.INTRO]
    }
}

"""
INTRO:
Welcome to my story of science! 
You will use the number keys to make choices as you learn about Archimedes, 
the most famous mathematician of ancient Greece.

0: start.

BEGINNING: 
King Hiero II of Syracuse had a golden crown made for himself. 
He gave a local goldsmith an adequate amount of gold to produce the crown, 
but suspected that the crown made was impure, 
with the goldsmith taking some of the gold for himself.
0: continue.

BEGINNING (cont):
Following his suspicion, he tasked Archimedes with testing the purity of his crown.
Archimedes had to answer a question,
the question of how he would accomplish this.

When do you think he came up with an answer?
0: when wearing the King's crown.
1: when weighing some gold and silver.
2: in a bathtub.

Wearing the crown:
Unfortunately, that's not how the story goes.

0: back.

Weighing gold and silver:



"""
class Moment:
    def __init__(self, moment_name):
        self.text = moments_dict[moment_name]['text']
        self.prompt = moments_dict[moment_name]['prompt']
        self.choices = moments_dict[moment_name]['choices']

    def run(self):
        print(self.text)

        valid_input = False
        while not valid_input:
            usr_input = input(self.prompt)

            if usr_input == 'e':
                exit()

            try:
                choice_index = int(usr_input) - 1

                if choice_index >= 0 and choice_index < len(self.choices):
                    valid_input = True
                    next_moment = Moment(self.choices[choice_index])
                    next_moment.run()
                else:
                    print("\nINVALID INPUT :(\n") 
            except ValueError:
                print("\nINVALID INPUT :(\n") 

if __name__ == "__main__":
    beginning = Moment(MomentsEnum.INTRO)
    beginning.run()