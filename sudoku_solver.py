#from http://norvig.com/sudoku.html

from string import ascii_uppercase
from string import digits
from collections import namedtuple

def cross(A, B):
    """Cross product of elements in
    A and elements in B."""
    return [a + b for a in A for b in B]



def setup_puzzle(size):

    rows = ascii_uppercase[:size]
    cols = digits[-size:]

    squares = cross(rows, cols)

    unitlist = ([cross(rows, c) for c in cols] +
                [cross(r, cols) for r in rows] +
                [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

    units = dict((s, [u for u in unitlist if s in u]) for s in squares)

    peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)

    Puzzle = namedtuple('Puzzle', field_names='squares, unitlist, units, peers, size')

    return Puzzle(squares=squares, unitlist=unitlist, units=units, peers=peers, size=size)


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
    return dict(zip(Puzzle.squares, chars))

