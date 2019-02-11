from sentence import Sentence
from typing import List


class Crossover:
    def __init__(self, sentence1: Sentence, sentence2: Sentence):
        if len(sentence1.text) != len(sentence2.text):
            raise Exception("Mutation von Sätzen mit unterschiedlicher Länge nicht möglich")
        self.sentence1: Sentence = sentence1
        self.sentence2: Sentence = sentence2

    def crossover(self) -> Sentence:
        sentence: Sentence = Sentence(len(self.sentence1.text))
        midpoint: int = len(self.sentence1.text) / 2
        newText: List[str] = []
        for i in range(len(self.sentence1.text)):
            if i < midpoint:
                newText.append(self.sentence1.text[i])
            else:
                newText.append(self.sentence2.text[i])
        sentence.text = "".join(newText)
        return sentence
