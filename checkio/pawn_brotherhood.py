# Author = CCortello
# Date = 8/12/2016

"""Description"""


def safe_pawns(pawns):

    """"Given a series of strings in chess notation ('b4, c8', ...) find the
    number of safe pawns if they were placed in the given locations."""

    # convert given strings into a 2D array
    board = [[0]*8 for i in range(8)]
    for i in pawns:
        board[ord(i[0]) - 97][int(i[1]) - 1] = 1

    # check
    count = 0
    for i in pawns:
        left_defender = chr(ord(i[0]) - 1) + str(int(i[1]) - 1)
        right_defender = chr(ord(i[0]) + 1) + str(int(i[1]) - 1)
        print(left_defender, i, right_defender)
        if right_defender in pawns or left_defender in pawns:
            count += 1
    return count


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
