from crossover import Crossover
from population import Population
from selection import Selection
import configuration
import time


if __name__ == '__main__':
    start: int = time.time_ns()
    population: Population = Population()
    population.createRandom(configuration.POPULATION_SIZE, configuration.TARGET)
    generationNumber: int = 1
    while True:
        population.calculateFitness()
        population.sortByFitness()
        print(generationNumber, population.getBestSentence().text, "{:.3}".format(population.getBestSentence().fitness))
        if population.isFinished():
            break
        population = Selection(population, configuration.TARGET).tournamentSelectionWithCrossover()
        generationNumber += 1
    end: int = time.time_ns()
    print("Time:", str((end-start)/1000000000), "s")
