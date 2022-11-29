# For this example, we are going to import the "random" module for generating
# the pseudo-random numbers that will simulate a roulette's behaviour.
import random

# We will create a Roulette class where we are going to define the methods that will generate the outcome for each throw.
class Roulette:
    def __init__(self):
        self.results = []

    # The "throw" method will simulate the roulette's throw, and save a list of booleans that indicate
    # if the result is red or black, high or low, and even or odd. The outcome itself is not stored anywhere.
    def throw(self):
        # We create the list that will be appended to the results list.
        res = []
        # We use randint to generate a random integer between 0 and 36.
        throw = random.randint(0, 36)
        # If the generated number is 0, we save a list that won't pass any of the player's checks.
        if throw == 0:
            res = [2, 2, 2]
        # Else, we create the three booleans.
        else:
            # First, we check if it's red (1) or black (0).
            if throw in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                res.append(1)
            else:
                res.append(0)
                # Then we check if it's high (1) or low (0).
            if throw >= 19:
                res.append(1)
            else:
                res.append(0)
            # And finally, we check if it's even (1) or odd (0).
            if throw % 2 == 0:
                res.append(1)
            else:
                res.append(0)
        # Once the list is ready, we append it to the results list.
        self.results.append(res)

# We will also create the Player class, that will store each player's balance and their rules for betting.
class Player:
    def __init__(self, bettingPosition, bettingBoolean):
        # The balance starts at zero, and each consecutive bet will modify it.
        self.balance = 0
        # The sum of the first and last elements of the bettingList define how much does the player bet.
        self.bettingList = [1, 2, 3, 4]
        # The bettingPosition attribute indicates what item of the results list should be checked for each player.
        self.bettingPosition = bettingPosition
        # The bettingBoolean attribute indicates what boolean will be looked for in the bettingPosition of the results list.
        self.bettingBoolean = bettingBoolean

    # The "check" method will compare the betting rules previously defined with a specific roulette throw.
    def check(self, res):
        # The player bets the sum of the first and last numbers on the bettingList.
        if len(self.bettingList) > 1:
            bet = self.bettingList[0] + self.bettingList[-1]
        else:
            bet = self.bettingList[0]
        # The bet should also be between 5 and 4000.
        if bet < 5:
            bet = 5
        # If the bet exceeds 4000, the bettingList should be restarted.
        elif bet > 4000:
            bet = 5
            self.bettingList = [1, 2, 3, 4]
        # If the betting criteria is met, the player wins the betted amount, adds it to their balance and updates their bettingList.
        if res[self.bettingPosition] == self.bettingBoolean:
            self.balance += bet
            self.bettingList.append(bet)
        # If the betting criteria isn't met, the player loses its bet, and updates their bettingList.
        else:
            self.balance -= bet
            if len(self.bettingList) <= 2:
                self.bettingList = [1, 2, 3, 4]
            else:
                self.bettingList.pop(0)
                self.bettingList.pop(-1)

# We will also create the Player class, that will store each player's balance and their rules for betting.
class Player:
    def __init__(self, bettingPosition, bettingBoolean):
        # The balance starts at zero, and each consecutive bet will modify it.
        self.balance = 0
        # The sum of the first and last elements of the bettingList define how much does the player bet.
        self.bettingList = [1, 2, 3, 4]
        # The bettingPosition attribute indicates what item of the results list should be checked for each player.
        self.bettingPosition = bettingPosition
        # The bettingBoolean attribute indicates what boolean will be looked for in the bettingPosition of the results list.
        self.bettingBoolean = bettingBoolean

    # The "check" method will compare the betting rules previously defined with a specific roulette throw.
    def check(self, res):
        # The player bets the sum of the first and last numbers on the bettingList.
        if len(self.bettingList) > 1:
            bet = self.bettingList[0] + self.bettingList[-1]
        else:
            bet = self.bettingList[0]
        # The bet should also be between 5 and 4000.
        if bet < 5:
            bet = 5
        # If the bet exceeds 4000, the bettingList should be restarted.
        elif bet > 4000:
            bet = 5
            self.bettingList = [1, 2, 3, 4]
        # If the betting criteria is met, the player wins the betted amount, adds it to their balance and updates their bettingList.
        if res[self.bettingPosition] == self.bettingBoolean:
            self.balance += bet
            self.bettingList.append(bet)
        # If the betting criteria isn't met, the player loses its bet, and updates their bettingList.
        else:
            self.balance -= bet
            if len(self.bettingList) <= 2:
                self.bettingList = [1, 2, 3, 4]
            else:
                self.bettingList.pop(0)
                self.bettingList.pop(-1)

# With both classes ready, we create the instances needed.
roulette = Roulette()
playerA = Player(0, 1)
playerB = Player(0, 0)
playerC = Player(1, 1)
playerD = Player(1, 0)
playerE = Player(2, 1)
playerF = Player(2, 0)

# We will use a for loop to simulate 10.000 roulette throws.
for i in range(1, 10001):
    roulette.throw()
    playerA.check(roulette.results[i-1])
    playerB.check(roulette.results[i-1])
    playerC.check(roulette.results[i-1])
    playerD.check(roulette.results[i-1])
    playerE.check(roulette.results[i-1])
    playerF.check(roulette.results[i-1])

# Finally, we print a brief explanation of the simulation, and then each player's ending balance.
print('This program will simulate a roulette being thrown 10,000 times.')
print('Six players will make simple bets, and each player will always repeat the same bet:')
print('Player A bets for red numbers.')
print('Player B bets for black numbers.')
print('Player C bets for high numbers.')
print('Player D bets for low numbers.')
print('Player E bets for even numbers.')
print('Player F bets for odd numbers.')
print()
print('After 10,000 games:')
print('Player A\'s ending balance is', playerA.balance)
print('Player B\'s ending balance is', playerB.balance)
print('Player C\'s ending balance is', playerC.balance)
print('Player D\'s ending balance is', playerD.balance)
print('Player E\'s ending balance is', playerE.balance)
print('Player F\'s ending balance is', playerF.balance)
print()
print('The global ending balance is', playerA.balance + playerB.balance + playerC.balance + playerD.balance + playerE.balance + playerF.balance)
print()
input('Press any key to exit.')