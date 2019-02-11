from population import Population
from sentence import Sentence
from crossover import Crossover
from typing import List
import random
import configuration


class Selection:
    def __init__(self, population: Population, target: str):
        self.population: Population = population
        self.target: str = target

    # Makes a tournament selection and the winners (half of the population) will reproduce 2 times
    # the worse half of the original population will die
    def tournamentSelectionWithCrossover(self) -> Population:
        fighters: List[Sentence] = self.population.sentences.copy()
        winners: List[Sentence] = []
        childs: List[Sentence] = []
        while len(fighters) > 0:
            fighterIndex1: int = random.randrange(0, len(fighters))
            fighter1: Sentence = fighters[fighterIndex1]
            fighters.remove(fighter1)
            fighterIndex2: int = random.randrange(0, len(fighters))
            fighter2: Sentence = fighters[fighterIndex2]
            fighters.remove(fighter2)
            if fighter1.fitness > fighter2.fitness:
                winners.append(fighter1)
            else:
                winners.append(fighter2)
        random.shuffle(winners)
        while len(winners) > 0:
            childs.append(Crossover(winners[0], winners[1]).crossover())
            childs.append(Crossover(winners[1], winners[0]).crossover())
            winners.remove(winners[0])
            winners.remove(winners[0])
        newSentences: List[Sentence] = childs
        for s in newSentences:
            s.mutate(configuration.MUTATION_RATE)
        self.population.sortByFitness()
        originalSize: int = len(self.population.sentences)
        while len(newSentences) < originalSize:
            newSentences.append(self.population.sentences[0])
            self.population.sentences.remove(self.population.sentences[0])
        newPopulation: Population = Population()
        newPopulation.createByList(newSentences, self.target)
        return newPopulation
