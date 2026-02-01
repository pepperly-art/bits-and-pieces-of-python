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
    
column_winner(board)
row_winner(board)



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
