import sys

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


