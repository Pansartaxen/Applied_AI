from cProfile import label
from ex_n_queens import NQueens
from time import time
from matplotlib import pyplot as plt
import math

def main():
    print('.: N-Queens Problem :.')
    performance = [[],[],[],[],[],[]]
    #times = int(input('Enter the number of times the algorithm should be run: '))
    size_range = input('Input range: ')
    size_range = size_range.split(' ')
    size_range = [int(i) for i in size_range]
    #size = 8
    for size in range(size_range[0], size_range[1] + 1):
    #for _ in range(times):
        print(f'Board size: {size}')
        #print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
        n_queens = NQueens(size)
        start_dfs = time()
        dfs_solutions, dfs_exp = n_queens.solve_dfs()
        end_dfs = time()
        start_bfs = time()
        bfs_solutions, bfs_exp = n_queens.solve_bfs()
        end_bfs = time()
        # if print_solutions:
        #     for i, solution in enumerate(dfs_solutions):
        #         print('DFS Solution %d:' % (i + 1))
        #         n_queens.print(solution)
        #     for i, solution in enumerate(bfs_solutions):
        #         print('BFS Solution %d:' % (i + 1))
        #         n_queens.print(solution)
        print(f'Total DFS solutions: {len(dfs_solutions)} in {end_dfs - start_dfs} seconds with {dfs_exp} explorations')
        print(f'Total BFS solutions: {len(bfs_solutions)} in {end_bfs - start_bfs} seconds with {bfs_exp} explorations')
        performance[0].append(size)
        performance[1].append(end_dfs - start_dfs)
        performance[2].append(size)
        performance[3].append(end_bfs - start_bfs)
        performance[4].append(size)
        performance[5].append((dfs_exp*math.log(dfs_exp))/999999)
    plt.plot(performance[0], performance[1], label='DFS')
    plt.plot(performance[2], performance[3], label='BFS')
    plt.plot(performance[4], performance[5], label='Reference')
    plt.legend()
    plt.xlabel('Board size')
    plt.ylabel('Time (seconds)')
    #plt.show()


if __name__ == '__main__':
    main()
