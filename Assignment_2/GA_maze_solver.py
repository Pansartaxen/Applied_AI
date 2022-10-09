'''
Marius Stokkedal
matk20@student.bth.se
Sep 2022
Karlskrona, Sweden
'''

import random
import copy
import numpy as np
from matplotlib import pyplot as plt

GOAL = (31,18)
#GOAL = (21,16)
#GOAL = (8,18)
ACCEPTED_SCORE = 1
POP_SIZE = 1000
STRIDE_LEN = 200
MAZE = [
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
    def __init__(self, path : list):
        self.path = path
        self.wall_hits = 0
        self.position = [1,1]
        self.fitness = 9999

    def get_pos(self):
        '''Returns current position'''
        return self.position

    def get_fitness(self):
        '''Returns the fitness of the path'''
        return self.fitness

    def set_fitness(self, fitness):
        '''Sets the fitness of the path'''
        self.fitness = fitness

    def move_validation(self, move, x_cord, y_cord):
        """
        Checks if the move is valid
        1: Move up
        2: Move down
        3: Move left
        4: Move right
        Returns True if the move is valid
        and False if the move is invalid
        """
        if move == 1:
            if MAZE[y_cord-1][x_cord] == '#':
                self.wall_hits += 1
                return False
        elif move == 2:
            if MAZE[y_cord+1][x_cord] == '#':
                self.wall_hits += 1
                return False
        elif move == 3:
            if MAZE[y_cord][x_cord-1] == '#':
                self.wall_hits += 1
                return False
        elif move == 4:
            if MAZE[y_cord][x_cord+1] == '#':
                self.wall_hits += 1
                return False

        return True

    def move_right(self):
        '''Moves one step right'''
        self.position = (self.position[0]+1, self.position[1])

    def move_left(self):
        '''Moves one step left'''
        self.position = (self.position[0]-1, self.position[1])

    def move_up(self):
        '''Moves one step up'''
        self.position = (self.position[0], self.position[1]-1)

    def move_down(self):
        '''Moves one step down'''
        self.position = (self.position[0], self.position[1]+1)

    def change_path(self, path):
        '''Sets a new path'''
        self.path = path

    def mate(self, par2):
        '''Mate two parent-paths to create a new path'''
        child_path = []
        for gp1, gp2 in zip(self.path, par2.path):
            prob = random.random()
            if prob < 0.45:
                child_path.append(gp1)
            elif prob < 0.90:
                child_path.append(gp2)
            else:
                child_path.append(random.randint(0,4))

        # JUMP = 3
        # for i in range(0, STRIDE_LEN, JUMP):
        #     prob = random.random()
        #     if prob < 0.4:
        #         child_path.extend(self.path[i:i+JUMP])
        #     elif prob < 0.8:
        #         child_path.extend(par2.path[i:i+JUMP])
        #     else:
        #         child_path.extend([random.randint(0,4) for _ in range(JUMP)])
        
        return Path(child_path)

    def print_path(self):
        """
        Prints path
        0: Do nothing
        1: Move up
        2: Move down
        3: Move left
        4: Move right
        """
        self.position = [1,1]
        maze_cpy = copy.deepcopy(MAZE)
        for move in self.path:
            marker = '0'
            x_cord, y_cord = self.position[0], self.position[1]
            if self.move_validation(move, x_cord, y_cord):
                if move == 1:
                    marker = '^'
                    self.move_up()
                elif move == 2:
                    marker = 'v'
                    self.move_down()
                elif move == 3:
                    marker = '<'
                    self.move_left()
                elif move == 4:
                    marker = '>'
                    self.move_right()
            maze_cpy[y_cord][x_cord] = marker

        for row in maze_cpy:
            print(' '.join(row))
        print('\n')

        maze_cpy.clear()

def main():
    best_path = None
    population = []
    best_score = 100000
    generation = 0
    score_lst = []
    gen_lst = []

    for i in range(POP_SIZE):
        population.append(Path(list(np.random.randint(low = 0,high=4,size=STRIDE_LEN))))
    print('*-*-*-*-* Population created *-*-*-*-*')
    best_path = population[0]

    while best_score > ACCEPTED_SCORE and best_path.get_pos() != GOAL:
        generation += 1
        best_score = 100000
        best_path = None

        for i in range(POP_SIZE):
            population[i].position = [1,1]
            path = population[i]
            for j in range(STRIDE_LEN):
                x_cord, y_cord = path.position[0], path.position[1]
                move = path.path[j]

                if path.move_validation(move, x_cord, y_cord):
                    if move == 1:
                        path.move_up()
                    elif move == 2:
                        path.move_down()
                    elif move == 3:
                        path.move_left()
                    elif move == 4:
                        path.move_right()

            for number in path.path:
                zero_cnt = 0
                if number == 0:
                    zero_cnt += 1

            score = abs(path.position[0] - GOAL[0])*33 + abs(path.position[1] - GOAL[1])*22 - (zero_cnt) + (path.wall_hits)/30
            '''
            Explanation of the score:
            The score is calculated by the distance from the goal, the number of zeros in the path and the number of wall hits.
            The distance from the goal is multiplied by 33 and 22 because the distance in the x-axis is more important than the distance in the y-axis.
            The number of zeroes is calculated because the path should be as short as possible.
            The wall hits are calculated to get a more efficent path and divided by 30 to have a solution in a reasonable time.
            '''
            path.set_fitness(score)
            if score < best_score:
                best_score = score
                best_path = path

        population = sorted(population, key = lambda x:x.get_fitness())

        score_lst.append(population[0].get_fitness())
        gen_lst.append(generation)

        if generation % 100 == 0:
            population[0].print_path()
            print('best_score:', best_score, 'generation:', generation)
            print('\n')

        new_population = []
        stop = int(10*POP_SIZE/100)
        #Adds the best 10% of the population to the new population
        new_population = population[:stop].copy()

        for _ in range(int(45*POP_SIZE/100)):
            #Fills 45% of the new population with a ranndom pick of the 50 best paths
            individual = random.choice(population[0:50])
            new_path = []
            path = individual.path
            for k in range(STRIDE_LEN):
                if random.random() < 0.6:
                    new_path.append(random.randint(0,4))
                else:
                    new_path.append(path[k])
            new_population.append(Path(new_path))

        for _ in range(int(45*POP_SIZE/100)):
            #Fills 45% of the new population by mating a ranom pick of the 30 best paths
            parent1 = random.choice(population[0:30])
            parent2 = random.choice(population[0:30])
            child = parent1.mate(parent2)
            new_population.append(child)

        population = new_population

    print('*-*-Done-*-*\nThe best path was:', best_path.path, 'was found in generation:', generation, 'with score:', best_score, '\n')
    best_path.print_path()
    plt.plot(gen_lst, score_lst)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
