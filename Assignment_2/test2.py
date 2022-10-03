import random
maze = ['1', '1', '1', '1']

def print_maze():
    mace_cpy = maze.copy()
    index = random.randint(0,3)
    mace_cpy[index] = 5
    print(mace_cpy)
    print()

for i in range(10):
    print_maze()
print(maze)