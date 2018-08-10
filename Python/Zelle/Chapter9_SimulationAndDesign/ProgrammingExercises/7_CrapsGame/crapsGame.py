# crapsGame.py
# A program that simulates a craps dice game. The program estimates the 
# probability of the player winning over a number of games.
"""Craps is a dice game played at many casinos. A player rolls a pair of 
normal six-sided dice. If the initial roll is 2, 3, or 12, the player loses. If
the roll is 7 or 11, the player wins. Any other initial roll causes the player
to "roll for point." That is, the player keeps rolling the dice until either
rolling a 7 or re-rolling the value of the initial roll. If the player re-rolls
the initial value before rolling a 7, it's a win. Rolling a 7 first is a 
loss.
    Write a game to simulate multiple games of craps and estimate the 
probability that the player wins. For example, if the player wins 249 out of 
500 games, then the estimated probability of winning is 249/500 = 0.498."""

from random import randrange

def main():

    printIntro()
    n = getInputs()
    wins = simNGames(n)
    printSummary(wins, n)

def printIntro():

    print("This program simulates the dice game of craps. The player rolls \
two normal six-sided dice. If the initial roll is 2, 3, or 12, the player \
loses. If the roll is 7 or 11, the player wins. Any other initial roll causes \
the player to \"roll for point.\" That is the player keeps rolling the dice \
until either rolling a 7 or re-rolling the value of the intial roll. If the \
player re-rolls the initial value before rolling a 7, it's a win. Rolling a 7 \
before the initial value is a loss.")
    
def getInputs():
    n = 0
    while n < 1:
        try:
            n = int(input("How many craps games to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue
    return n

def simNGames(n):
    # Simulates n games of craps
    # Returns the number of won craps games
    wins = 0
    for i in range(n):
        win = simOneGame()
        if win == True:
            wins = wins + 1
    return wins

def simOneGame():
    # Simulates a game of craps
    # Returns True if the game is won, otherwise False
    # Initialize the first roll
    roll = 1
    dieA = randrange(1,7)
    dieB = randrange(1,7)
    score = dieA + dieB
    initScore = score
    win = True
    playing = True

    while playing == True:
        playing = gameOver(roll, score, initScore)
        # print(score)
        if roll == 1:
            # Test for an initial loss
            if score == 2 or score == 3 or score == 12:
                win = False
                return win
            # Test for an initial win
            elif score == 7 or score == 11:
                win = True
                return win
            else:
                dieA = randrange(1, 7)
                dieB = randrange(1, 7)
                score = dieA + dieB
                roll = roll + 1
        else:
            # Test for a win or loss on "roll for point"
            if score == 7:
                win = False
                return win
            elif score == initScore:
                win = True
                return win
            else:
                dieA = randrange(1, 7)
                dieB = randrange(1, 7)
                score = dieA + dieB
                roll = roll + 1
    return win

def gameOver(roll, score, initScore):
    # Score is the sum of the dice
    # Returns True if the game is over, otherwise False
    if roll == 1:
        # Test for an initial loss
        if score == 2 or score == 3 or score == 12:
            return False
        # Test for an initial win
        if score == 7 or score == 11:
            return False
        else:
            return True
    else:
        # Test for a win or loss on "roll for point"
        if score == 7 or score == initScore:
            return False
        else:
            return True

def printSummary(wins, n):
    # Prints a summary of won games and the percentage of wins
    print("\nGames simulated:", n)
    print("You won {0} games with a win percentage of ({1:0.1%})."\
    .format(wins, wins/n))
        
if __name__ == '__main__': main()
