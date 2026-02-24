def winner(board):
    if winning_line(board) or row_winner(board) or column_winner(board) or diagonal_winner(board):
        return True
    else:
        return False

def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True

def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False

def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False

def diagonal_winner(board):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][-i-1])
    return winning_line(diagonal1) or winning_line(diagonal2)



# here's my overcomplicated code.... above is a much a clearer version. ah.

board = [
            ['A', 'A', ' ', 'B', 'B', 'B'],
            [' ', 'A', 'B', 'A', 'B', 'B'],
            ['A', 'A', 'B', 'B', 'B', 'A'],
            ['A', 'A', ' ', 'A', 'B', 'B'],
            ['A', 'A', 'B', 'B', 'B', 'A'],
            [' ', 'B', 'B', ' ', 'B', 'A']
        ]

def row_winner(board):
    print(" -------------------------------- ")
    print("           ROW CHECK ")
    for entry in range(len(board)):
        #print(f"{entry} this is entry")
        check_first = board[entry][0]
        if check_first == ' ':
            #print (f"{board[entry]} starts with SPACE")
            return False
        #print(f"{check_first} this is the first letter in the list)")
        matching = []
        for each in board[entry]:
            matching.append(board[entry][0])
        a = matching
        b = board[entry]
        print(f"{b} vs {a} check")
        if a == b:
            #print(f"{b} vs {a} is TRUE")
            return True
        else:
            #print(f"{b} vs {a} is FALSE")
            pass
    return a == b

def column_winner(board):
    print(" ------------------------------- ")
    print("          COLUMN CHECK ")
    for entry in range(len(board)):
        #print(f"entry: {entry}")
        check_first = board[0][entry]
        matching = []
        column = []
        for each in range(len(board)):
            matching.append(board[0][entry])
            column.append(board[each][entry])
        #print(f"{matching} is matching for a win")
        a = matching
        b = column
        print(f"{b} vs {a} check")
        if a == b and check_first != ' ':
            print(f"{b} vs {a} is TRUE")
            return True
        else:
            print(f"{b} vs {a} is FALSE")
            pass
    return False

def diagonal_winner(board):
    print(" -------------------------------- ")
    print("     DIAGONAL CHECK ")
    # check board length
    board_length = (len(board))-1
    # check top left corner and make array
    check_first = board[0][0]
    check_second = board[0][board_length]
    print(f"top diagonals: {check_first} and {check_second}")
    matching = []
    diagonal = []
    matching_2 = []
    diagonal_2 = []
    for entry in range(len(board)):
        matching.append(board[0][0])
        diagonal.append(board[entry][entry])
        matching_2.append(board[0][board_length])
        diagonal_2.append(board[entry][(entry * -1) - 1])
        #print(f"""
        #entry: {entry} | {(entry * -1) - 1}
        #what I need is 0,-1 1,-2 2,-3, 3,-4
        #or             0, 3 1, 2 2, 1, 3, 0
        #""")
    a = matching
    b = diagonal
    c = matching_2
    d = diagonal_2
    print(f"{b} vs {a} check, first")
    print(f"{d} vs {c} check, second")
    if a == b and check_first != ' ':
        print(f"{b} vs {a} is TRUE")
        return True
    elif c == d and check_second != ' ':
        print(f"{d} vs {c} is TRUE")
        return True
    else:
        print(f"{b} vs {a} is FALSE")
        print(f"{c} vs {d} is FALSE")
        pass
    return False
    
#column_winner(board)
#row_winner(board)



#notes: 
#maybe matching doesn't need to be a list, just check the full board against the first symbol

#I don't think this one worked

# def row_winner(board):
#     row_count = len(board)
#     for entry in range(row_count):
#         matching = board[entry][0]
#         print(f"{matching} is the first entry and must match the rest")
#         for each in board[entry]:
#             print(f"{each} is current entry")
#             if matching == ' ':
#                 print("Matching is Empty, Return False")
#                 return False
#             if matching == :
#                 pass
#             else:
#                 return True


# good



# assert_equal(
#     row_winner(
#         board = [[' ', 'V', 'P', ' '], ['P', 'P', ' ', 'P'], ['P', 'P', 'P', 'P'], [' ', ' ', 'P', 'V']]
#     ),
#     False
# )
# assert_equal(
#     row_winner(
#         [
#             ['X', ' ', 'X'],
#             ['O', 'X', 'X'],
#             ['O', 'O', 'O']
#         ]
#     ),
#     True
# )

# assert_equal(
#     row_winner(
#         [
#             ['S', 'S', 'S', 'S'], 
#             ['M', 'M', 'S', ' '], 
#             [' ', 'S', 'M', 'S'], 
#             [' ', 'M', ' ', 'S']
#         ]
#     ),
#     True
# )

# board = 
