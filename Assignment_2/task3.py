import random
from time import sleep
import numpy as np
import math

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 'S', 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 'G', 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

class Path:
    def __init__(self, size):
        self.path = list(np.random.randint(low = 0,high=4,size=size))
        self.wall_hits = 0
        self.position = (1,1)
        self.mutation = 0.5

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
            return maze[y-1][x] != 0
        elif move == 2:
            return maze[y+1][x] != 0
        elif move == 3:
            return maze[y][x-1] != 0
        elif move == 4:
            return maze[y][x+1] != 0
    
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

    def mutate(self):
        """
        Mutates the path by changing a random move
        """
        for i in range(len(self.path)):
            if random.uniform(0, 1) < self.mutation:
                self.path[i] = random.randint(0,4)

def main(maze):
    goal = (31,20)
    acc_len = 5 #Accepted length from goal
    best_score = 100
    best_path = None
    population = []

    for i in range(30):
        population.append(Path(30))

    while best_score > acc_len:
        score_list = []
        for i in range(30):
            #print(population[i].path)
            for j in range(30):
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
                else:
                    population[i].wall_hits += 1

            score = abs(population[i].position[0] - goal[0]) + abs(population[i].position[1] - goal[1]) + population[i].wall_hits
            score_list.append(score)
            if score < best_score:
                best_score = score
                best_path = population[i]
                index_best_path = i
        
        score_list, population = (list(t) for t in zip(*sorted(zip(score_list, population))))

        for i in range(30):
            population[i].changePath(best_path.path)
            population[i].mutate()
            population[i].wall_hits = 0
            population[i].position = (1,1)
        
        print('best_score: ', best_score)
        sleep(1)

        if best_score > acc_len:
            best_score = 100
            best_path = None

main(maze)