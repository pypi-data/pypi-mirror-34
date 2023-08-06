from .exceptions import FormatError, ComputeError
from .cell import Cell
from collections import deque
from itertools import combinations

import heapq, copy, time


class _Process():
    """A container of solver's table during futher exploration.

    Attributes:
        table: a copy of solver's table.
    """

    @classmethod
    def from_solver(cls, solver):
        return cls(copy.deepcopy(solver.table))

    def __init__(self, table):
        self.table = table

class Solver():

    @staticmethod
    def load(txt):
        """Create a list structure from a special form of string.

        Args:
            txt: a form of string, 9 lines, x represents blank cell that needs to fill. An example here:
                xx31x8xxx
                xx2xxx7xx
                8xx63xxxx
                xx4x568xx
                xxx2x9xxx
                xx538x2xx
                xxxx91xx3
                xx9xxx4xx
                xxx8x79xx
        
        Returns:
            A 2d list object with None values.
        """
        if txt is None or txt == '':
            raise FormatError('Nothing passed in')
        if not isinstance(txt, str):
            raise FormatError('Expect a string value')
        table = list(filter(lambda x: False if x == '' else True, txt.splitlines()))
        if len(table) != 9:
            raise FormatError('Row number is {} which is not equal to 9'.format(len(table)))
        for i,row in enumerate(table):
            try:
                table[i] = list(map(lambda x: None if x == 0 else x,
                    map(int, row.strip().replace(' ', '').replace('x', '0'))))
                if len(table[i]) < 9:
                    raise FormatError('Col-{} has cells less than 9'.format(i+1))
                elif len(table[i]) > 9:
                    raise FormatError('Col-{} has cells more than 9'.format(i+1))
            except ValueError as e:
                msg = e.args[0]
                idx_start = msg.index('\'')
                idx_end = msg.rindex('\'')
                raise FormatError('Row-{} has an error when parsing, {} is not an number'.format(i+1,
                    msg[idx_start:idx_end+1]))
        return table

    @staticmethod
    def validate(table):
        """Check whether or not a table is perfectly complete.
        """
        # test horizontal
        for i in range(9):
            test_cell = Cell()
            test_cell.minus(*table[i])
            if len(test_cell) > 0:
                return False
        # test vertical
        for j in range(9):
            test_cell = Cell()
            test_cell.minus(*(table[i][j] for i in range(9)))
            if len(test_cell) > 0:
                return False
        # test windows
        for ki,kj in ((x,y) for x in range(0,9,3) for y in range(0,9,3)):
            test_cell = Cell()
            for i, j in ((ki+x, kj+y) for x in range(3) for y in range(3)):
                test_cell.minus(table[i][j])
            if len(test_cell) > 0:
                return False
        return True
    
    @classmethod
    def solve(cls, table):
        """Algorithm goes here, pass a 2d list in and get a filled back.
        """
        info = {} # TODO stores some verbose
        exploration = [] # A stack, used to store uncertained tables, wrapped by Process

        def add2exploration(svl):
            x, y = p = min(svl.uncertain, key=lambda p: svl.table[p[0]][p[1]])
            for k in svl.table[x][y].all_possibility():
                process = _Process.from_solver(svl)
                process.table[x][y] = k
                exploration.append(process)

        start_time = time.clock()

        svl = cls(table)
        if not svl.is_end():
            add2exploration(svl)

        while not len(exploration) == 0:
            explore = exploration.pop()
            try:
                svl = cls(explore.table)
                uncertained = len(svl.uncertain)
                if not svl.is_end():
                    add2exploration(svl)
                elif not svl.is_confirm():
                    continue
                else:
                    break
            except ComputeError:
                pass

        info['cost'] = time.clock() - start_time

        if not svl.is_confirm():
            raise FormatError('Search for no result')
        svl.info = info
        return svl

    def __repr__(self):
        line = '+-----------+-----------+-----------+\n'
        s = ''
        for i in range(9):
            s += line if i%3 == 0 else ''
            s += '| {} ! {} ! {} | {} ! {} ! {} | {} ! {} ! {} |\n'.format(*self.table[i])
        s += line
        return s

    def draw(self):
        print(repr(self), end='')

    def is_confirm(self):
        return Solver.validate(self.table)

    def horizontal_indices(self, x, y):
        return [(x,i) for i in range(9) if not i == y]

    def vertical_indices(self, x, y):
        return [(i,y) for i in range(9) if not i == x]

    def cells_indices(self, x, y):
        base = (x-x%3, y-y%3)
        result = []
        for i in range(3):
            for j in range(3):
                a, b = base[0]+i, base[1]+j
                if a == x and b == y:
                    continue
                result.append((a, b))
        return result

    def all_indices(self, x, y):
        idx = set(self.horizontal_indices(x, y) + self.vertical_indices(x, y) + self.cells_indices(x, y))
        for i in idx:
            try:
                self.table[i[0]][i[1]]
            except IndexError:
                continue
            yield i

    def all_affected_cells(self, x, y):
        for p in self.all_indices(x, y):
            i, j = p
            if isinstance(self.table[i][j], Cell):
                yield self.table[i][j]

    def compute_possible_values(self, x, y):
        if isinstance(self.table[x][y], int):
            return self.table[x][y]
        if self.table[x][y] is None:
            self.table[x][y] = Cell()
            self.table[x][y].set_pos(x, y)
        cell = self.table[x][y]
        
        for idx in self.all_indices(x, y):
            i, j = idx
            if isinstance(self.table[i][j], int):
                cell.minus(self.table[i][j])

        if len(cell) == 0:
            raise ComputeError('Collapsed at ROW-{} COL-{}'.format(*map(lambda x: x+1, cell.get_pos())))
        return cell

    def push_affected_cells(self, x, y):
        for p in self.uncertain:
            self.que.append(p)
            
    def is_end(self):
        return True if len(self.uncertain) == 0 else False

    def __init__(self, table):
        self.table = table
        self.uncertain = set()
        self.que = set()

        for x in range(len(self.table)):
            for y in range(len(self.table[x])):
                self.table[x][y] = self.compute_possible_values(x, y)
                if isinstance(self.table[x][y], Cell):
                    self.uncertain.add((x,y))
        self.que = deque(self.uncertain)

        while len(self.que) > 0:
            x, y = pos = self.que.popleft()
            cell = self.table[x][y]
            if pos in self.uncertain:
                if len(cell) == 1:
                    value = cell.get_one()
                    self.uncertain.remove(pos)
                    self.push_affected_cells(x, y)
                    self.table[x][y] = value
                else:
                    self.compute_possible_values(x, y)


    def __getitem__(self, k):
        return self.info[k]