# Author = CCortello
# Date = 8/12/2016

"""Description"""


def safe_pawns(pawns):
    board = [[0]*8 for i in range(8)]
    for i in pawns:
        x = ord(i[0]) - 97
        y = int(i[1]) - 1
        board[x][y] = 1
    print(board)
    return 0


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
