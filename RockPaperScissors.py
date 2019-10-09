<<<<<<< HEAD
import random
import tkinter as tk

class MainGUI:
    def __init__(self, master):
        self.master = master
        
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.grid()

        self.playerScore = tk.Label(self.master, text = "P 0/3")
        self.playerScore.grid(row = 1, column = 0)

        self.computerScore = tk.Label(self.master, text = "C 0/3")
        self.computerScore.grid(row = 1, column = 2)

        self.playerChoices = tk.Label(self.master, text = "Please choose your weapon.")
        self.playerChoices.grid(row = 2, columnspan = 3)

        self.resultLabel = tk.Label(self.master, text = "Not started.")
        self.resultLabel.grid(row = 3, columnspan = 3)

        self.rockButton = tk.Button(self.master, text = "Rock", width = 10, height = 2, command = lambda: playGame(self, 0))
        self.rockButton.grid(row = 4, column = 0)

        self.paperButton = tk.Button(self.master, text = "Paper", width = 10, height = 2, command = lambda: playGame(self, 1))
        self.paperButton.grid(row = 4, column = 1)

        self.scissorsButton = tk.Button(self.master, text = "Scissors", width = 10, height = 2, command = lambda: playGame(self, 2))
        self.scissorsButton.grid(row = 4, column = 2)

        

def playGame(gui, usersGo):
    computersGo = random.randint(0, 2)

    weapons = ["Rock", "Paper", "Scissors"]

    gui.playerChoices["text"] = str(weapons[usersGo]) + " v " + str(weapons[computersGo])

    if (usersGo == computersGo):
        gui.resultLabel["text"] = "A Tie"
    else:
        if (usersGo == 0):
            if (computersGo == 2):
                gui.resultLabel["text"] = "You Won"
            else:
                gui.resultLabel["text"] = "You Lost"
        elif (usersGo == 1):
            if (computersGo == 0):
                gui.resultLabel["text"] = "You Won"
            else:
                gui.resultLabel["text"] = "You Lost"
        if (usersGo == 2):
            if (computersGo == 1):
                gui.resultLabel["text"] = "You Won"
            else:
                gui.resultLabel["text"] = "You Lost"

def main():
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
=======
import random
import tkinter as tk

class MainGUI:
    def __init__(self, master, gameStats):
        self.master = master
        
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.grid()

        self.playerScore = tk.Label(self.master, text = "P 0")
        self.playerScore.grid(row = 1, column = 0)

        self.computerScore = tk.Label(self.master, text = "C 0")
        self.computerScore.grid(row = 1, column = 2)

        self.playerChoices = tk.Label(self.master, text = "Please choose your weapon.")
        self.playerChoices.grid(row = 2, columnspan = 3)

        self.resultLabel = tk.Label(self.master, text = "Not started.")
        self.resultLabel.grid(row = 3, columnspan = 3)

        self.rockButton = tk.Button(self.master, text = "Rock", width = 10, height = 2, command = lambda: playGame(self, 0, gameStats))
        self.rockButton.grid(row = 4, column = 0)

        self.paperButton = tk.Button(self.master, text = "Paper", width = 10, height = 2, command = lambda: playGame(self, 1, gameStats))
        self.paperButton.grid(row = 4, column = 1)

        self.scissorsButton = tk.Button(self.master, text = "Scissors", width = 10, height = 2, command = lambda: playGame(self, 2, gameStats))
        self.scissorsButton.grid(row = 4, column = 2)

class GameStats:
    def __init__(self):
        self.userWon = 0
        self.computerWon = 0

def playGame(gui, usersGo, stats):
    computersGo = random.randint(0, 2)

    weapons = ["Rock", "Paper", "Scissors"]

    gui.playerChoices["text"] = str(weapons[usersGo]) + " v " + str(weapons[computersGo])

    if (usersGo == computersGo):
        gui.resultLabel["text"] = "A Tie"
    else:
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

    gui.playerScore["text"] = "P " + str(stats.userWon)
    gui.computerScore["text"] = "C " + str(stats.computerWon)

def main():
    root = tk.Tk()
    gameStats = GameStats()
    app = MainGUI(root, gameStats)
    root.mainloop()

if __name__ == "__main__":
>>>>>>> Keep score of how many games the user and computer have won; update the label to reflect the score
    main()