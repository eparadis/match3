import itertools
import unittest

def hasMatchOfExactLength(matchLength, row):
    groups = [(k, sum(1 for i in g)) for k,g in itertools.groupby(row)]
    for group in groups:
        if group[1] == matchLength:
            return True
    return False

def transposeBoard( board):
    return zip(*board)

def countMatchInRows(matchLength, board):
    count = 0
    for row in board:
        if hasMatchOfExactLength(matchLength, row):
            count += 1
    return count
    
def countMatchInColumns(matchLength, board):
    board = transposeBoard(board)
    return countMatchInRows(matchLength, board)

def countMatchThrees(board):
    return countMatchN(3, board)

def countMatchN(matchLength, board):
    if matchLength == 1:
        r = countMatchInRows(1, board)
        c = countMatchInColumns(1, board)
        return min(r,c)
    return countMatchInRows(matchLength, board) + countMatchInColumns(matchLength, board)


class Match3Tests( unittest.TestCase):
    def test_pinningOriginalBehavior(self):
        a = [ [ 1, 2, 3], 
              [ 1, 2, 4], 
              [ 1, 1, 1] ]
        b = [ [ 1, 2, 3, 4],
              [ 1, 2, 3, 4],
              [ 1, 2, 3, 4],
              [ 5, 6, 3, 8] ]
        self.assertEqual( countMatchThrees(a), 2)
        self.assertEqual( countMatchThrees(b), 3)
        self.assertEqual( countMatchN(2, a), 1)
        self.assertEqual( countMatchN(1, b), 3)

if __name__ == '__main__':
    unittest.main()

