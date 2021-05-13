from sys import exit
from enum import Enum

class MomentsEnum(Enum):
    INTRO = 1
    BEG = 2
    BEG_CONT = 3
    WEARING_CROWN = 4
    WEIGHING_METALS = 5
    BATHTUB = 6
    BATHTUB_CONT = 7
    EUREKA = 8
    NAKED = 9
    BOTH = 10
    REAL = 11
    NOT_READY = 12
    REAL_CONT = 13
    EXIT = 14

moments_dict = {
    MomentsEnum.INTRO: {
        "text": "\nWelcome to my story of science!\nYou will use the number keys to make choices as you learn about Archimedes,\nthe most famous mathematician of ancient Greece.\n",
        "prompt": "Are you ready?\n1: Yes!\n2: Yes.\nPS: Don't forget to press enter. Also, you can press e to exit.\n\n",
        "choices": [MomentsEnum.BEG, MomentsEnum.BEG]
    },
    MomentsEnum.BEG: {
        "text": "\nKing Hiero II of Syracuse had a golden crown made for himself.\nHe gave a local goldsmith an adequate amount of gold to produce the crown,\nbut suspected that the crown made was impure with silver,\nwith the goldsmith taking some of the gold for himself.\n",
        "prompt": "1: continue.\n\n",
        "choices": [MomentsEnum.BEG_CONT]
    },
    MomentsEnum.BEG_CONT: {
        "text": "\nFollowing his suspicion, he tasked Archimedes with testing the purity of his crown.\nArchimedes had to answer a question,\nthe question of how he would accomplish this.\n",
        "prompt": "When do you think he came up with an answer?\n1: when wearing the King's crown.\n2: when wearing some gold and silver.\n3: in a bathtub.\n\n",
        "choices": [MomentsEnum.WEARING_CROWN, MomentsEnum.WEIGHING_METALS, MomentsEnum.BATHTUB]
    },
    MomentsEnum.WEARING_CROWN: {
        "text": "\nUnfortunately, that's not how the story goes.\n",
        "prompt": "1: back.\n\n",
        "choices": [MomentsEnum.BEG_CONT]
    },
    MomentsEnum.WEIGHING_METALS: {
        "text": "\nWhile gold and silver have different densities (a key fact for later), that's not how the story goes.\n",
        "prompt": "1: back.\n\n",
        "choices": [MomentsEnum.BEG_CONT]
    },
    MomentsEnum.BATHTUB: {
        "text": "\nWhen in a bath, Archimedes realized that his body displaced water in an amount equal to his volume.\nTherefore, water could be used to measure the volume of non-geometric objects.\n",
        "prompt": "1: continue.\n\n",
        "choices": [MomentsEnum.BATHTUB_CONT]
    },
    MomentsEnum.BATHTUB_CONT: {
        "text": "\nWith water, therefore, the volume of the crown could be measured.\nThen, if the crown was weighed, its density could be calculated.\nThe density of the crown could then be compared to that of pure gold, as silver is less dense than gold.\n",
        "prompt": "What do you think happened when he made this realization?\n1: he exclaimed \"Eureka!\" out of joy.\n2: he leapt out of his bath and ran through the streets of Syracuse naked.\n3: he did all of the above.\n\n",
        "choices": [MomentsEnum.EUREKA, MomentsEnum.NAKED, MomentsEnum.BOTH]
    },
    MomentsEnum.EUREKA: {
        "text": "\nWhile he did shout \"Eureka!\", twice, he also did so while running through the streets of Syracuse naked.\nWell, at least that's how the story goes.\nThe true story isn't as much of a spectacle.\n",
        "prompt": "Ready to learn about the real story?\n1: yes.\n2: also yes.\n3: no.\n\n",
        "choices": [MomentsEnum.REAL, MomentsEnum.REAL, MomentsEnum.NOT_READY]
    },
    MomentsEnum.NAKED: {
        "text": "\nWhile he did run through the streets of Syracuse naked, he also did so while shouting \"Eureka!\" twice.\nWell, at least that's how the story goes.\nThe true story isn't as much of a spectacle.\n",
        "prompt": "Ready to learn about the real story?\n1: yes.\n2: also yes.\n3: no.\n\n",
        "choices": [MomentsEnum.REAL, MomentsEnum.REAL, MomentsEnum.NOT_READY]
    },
    MomentsEnum.BOTH: {
        "text": "\nArchimedes indeed shouted \"Eureka!\" twice as he leapt out of his bath and ran through the streets of Syracuse naked.\nWell, at least that's how the story goes.\nThe true story isn't as much of a spectacle.\n",
        "prompt": "Ready to learn about the real story?\n1: yes.\n2: also yes.\n3: no.\n\n",
        "choices": [MomentsEnum.REAL, MomentsEnum.REAL, MomentsEnum.NOT_READY]
    },
    MomentsEnum.REAL: {
        "text": "\nAlthough no one can know for sure, Archimedes probably solved the king's demand with \"Archimedes' principle\".\nThe principle, also known as the law of buoyancy,\nstates that the upward buoyant force exerted on a body immersed in a fluid\nis equal to the weight of the fuild that the body displaces.\nThis is modeled with the equation F = -pgV,\nwhere F is the buoyant force,\np is the density of the fluid,\ng is the accelaration due to gravity,\nand V is the volume of fluid displaced.\n",
        "prompt": "Ready for further explanation?\n1: yes.\n\n",
        "choices": [MomentsEnum.REAL_CONT]
    },
    MomentsEnum.NOT_READY: {
        "text": "\nSorry, you are going to learn about it anyways, it's not your choice.\n",
        "prompt": "1: continue.\n\n",
        "choices": [MomentsEnum.REAL]
    },
    MomentsEnum.REAL_CONT: {
        "text": "\nInstead of following the method previously mentioned,\nArchimedes probably instead used a contraption (one that is difficult to explain without a diagram) that followed his principle to determine the purity of the crown.\nThis principle of his is crucial to the field of hydrostatics,\nand his discovery of it is one of the reasons why he is one of the most famous mathematicians of ancient Greece.\nAlthough the story of him running through the streets naked is probably fantasy, we can hope that he discovered the principle in a bath.\n",
        "prompt": "1: home.\n\n",
        "choices": [MomentsEnum.INTRO]
    }
}

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