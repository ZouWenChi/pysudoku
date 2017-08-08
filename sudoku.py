import copy
import math
import random
import time


class Situation:

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrixDimension = len(matrix)
        self.boxDimension = int(math.sqrt(self.matrixDimension))

    def mprint(self):
        """
        print the matrix
        """
        for i in range(self.matrixDimension):
            for j in range(self.matrixDimension):
                print(self.matrix[i][j], end=" ")
            print()

    def getChoices(self, x, y, diagonal=False):
        """
        get selective numbers of a point that is empty
        if diagonal is True, then the diagonal elements must be the set
        of 1, 2, 3, ...
        """
        s = set(range(1, self.matrixDimension + 1))

        for j in range(self.matrixDimension):
            v = self.matrix[x][j]
            if v and v in s:
                s.remove(v)

        for i in range(self.matrixDimension):
            v = self.matrix[i][y]
            if v and v in s:
                s.remove(v)

        xx = x // self.boxDimension * self.boxDimension
        yy = y // self.boxDimension * self.boxDimension
        for i in range(xx, xx + self.boxDimension):
            for j in range(yy, yy + self.boxDimension):
                v = self.matrix[i][j]
                if v and v in s:
                    s.remove(v)

        if not diagonal:
            return s

        if x == y:
            for i in range(self.matrixDimension):
                v = self.matrix[i][i]
                if v and v in s:
                    s.remove(v)

        if x == self.matrixDimension - y - 1:
            for i in range(self.matrixDimension):
                v = self.matrix[i][self.matrixDimension - i - 1]
                if v and v in s:
                    s.remove(v)

        return s

    def getMinChoice(self):
        """
        get a point that has minimum selective numbers in the matrix
        """
        r = self.matrixDimension + 1  # let r be big enough
        choices = None
        point = (None, None)
        for i in range(self.matrixDimension):
            for j in range(self.matrixDimension):
                if self.matrix[i][j] != 0:
                    continue
                s = self.getChoices(i, j)
                if len(s) < r:
                    r = len(s)
                    choices = s
                    point = i, j
                    if r == 1:
                        break
        return point, choices


def solve(matrix, all=True):

    all_situation = []
    s = Situation(matrix)
    stack = []
    next = True
    while True:
        if next:
            point, choices = s.getMinChoice()

        if point == (None, None):
            all_situation.append(s)
            if not all:
                break

        if not choices:
            if not stack:
                break
            else:
                s, point, choices = stack.pop()
                next = False
                continue
        v = random.choice(list(choices))
        choices.remove(v)
        stack.append((copy.deepcopy(s), point, copy.deepcopy(choices)))
        s.matrix[point[0]][point[1]] = v
        next = True

    return all_situation


def main():
    matrix = """
    0 2 1 0 7 0 0 0 5
    0 0 0 8 3 0 2 0 0
    7 6 0 0 0 9 4 0 8
    5 9 0 0 8 3 7 2 0
    0 0 0 5 0 0 1 0 9
    0 8 0 7 0 6 0 4 3
    3 0 0 9 2 0 6 5 0
    2 1 5 3 0 0 0 7 0
    9 0 6 0 1 5 0 0 0
    """
    matrix = """
5 7 0 0 0 0 3 0 0 
0 0 0 4 0 0 0 0 8 
6 0 2 0 0 0 0 5 0 
0 0 0 6 0 8 9 0 0 
7 0 0 0 0 0 0 0 0 
2 1 0 0 0 0 0 3 0 
0 0 0 7 0 4 0 0 3 
1 0 0 2 0 0 4 0 0 
0 4 0 8 0 5 6 0 7    
"""

    matrix = matrix.strip()
    matrix = matrix.split('\n')
    matrix = [[int(x) for x in row.split()] for row in matrix]
    all_situation = solve(matrix)

    print("=" * 20)
    for s in all_situation:
        s.mprint()
        print("-" * 20)


if __name__ == "__main__":
    t0 = time.time()
    main()
    t1 = time.time()
    print("The spent time is %f seconds.\n" % (t1 - t0))
