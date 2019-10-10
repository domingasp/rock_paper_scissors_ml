###################### Imports ######################
# "random" for computer choices, "time" for delay, "tkinter" for GUI
import random, time, os
import tkinter as tk
from tkinter.font import Font

from PIL import Image, ImageTk

###################### Classes ######################
# Initialises the GUI for the application. Allows manipulation of the GUI elements from other parts of the program
class MainGUI:
    def __init__(self, master, gameStats):
        self.master = master
        
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.grid()

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

        # Middle label used to display the initial instruction as well as the "vs" text
        self.resultLabel = tk.Label(self.master, text = "Please choose your weapon.", font = self.topFont)
        self.resultLabel.grid(row = 3, columnspan = 3)

        # Add label images at desired size
        self.winLabelImage = resizeImage(os.path.join("images", "win_label.png"), 45, 45)
        self.loseLabelImage = resizeImage(os.path.join("images", "lose_label.png"), 60, 60)
        self.tieLabelImage = resizeImage(os.path.join("images", "tie_label.png"), 60, 60)
        self.rockLabelImage = resizeImage(os.path.join("images", "rock_label.png"), 60, 60)
        self.paperLabelImage = resizeImage(os.path.join("images", "paper_label.png"), 60, 60)
        self.scissorsLabelImage = resizeImage(os.path.join("images", "scissors_label.png"), 60, 60)

        # Adds the images at the desired size as variables that can be used by the buttons
        self.rockButtonImage = resizeImage(os.path.join("images", "rock_button.png"), 75, 75)
        self.paperButtonImage = resizeImage(os.path.join("images", "paper_button.png"), 75, 75)
        self.scissorsButtonImage = resizeImage(os.path.join("images", "scissors_button.png"), 75, 75)

        # Create Rock, Paper, Scissors buttons for play (highlightthickness and bd are used to remove the default background from the buttons)
        self.rockButton = tk.Button(self.master, image = self.rockButtonImage, command = lambda: playGame(self, 0, gameStats), highlightthickness = 0, bd = 0)
        self.rockButton.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.paperButton = tk.Button(self.master, image = self.paperButtonImage, command = lambda: playGame(self, 1, gameStats), highlightthickness = 0, bd = 0)
        self.paperButton.grid(row = 5, column = 1, pady = 10)

        self.scissorsButton = tk.Button(self.master, image = self.scissorsButtonImage, command = lambda: playGame(self, 2, gameStats), highlightthickness = 0, bd = 0)
        self.scissorsButton.grid(row = 5, column = 2, padx = 10, pady = 10)

# Class to keep track of the current number of games the user and computer have won
class GameStats:
    def __init__(self):
        self.userWon = 0
        self.computerWon = 0

# filePath is the location of the image , height and width are the required dimensions of the resized image
def resizeImage(filePath, height, width):
        image = Image.open(filePath)
        image = image.resize((height, width), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

###################### Functionality ######################
# Plays a round of the game
def playGame(gui, usersGo, stats):
    gui.rockButton["state"] = "disabled"
    gui.paperButton["state"] = "disabled"
    gui.scissorsButton["state"] = "disabled"

    # Generates the computers go
    computersGo = random.randint(0, 2)

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
            else:
                stats.computerWon += 1
                gui.resultLabel["image"] = gui.loseLabelImage
        elif (usersGo == 1):
            if (computersGo == 0):
                gui.resultLabel["image"] = gui.winLabelImage
                stats.userWon += 1
            else:
                stats.computerWon += 1
                gui.resultLabel["image"] = gui.loseLabelImage
        if (usersGo == 2):
            if (computersGo == 1):
                gui.resultLabel["image"] = gui.winLabelImage
                stats.userWon += 1
            else:
                stats.computerWon += 1
                gui.resultLabel["image"] = gui.loseLabelImage

    # Sets the player and computer score labels to reflect the new scores
    gui.playerScore["text"] = str(stats.userWon)
    gui.computerScore["text"] = str(stats.computerWon)

    # Re-enables the bottom 3 buttons to allow the user to play again
    gui.rockButton["state"] = "normal"
    gui.paperButton["state"] = "normal"
    gui.scissorsButton["state"] = "normal"

###################### Start application ######################
def main():
    # Initialises the root, the GameStats class and the MainGUI class
    root = tk.Tk()
    gameStats = GameStats()
    app = MainGUI(root, gameStats)
    root.mainloop()

# Runs the main function on start
if __name__ == "__main__":
    main()