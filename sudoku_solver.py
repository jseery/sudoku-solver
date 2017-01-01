#from http://norvig.com/sudoku.html

def cross(A, B):
	"""Cross product of elements in
	A and elements in B."""
	return [a + b for a in A for b in B]