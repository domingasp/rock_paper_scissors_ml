###################### Imports ######################
# "random" for computer choices, "time" for delay, "tkinter" for GUI,
# os for file paths, Font to initialise application font,
# Image and ImageTk for loading and resizing images
import random, time, os
import tkinter as tk
from tkinter.font import Font

from PIL import Image, ImageTk

###################### Classes ######################
# Initialises the GUI for the application. Allows manipulation of the GUI elements from other parts of the program
class MainGUI:
    def __init__(self, master, gameStats, computerBrain):
        self.master = master
        
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.grid()

        # Initialise the font used for the game
        self.topFont = Font(family = "Arial", size = 12)

        # Displays the human players score
        self.playerLabel = tk.Label(self.master, text = "Player", font = self.topFont)
        self.playerLabel.grid(row = 1, column = 0)
        self.playerScore = tk.Label(self.master, text = "0", font = self.topFont)
        self.playerScore.grid(row = 2, column = 0)

        # Displays the computers score
        self.computerLabel = tk.Label(self.master, text = "Computer", font = self.topFont)
        self.computerLabel.grid(row = 1, column = 2)
        self.computerScore = tk.Label(self.master, text = "0", font = self.topFont)
        self.computerScore.grid(row = 2, column = 2)

        # Displays the players choice upon play
        self.playerChoice = tk.Label(self.master)
        self.playerChoice.grid(row = 3, column = 0)

        # Displays the computers choice upon play
        self.computerChoice = tk.Label(self.master)
        self.computerChoice.grid(row = 3, column = 2)

        # Middle label used to display the initial instruction as well as the result image
        self.resultLabel = tk.Label(self.master, text = "Please choose your weapon.", font = self.topFont)
        self.resultLabel.grid(row = 3, columnspan = 3)

        # Add label images at desired size
        self.winLabelImage = resizeImage(os.path.join("images", "win_label.png"), 45, 45)
        self.loseLabelImage = resizeImage(os.path.join("images", "lose_label.png"), 45, 45)
        self.tieLabelImage = resizeImage(os.path.join("images", "tie_label.png"), 45, 45)
        self.rockLabelImage = resizeImage(os.path.join("images", "rock_label.png"), 60, 60)
        self.paperLabelImage = resizeImage(os.path.join("images", "paper_label.png"), 60, 60)
        self.scissorsLabelImage = resizeImage(os.path.join("images", "scissors_label.png"), 60, 60)

        # Adds the images at the desired size as variables that can be used by the buttons
        self.rockButtonImage = resizeImage(os.path.join("images", "rock_button.png"), 75, 75)
        self.paperButtonImage = resizeImage(os.path.join("images", "paper_button.png"), 75, 75)
        self.scissorsButtonImage = resizeImage(os.path.join("images", "scissors_button.png"), 75, 75)

        # Create Rock, Paper, Scissors buttons for play (highlightthickness and bd are used to remove the default background from the buttons)
        self.rockButton = tk.Button(self.master, image = self.rockButtonImage, command = lambda: playGame(self, 0, gameStats, computerBrain), highlightthickness = 0, bd = 0)
        self.rockButton.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.paperButton = tk.Button(self.master, image = self.paperButtonImage, command = lambda: playGame(self, 1, gameStats, computerBrain), highlightthickness = 0, bd = 0)
        self.paperButton.grid(row = 5, column = 1, pady = 10)

        self.scissorsButton = tk.Button(self.master, image = self.scissorsButtonImage, command = lambda: playGame(self, 2, gameStats, computerBrain), highlightthickness = 0, bd = 0)
        self.scissorsButton.grid(row = 5, column = 2, padx = 10, pady = 10)

# Class to keep track of the current number of games the user and computer have won
class GameStats:
    def __init__(self):
        self.userWon = 0
        self.computerWon = 0

# Class to keep track of previous two goes of the computer and the player and determine which choice is likely to win
class ComputerBrain:
    def __init__(self):
        # Keeps track of the players and computers previous two choices
        # ...Go1 represents the previous go
        # ...Go2 represents the go before ...Go1
        self.previousComputerGo1 = -1
        self.previousComputerGo2 = -1
        self.previousPlayerGo1 = -1
        self.previousPlayerGo2 = -1

        # Keeps track if the previous go the computer won or lost
        # 0 = Lost
        # 1 = Won
        self.previousResult = -1

    # Determines which weapon the computer should choose
    def chooseWeapon(self, computerGo1, computerGo2, playerGo1, playerGo2, previousResult):
        probabilityList = [0] * 33 + [1] * 33 + [2] * 33

        # If no goes have been played
        if (computerGo1 == -1 or playerGo1 == -1):
            probabilityList = [0] * 50 + [1] * 20 + [2] * 30
        # 2+ go
        else:
            # If the last 2 user goes were the same the user is unlikely to play the same move again
            if (playerGo1 == playerGo2):
                # If player choices were rock
                if (playerGo1 == 0):
                    probabilityList = [0] * 15 + [1] * 35 + [2] * 50
                # If player choices were paper
                elif (playerGo1 == 1):
                    probabilityList = [0] * 50 + [1] * 15 + [2] * 35
                # If player choices were scissors
                elif (playerGo1 == 2):
                    probabilityList = [0] * 35 + [1] * 50 + [2] * 15
            # If computer lost last game
            elif (previousResult == 0):
                # If player chose rock to win
                if (playerGo1 == 0):
                    probabilityList = [0] * 50 + [1] * 20 + [2] * 30
                # If player chose paper to win
                elif (playerGo1 == 1):
                    probabilityList = [0] * 30 + [1] * 50 + [2] * 20
                # If player chose scissors to win
                elif (playerGo1 == 2):
                    probabilityList = [0] * 20 + [1] * 35 + [2] * 45
            # Last 2 goes have not been equal and computer won the last game
            else:
                # Computer last 2 goes were the same
                if (computerGo1 == computerGo2):
                    # If player choices were rock
                    if (computerGo1 == 0):
                        probabilityList = [0] * 20 + [1] * 40 + [2] * 40
                    # If player choices were paper
                    elif (computerGo1 == 1):
                        probabilityList = [0] * 40 + [1] * 20 + [2] * 40
                    # If player choices were scissors
                    elif (computerGo1 == 2):
                        probabilityList = [0] * 40 + [1] * 40 + [2] * 20
                # Last 2 computer goes were not equal
                else:
                    # If player chose previously rock
                    if (computerGo1 == 0):
                        probabilityList = [0] * 20 + [1] * 40 + [2] * 40
                    # If player chose previously paper
                    elif (computerGo1 == 1):
                        probabilityList = [0] * 40 + [1] * 20 + [2] * 40
                    # If player chose previously scissors
                    elif (computerGo1 == 2):
                        probabilityList = [0] * 40 + [1] * 40 + [2] * 20

        # Return a random choice from the list
        return random.choice(probabilityList)

# filePath is the location of the image , height and width are the required dimensions of the resized image
def resizeImage(filePath, height, width):
        image = Image.open(filePath)
        image = image.resize((height, width), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

###################### Functionality ######################
# Plays a round of the game
def playGame(gui, usersGo, stats, computerBrain):
    gui.rockButton["state"] = "disabled"
    gui.paperButton["state"] = "disabled"
    gui.scissorsButton["state"] = "disabled"

    # Generates the computers go
    computersGo = computerBrain.chooseWeapon(computerBrain.previousComputerGo1, computerBrain.previousComputerGo2, computerBrain.previousPlayerGo1, computerBrain.previousPlayerGo2, computerBrain.previousResult)

    # Choices used when displaying in the GUI
    weapons = [gui.rockLabelImage, gui.paperLabelImage, gui.scissorsLabelImage]

    # Sets the "vs" label text to be empty and the image to be empty and spanning only 1 column in prepation of the choices being displayed
    gui.resultLabel["text"] = ""
    gui.resultLabel["image"] = ""
    gui.resultLabel.grid(row = 3, column = 1, columnspan = 1)

    # Sets both choice labels to rock image as if playing with humans who say "Rock, Paper, Scissors" as they play
    # Timer to delay the next action of the game to allow the user time to see what is happening
    gui.playerChoice["image"] = gui.rockLabelImage
    gui.computerChoice["image"] = gui.rockLabelImage
    gui.master.update()
    time.sleep(0.5)

    # Sets both choice labels to paper image as if playing with humans who say "Rock, Paper, Scissors" as they play
    # Timer to delay the next action of the game to allow the user time to see what is happening
    gui.playerChoice["image"] = gui.paperLabelImage
    gui.computerChoice["image"] = gui.paperLabelImage
    gui.master.update()
    time.sleep(0.5)

    # Sets the choice labels
    gui.playerChoice["image"] = weapons[usersGo]
    gui.computerChoice["image"] = weapons[computersGo]

    # Checks whether the game is a tie
    if (usersGo == computersGo):
        gui.resultLabel["image"] = gui.tieLabelImage
    # If not a tie check the different combinations
    else:
        # 0 : Rock
        # 1 : Paper
        # 2 : Scissors
        # Checks who the winner is and updates the stats class variables to reflect the new stats
        if (usersGo == 0):
            if (computersGo == 2):
                gui.resultLabel["image"] = gui.winLabelImage
                stats.userWon += 1
                computerBrain.previousResult = 0
            else:
                gui.resultLabel["image"] = gui.loseLabelImage
                stats.computerWon += 1
                computerBrain.previousResult = 1
        elif (usersGo == 1):
            if (computersGo == 0):
                gui.resultLabel["image"] = gui.winLabelImage
                stats.userWon += 1
                computerBrain.previousResult = 0
            else:
                gui.resultLabel["image"] = gui.loseLabelImage
                stats.computerWon += 1
                computerBrain.previousResult = 1
        if (usersGo == 2):
            if (computersGo == 1):
                gui.resultLabel["image"] = gui.winLabelImage
                stats.userWon += 1
                computerBrain.previousResult = 0
            else:
                gui.resultLabel["image"] = gui.loseLabelImage
                stats.computerWon += 1
                computerBrain.previousResult = 1

    # Sets the player and computer score labels to reflect the new scores
    gui.playerScore["text"] = str(stats.userWon)
    gui.computerScore["text"] = str(stats.computerWon)

    # Update computer brains memory to store the latest two turns
    computerBrain.previousComputerGo2 = computerBrain.previousComputerGo1
    computerBrain.previousComputerGo1 = computersGo
    computerBrain.previousPlayerGo2 = computerBrain.previousPlayerGo1
    computerBrain.previousPlayerGo1 = usersGo

    # Re-enables the bottom 3 buttons to allow the user to play again
    gui.rockButton["state"] = "normal"
    gui.paperButton["state"] = "normal"
    gui.scissorsButton["state"] = "normal"

###################### Start application ######################
def main():
    # Initialises the root, the GameStats class and the MainGUI class
    root = tk.Tk()
    gameStats = GameStats()
    computerBrain = ComputerBrain()
    app = MainGUI(root, gameStats, computerBrain)
    root.mainloop()

# Runs the main function on start
if __name__ == "__main__":
    main()