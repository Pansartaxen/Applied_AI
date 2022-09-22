from queue import Queue

class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_dfs(self):
        """Solves the puzzle using a DFS aproach"""
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        explorations = 0
        while stack:
            solution = stack.pop()
            #explorations += 1
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                explorations += 1
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
        return solutions, explorations

    def solve_bfs(self):
        """Solves the puzzle using a BFS aproach"""
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        explorations = 0
        while not queue.empty():
            #explorations += 1
            solution = queue.get()
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                explorations += 1
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.put(queens)
        return solutions, explorations

    def conflict(self, queens):
        """
        Checks if the current placement is okay or not
        Returns True if there is a conflict and False otherwise
        """
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens):
        """Not used but saved just in case xD"""
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)
