from string import ascii_uppercase
from string import digits
from collections import namedtuple


class SudokuPuzzle:

    size=9
    rows = ascii_uppercase[:size]
    cols = digits[-size:]


    def __init__(self):
        """initializes puzzle structure with squares,
        defines units and peers"""

        #self.squares is a list of all the squares in a puzzle
        #in a 9x9 puzzle, self.squares will have len() = 81
        self.squares = cross(self.rows, self.cols)

        #self.unitlist is a list of all rows, columns, and squares
        #each list in self.unitlist contains all the squares in that list
        self.unitlist = ([cross(self.rows, c) for c in self.cols] +
                    [cross(r, self.cols) for r in self.rows] +
                    [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        
        #self.units is a dict where keys are each square, and
        # values are the units from unitlist
        # that the key is a part of
        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.squares)

        #self.peers is also a dict where keys are each square,
        #but instead of a list of units like in self.units,
        #we have a set of the squares that share a unit (row, column, or box) with that square
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)


    def grid_to_values(self, grid):
        """Convert grid into a dict of {square: char} with '0' or '.' for empties"""
        chars = [c for c in grid if c in digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))


    def import_puzzle_state(self, grid):
        """from a grid like test_grid, construct the state of a puzzle
        values in the grid eliminate other possibilities from that square's values
        """
        self.values = dict((s, digits) for s in self.squares)
        for s, d in self.grid_to_values(grid).items():
            if d in digits and not self.assign(s, d):
                return False ##Fail if we can't assign d to squares
        return self.values


    def assign(self, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = self.values[s].replace(d, '')
        if all(eliminate(self.values, s, d2) for d2 in other_values):
            return self.values
        else:
            return False


    def __repr__(self):
        """Display these values as a 2-D grid."""
        width = 1 + max(len(self.values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)

        the_string = ''
        for r in self.rows:
            the_string = the_string + ''.join(self.values[r+c].center(width)+('|' if c in '36' else '') for c in self.cols) + '\n'
            if r in 'CF':
                the_string = the_string + line + '\n'
        return the_string


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