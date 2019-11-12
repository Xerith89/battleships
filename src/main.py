import sys
import board as brd
import opponent

gameRunning = True

welcomeMessage = """Welcome to BattleShips!
Choose either (N)ew Game or (Q)uit."""
print(welcomeMessage)

menuSelection = input()

if menuSelection == 'Q' or menuSelection == 'q':
    print("Goodbye.")
    gameRunning = False
elif menuSelection == 'N' or menuSelection == 'n':
    print("New game starting....")
else:
    print("Command not valid.")

# Set up board
board = brd.Board()
board.init_board()

opponent = opponent.Opponent()
   
while gameRunning:
    # print board
    board.print_board()
    # prompt for input
    gameSelection = input("\nEnter grid position to fire at.\n")
    # handle input
    opponent.checkIfHit(int(gameSelection))
    # check for game over conditions
    if opponent.checkRemainingBoats == 0:
        print("Game Over! You Win.")
        gameRunning = False


