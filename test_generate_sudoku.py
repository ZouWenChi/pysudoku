import unittest

import generate_sudoku
import sudoku


class TestStringMethods(unittest.TestCase):

    def test_solve_only_one(self):
        matrix = """
            0 9 3 8 4 7 1 2 6 
            6 4 2 1 9 3 8 5 7 
            7 8 1 2 6 5 4 9 3 
            2 3 4 5 8 9 7 6 1 
            8 5 6 4 7 1 9 3 2 
            9 1 7 6 3 2 5 4 8 
            1 7 5 3 2 4 6 8 9 
            3 6 9 7 5 8 2 1 4 
            4 2 8 9 1 6 3 7 5 
            """
        matrix = matrix.strip()
        matrix = matrix.split('\n')
        matrix = [[int(x) for x in row.split()] for row in matrix]
        s = sudoku.Situation(matrix)
        result = generate_sudoku.solve_only_one(s)        
        expect = True
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()



