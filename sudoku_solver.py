from SudokuPuzzle import SudokuPuzzle


def sample_puzzle():

    test_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

    print('Stringified test puzzle: {}'.format(test_grid))

    p = SudokuPuzzle()

    for square, peer_squares in p.peers.items():
    	print('square: {} // peers: {}'.format(square, peer_squares))
    input('press anything to continue...')

    for square, unit in p.units.items():
    	print('square: {} // units: {}'.format(square, unit))
    input('press anything to continue...')

    return


if __name__ == '__main__':
    sample_puzzle()
