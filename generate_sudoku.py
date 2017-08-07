import copy
import random

import sudoku


def generate_situation():
    matrix = """
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0
    """
    matrix = matrix.strip()
    matrix = matrix.split('\n')
    matrix = [[int(x) for x in row.split()] for row in matrix]
    all_situation = sudoku.solve(matrix, False)
    if all_situation:
        return all_situation[0]
    else:
        return None


def solve_only_one(s):
    num = 0
    stack = []
    next = True
    while True:
        if next:
            point, choices = s.getMinChoice()

        if point == (None, None):
            num += 1
            if num > 1:
                return False

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

    return True


def make_emptinesses(s):
    points = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(points)
    for x, y in points:
        temp = s.matrix[x][y]
        s.matrix[x][y] = 0
        trial = copy.deepcopy(s)
        if not solve_only_one(trial):
            s.matrix[x][y] = temp
        print(x, y)
        s.mprint()

    return s

def main():
    s = generate_situation()
    s = make_emptinesses(s)
    print("=" * 20)
    s.mprint()


if __name__ == '__main__':
    main()
