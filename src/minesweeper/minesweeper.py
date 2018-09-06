"""a minesweeper"""

import sys
import gamestate

GAME_SIZE = 6
MINE_CHANCE = 0.15

BOMB_GRAPHIC = "*"
SPACE_GRAPHIC = "."
UNREVEALED_GRAPHIC = "?"

def drawBoard(board: gamestate.GameState, fog=True):
    """draw the board"""

    print("\033c \033[1mMOONSWEEPER\033[0m")
    print()
    print()

    headerText = "  "
    for x in range(board.board_size):
        headerText += str(x)

    print(headerText)

    for y in range(board.board_size):

        rowText = str(y) + " "

        for x in range(board.board_size):

            cell = board.get_state_of_cell(gamestate.Coordinate(x, y))

            if fog and not cell.revealed:
                rowText += UNREVEALED_GRAPHIC

            elif cell.mine:
                rowText += "\033[31m" + BOMB_GRAPHIC + "\033[0m"

            elif cell.adjacent == 0:
                rowText += SPACE_GRAPHIC
            else:
                rowText += "\033[36m" + str(cell.adjacent) + "\033[0m"

        print(rowText)

def makeMove(board, x, y):
    board.reveal(gamestate.Coordinate(x, y))

def isWon(board):
    return board.cells_remaining() == 0


# board = engine.makeBoard()

def mainLoop():
    """main loop"""

    board = gamestate.GameState(GAME_SIZE, MINE_CHANCE)

    while not isWon(board):

        drawBoard(board)

        print()
        print("type coordinate to reveal (xy) then press return")
        print()

        sys.stdout.flush()

        command = sys.stdin.readline()

        command = command.rstrip()

        if command == "quit":
            sys.exit()

        if len(command) > 2:
            print("coordinate too long")
            continue

        if len(command) < 2:
            print("coordinate too short")
            continue

        try:
            x = int(command[0])
            y = int(command[1])

        except:

            continue

        try:
            makeMove(board, x, y)
        except:

            drawBoard(board, fog=False)

            print("BANG YOU DIED.")

            sys.exit()

    drawBoard(board)

    if isWon(board):
        print("YAY YOU WON")

mainLoop()
