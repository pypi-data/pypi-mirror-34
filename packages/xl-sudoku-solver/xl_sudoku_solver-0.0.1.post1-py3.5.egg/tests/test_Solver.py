from xl_sudoku_solver.solver import Solver
from xl_sudoku_solver.exceptions import *

import unittest, os

class TestSolver(unittest.TestCase):

    def test_load(self):
        with self.assertRaises(FormatError):
            Solver.load(None)
        with self.assertRaises(FormatError):
            Solver.load('')
        with self.assertRaises(FormatError):
            Solver.load('123456789')
        with self.assertRaises(FormatError):
            Solver.load('123456789\n123456789')
        with self.assertRaises(FormatError):
            Solver.load('123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789')
        with self.assertRaises(FormatError):
            Solver.load('123d26789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789')
        with self.assertRaises(FormatError):
            Solver.load('i1xxxx64x\n5xx1x328x\nxxx75xy1x\n8x4325xxx\n96xxxx7xx\nxxx97685x\n698x37421\n421x895xx\n3x7241x6x')
        with self.assertRaises(FormatError):
            Solver.load("""
            123456789
            12x456789
            123456789
            12345678
            123456789
            123456789
            123456789
            123456789
            12345678x""")
        with self.assertRaises(FormatError):
            Solver.load("""
            123456789
            12x456789
            123456789
            12345678xx
            123456789
            123456789
            123456789
            123456789
            12345678x""")

        self.assertEqual(Solver.load('123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789'),
            [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
        self.assertEqual(Solver.load("""
                             12345        6789
                            12345          6789
                           12345            6789
                          12345              6789
                        12345                 6789
                         12345                 6789
                          12345                 6789
                            12345                6789
                              12345               6789"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
        self.assertEqual(Solver.load("""
            123456789
            12x456789
            123456789
            123456789
            123456789
            123456789
            123456789
            123456789
            12345678x"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,None,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,None]])
        self.assertNotEqual(Solver.load("""
            123456789
            12x456789
            123456789
            123456789
            123456789
            123x56789
            123456789
            123456789
            12345678x"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,None,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,None]])

    def test_validate(self):
        self.assertTrue(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,1,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,8,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,1,9,8],
            [1,9,3,5,2,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,8,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,8,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,1,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,8,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,2,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,1,6,3]
        ]))

    def test_solve(self):
        def open_file(filename):
            print(filename)
            f = open(os.path.join(os.path.dirname(__file__), filename), 'r')
            return f
        with open_file('problem-simple-1.txt') as problem1:
            Solver.solve(Solver.load(problem1.read())).draw()
        with open_file('problem-simple-2.txt') as problem2:
            Solver.solve(Solver.load(problem2.read())).draw()
        with open_file('problem-primary-1.txt') as problem3:
            Solver.solve(Solver.load(problem3.read())).draw()
        with open_file('problem-primary-2.txt') as problem4:
            Solver.solve(Solver.load(problem4.read())).draw()
        with open_file('problem-medium-1.txt') as problem5:
            Solver.solve(Solver.load(problem5.read())).draw()
        with open_file('problem-medium-2.txt') as problem6:
            Solver.solve(Solver.load(problem6.read())).draw()
        with open_file('problem-senior-1.txt') as problem7:
            Solver.solve(Solver.load(problem7.read())).draw()
        with open_file('problem-senior-2.txt') as problem8:
            Solver.solve(Solver.load(problem8.read())).draw()
        with open_file('problem-memory.txt') as problem9:
            Solver.solve(Solver.load(problem9.read())).draw()