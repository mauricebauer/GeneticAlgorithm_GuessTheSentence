from typing import List
from sentence import Sentence
from operator import attrgetter


class Population:
    def __init__(self):
        self.size = 0
        self.sentences: List[Sentence] = []
        self.target = ""
        self.fitnessCalculated: bool = False
        self.sorted: bool = False

    def createRandom(self, size: int, target: str):
        if size % 2 == 1:
            raise Exception("Populationsgröße muss gerade sein!")
        self.size: int = size
        self.sentences: List[Sentence] = []
        for i in range(self.size):
            self.sentences.append(Sentence(len(target)))
        self.target: str = target

    def createByList(self, sentences: List[Sentence], target: str):
        self.size: int = len(sentences)
        self.sentences: List = sentences
        self.target: str = target

    # Calculates fitness -> fitness value is not returned
    def calculateFitness(self):
        if not self.fitnessCalculated:
            self.fitnessCalculated = True
            for sentence in self.sentences:
                sentence.calculateFitness(self.target)

    # Returns if sentence is found. calculateFitness() needs to be ran first
    def isFinished(self) -> bool:
        return max(sentence.fitness for sentence in self.sentences) >= 0.999999999

    # Returns best sentence. calculateFitness() needs to be ran first
    def getBestSentence(self) -> Sentence:
        return max(self.sentences, key=attrgetter('fitness'))

    def sortByFitness(self):
        if not self.sorted:
            self.sorted = True
            self.sentences.sort(key=lambda x: x.fitness, reverse=True)
