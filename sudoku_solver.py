#from http://norvig.com/sudoku.html

from string import ascii_uppercase
from string import digits
from collections import namedtuple

class Puzzle:

    size=9
    rows = ascii_uppercase[:size]
    cols = digits[-size:]

    def __init__(self):
        """initializes puzzle structure with squares,
        defines units and peers"""

        self.squares = cross(self.rows, self.cols)

        self.unitlist = ([cross(self.rows, c) for c in self.cols] +
                    [cross(r, self.cols) for r in self.rows] +
                    [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.squares)

        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)

    def import_state(self, grid):
        """Convert grid into a dict of {square: char} with '0' or '.' for empties"""
        chars = [c for c in grid if c in digits or c in '0.']
        assert len(chars) == 81
        self.values = dict(zip(self.squares, chars))

        #store initial state of puzzle, but return working values dict
        self.initial_state = self.values
        
        return self.values

    def __repr__(self):
        """Display these values as a 2-D grid."""
        width = 1 + max(len(self.values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            print(''.join(self.values[r+c].center(width)+('|' if c in '36' else '') for c in self.cols))
            if r in 'CF': print(line)




def cross(A, B):
    """Cross product of elements in
    A and elements in B."""
    return [a + b for a in A for b in B]


def test_puzzle(Puzzle):
    "A set of unit tests."
    assert len(Puzzle.squares) == Puzzle.size ** 2
    assert len(Puzzle.unitlist) == 27
    assert all(len(Puzzle.units[s]) == 3 for s in Puzzle.squares)
    assert all(len(Puzzle.peers[s]) == 20 for s in Puzzle.squares)
    assert Puzzle.units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert Puzzle.peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')

def grid_to_values(grid, Puzzle):
    """Convert grid into a dict of {square: char} with '0' or '.' for empties"""
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    Puzzle.values = dict(zip(Puzzle.squares, chars))
    return Puzzle

