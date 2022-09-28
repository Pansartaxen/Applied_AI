import random
from time import sleep
import numpy as np
import math
from playsound import playsound

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#'],
    ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#'],
    ['#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

class Path:
    def __init__(self, path):
        self.path = path
        self.wall_hits = 0
        self.position = [1,1]
        self.mutation = 0.1
        self.fitness = 9999

    def moveValidation(self, maze, move, x, y):
        """
        Checks if the move is valid
        0: Do nothing
        1: Move up
        2: Move down
        3: Move left
        4: Move right
        """
        if move == 1:
            if maze[y-1][x] == '#':
                self.wall_hits += 1
                return False
            else:
                return True
        elif move == 2:
            if maze[y+1][x] == '#':
                self.wall_hits += 1
                return False
            else:
                return True
        elif move == 3:
            if maze[y][x-1] == '#':
                self.wall_hits += 1
                return False
            else:
                return True
        elif move == 4:
            if maze[y][x+1] == '#':
                self.wall_hits += 1
                return False
            else:
                return True
    
    def moveRight(self):
        self.position = (self.position[0]+1, self.position[1])

    def moveLeft(self):
        self.position = (self.position[0]-1, self.position[1])
    
    def moveUp(self):
        self.position = (self.position[0], self.position[1]-1)

    def moveDown(self):
        self.position = (self.position[0], self.position[1]+1)
    
    def changePath(self, path):
        self.path = path

    def mate(self, par2):
        child_path = []
        for gp1, gp2 in zip(self.path, par2.path):
            prob = random.random()

            if prob < 0.45:
                child_path.append(gp1)

            elif prob < 0.90:
                child_path.append(gp2)

            else:
                child_path.append(random.randint(0,4))

        return Path(child_path) 

    def printPath(self):
        self.position = (1,1)
        maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#'],
            ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#'],
            ['#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', 'G', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        for move in self.path:
            x, y = self.position[0], self.position[1]
            if self.moveValidation(maze, move, x, y):
                if move == 1:
                    self.moveUp()
                elif move == 2:
                    self.moveDown()
                elif move == 3:
                    self.moveLeft()
                elif move == 4:
                    self.moveRight()
            maze[y][x] = '!'
        for row in maze:
            print(row)
        print('\n')

def main(maze: list):
    #GOAL = (31,18)
    GOAL = (21,16)
    #GOAL = (8,18)
    ACC_LEN = 2
    POP_SIZE = 1000
    STRIDE_LEN = 200
    best_path = None
    population = []
    best_score = 100000

    generation = 0

    for i in range(POP_SIZE):
        population.append(Path(list(np.random.randint(low = 0,high=4,size=STRIDE_LEN))))

    while best_score > ACC_LEN:
        generation += 1
        best_score = 100000
        best_path = None

        for i in range(POP_SIZE):
            population[i].position = [1,1]
            for j in range(STRIDE_LEN):
                x, y = population[i].position[0], population[i].position[1]
                move = population[i].path[j]

                if population[i].moveValidation(maze, move, x, y):
                    if move == 1:
                        population[i].moveUp()
                    elif move == 2:
                        population[i].moveDown()
                    elif move == 3:
                        population[i].moveLeft()
                    elif move == 4:
                        population[i].moveRight()

            score = abs(population[i].position[0] - GOAL[0])*33 + abs(population[i].position[1] - GOAL[1])*22 + (population[i].wall_hits)/50
            #score = math.sqrt((population[i].position[0] - GOAL[0])**2 + (population[i].position[1] - GOAL[1])**2) + population[i].wall_hits/10
            population[i].fitness = score
            if score < best_score:
                best_score = score
                best_path = population[i]
                index_best_path = i

        population = sorted(population, key = lambda x:x.fitness)

        if generation % 100 == 0:
            population[0].printPath()
            print('best_score: ', best_score, 'generation: ', generation)
            print('\n')

        new_population = [] 
        s = int(20*POP_SIZE/100)
        new_population = population[:s].copy()

        for _ in range(int(40*POP_SIZE/100)): 
            individual = random.choice(population[40:50])
            new_path = []
            path = individual.path
            for k in range(STRIDE_LEN):
                if random.random() < 0.4:
                    new_path.append(random.randint(0,4))
                else:
                    new_path.append(path[k])
            new_population.append(Path(new_path))


        for _ in range(int(40*POP_SIZE/100)): 
            parent1 = random.choice(population[0:50])
            parent2 = random.choice(population[0:50])
            child = parent1.mate(parent2)
            new_population.append(child)

        population = new_population

        if best_score <= ACC_LEN:
            print('best_path: ', best_path.path, 'was found in generation: ', generation, 'with score: ', best_score, '\n')
            best_path.printPath()
            playsound('/Users/mariusstokkedal/Desktop/DV2619_Tillämpad_AI/Assignment_2/fanfare.wav')
            break

if __name__ == '__main__':
    main(maze)