import random
import string


class Sentence:
    # Initialize object with random chars
    def __init__(self, length: int):
        self.text: str = ""
        for i in range(length):
            self.text += random.choice(string.ascii_letters + " ")
        self.fitness: float = 0.0

    # Calculates fitness -> fitness value is not returned
    def calculateFitness(self, target: str):
        if len(self.text) != len(target):
            raise Exception("Length of target sentence is different than length of sentence")
        correctCharacters: int = 0
        for i in range(len(self.text)):
            if self.text[i] == target[i]:
                correctCharacters += 1
        self.fitness = correctCharacters / len(target)

    def mutate(self, chance: float):
        characters = list(self.text)
        for i in range(len(self.text)):
            if random.random() <= chance:
                characters[i] = random.choice(string.ascii_letters + " ")
        self.text = "".join(characters)
