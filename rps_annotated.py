class Game:
    def __init__(self, newPlayerName):
		#Define and set properties for the class
		self.playerName = newPlayerName
        self.playerHand = "NA"
        self.botHand = "NA"
        self.winner = "NA"
		#Print out a message so we know when the constructor has run
        print("New instance of game class for " + self.playerName)

	#Note: This function was copied and only modified to work in our class. 
	#We are going to work on cleaning this up and improving our Game class in future videos.
    def runGame(self):
        if ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 1):
            self.winner = 'You win'
        elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 2):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 3):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 1):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 2):
            self.winner = 'You win!'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 3):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 1):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 2):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 3):
            self.winner = 'You win!'
        else:
            self.winner = 'INVALID input, try again'


def main():
	#Create a new instance of our game by calling the constructor for the game class.
    myGame = Game('Kevin')
	#Print all the variables in the object by using the instance 'myGame' and the '.' dot to acess methods
	#and variables beloning to that object (instance).
	print(myGame.playerName)
    print(myGame.winner)
    print(myGame.botHand)
    print(myGame.playerHand)

	#Set the hand of the bod and player using the '.' and the assignment operator '='.
	#Works just like any other variable except these variables are contained within our object.
	#Think of these variables living inside the 'myGame' box.
    myGame.botHand = 1
    myGame.playerHand = 'paper'
	#Run our runGame method. The winner will be set in myGame.winner so we can then print it
    myGame.runGame()
    print(myGame.winner)
	
	#Create another instance of Game (to show that we can)
	otherGame = Game('Zibzo')
	#Run the other game
	otherGame.runGame()
	#This should print invalid input as we never set the player/bot hands
	print(otherGame.winner)