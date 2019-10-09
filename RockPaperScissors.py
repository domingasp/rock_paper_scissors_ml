###################### Imports ######################
# "random" for computer choices, "time" for delay, "tkinter" for GUI
import random, time
import tkinter as tk

###################### Classes ######################
# Initialises the GUI for the application. Allows manipulation of the GUI elements from other parts of the program
class MainGUI:
    def __init__(self, master, gameStats):
        self.master = master
        
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.grid()

        # Displays the human players score
        self.playerScore = tk.Label(self.master, text = "P 0")
        self.playerScore.grid(row = 1, column = 0)

        # Displays the computers score
        self.computerScore = tk.Label(self.master, text = "C 0")
        self.computerScore.grid(row = 1, column = 2)

        # Displays the players choice upon play
        self.playerChoice = tk.Label(self.master, text = "")
        self.playerChoice.grid(row = 2, column = 0)

        # Middle label used to display the initial instruction as well as the "vs" text
        self.vsLabel = tk.Label(self.master, text = "Please choose your weapon.")
        self.vsLabel.grid(row = 2, columnspan = 3)

        # Displays the computers choice upon play
        self.computerChoice = tk.Label(self.master, text = "")
        self.computerChoice.grid(row = 2, column = 2)

        # Displays the result of the current play
        self.resultLabel = tk.Label(self.master, text = "Not started.")
        self.resultLabel.grid(row = 3, columnspan = 3)

        # Create Rock, Paper, Scissors buttons for play
        self.rockButton = tk.Button(self.master, text = "Rock", width = 10, height = 2, command = lambda: playGame(self, 0, gameStats))
        self.rockButton.grid(row = 4, column = 0)

        self.paperButton = tk.Button(self.master, text = "Paper", width = 10, height = 2, command = lambda: playGame(self, 1, gameStats))
        self.paperButton.grid(row = 4, column = 1)

        self.scissorsButton = tk.Button(self.master, text = "Scissors", width = 10, height = 2, command = lambda: playGame(self, 2, gameStats))
        self.scissorsButton.grid(row = 4, column = 2)

# Class to keep track of the current number of games the user and computer have won
class GameStats:
    def __init__(self):
        self.userWon = 0
        self.computerWon = 0


###################### Functionality ######################
# Plays a round of the game
def playGame(gui, usersGo, stats):
    gui.rockButton["state"] = "disabled"
    gui.paperButton["state"] = "disabled"
    gui.scissorsButton["state"] = "disabled"

    # Generates the computers go
    computersGo = random.randint(0, 2)

    # Choices used when displaying in the GUI
    weapons = ["Rock", "Paper", "Scissors"]

    # Sets the "vs" label text to be empty and spanning only 1 column in prepation of the choices being displayed
    gui.vsLabel["text"] = ""
    gui.vsLabel.grid(row = 2, column = 1, columnspan = 1)

    # Sets both choice labels to "Rock" as if playing with humans who say "Rock, Paper, Scissors" as they play
    # Timer to delay the next action of the game to allow the user time to see what is happening
    gui.playerChoice["text"] = "Rock"
    gui.computerChoice["text"] = "Rock"
    gui.master.update()
    time.sleep(0.6)

    # Sets both choice labels to "Paper" as if playing with humans who say "Rock, Paper, Scissors" as they play
    # Timer to delay the next action of the game to allow the user time to see what is happening
    gui.playerChoice["text"] = "Paper"
    gui.computerChoice["text"] = "Paper"
    gui.master.update()
    time.sleep(0.6)

    # Sets the choice labels and the "vs" label to result in "$Player vs $Computer" being displayed with $Player and $Computer being the choices
    gui.vsLabel["text"] = "vs"
    gui.playerChoice["text"] = str(weapons[usersGo])
    gui.computerChoice["text"] = str(weapons[computersGo])

    # Checks whether the game is a tie
    if (usersGo == computersGo):
        gui.resultLabel["text"] = "A Tie"
    # If not a tie check the different combinations
    else:
        # 0 : Rock
        # 1 : Paper
        # 2 : Scissors
        # Checks who the winner is and updates the stats class variables to reflect the new stats
        if (usersGo == 0):
            if (computersGo == 2):
                gui.resultLabel["text"] = "You Won"
                stats.userWon += 1
            else:
                gui.resultLabel["text"] = "You Lost"
                stats.computerWon += 1
        elif (usersGo == 1):
            if (computersGo == 0):
                gui.resultLabel["text"] = "You Won"
                stats.userWon += 1
            else:
                gui.resultLabel["text"] = "You Lost"
                stats.computerWon += 1
        if (usersGo == 2):
            if (computersGo == 1):
                gui.resultLabel["text"] = "You Won"
                stats.userWon += 1
            else:
                gui.resultLabel["text"] = "You Lost"
                stats.computerWon += 1

    # Sets the player and computer score labels to reflect the new scores
    gui.playerScore["text"] = "P " + str(stats.userWon)
    gui.computerScore["text"] = "C " + str(stats.computerWon)

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