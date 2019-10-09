import random, time
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

        self.playerChoice = tk.Label(self.master, text = "")
        self.playerChoice.grid(row = 2, column = 0)

        self.vsLabel = tk.Label(self.master, text = "Please choose your weapon.")
        self.vsLabel.grid(row = 2, columnspan = 3)

        self.computerChoice = tk.Label(self.master, text = "")
        self.computerChoice.grid(row = 2, column = 2)

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
    gui.rockButton["state"] = "disabled"
    gui.paperButton["state"] = "disabled"
    gui.scissorsButton["state"] = "disabled"

    computersGo = random.randint(0, 2)

    weapons = ["Rock", "Paper", "Scissors"]

    gui.vsLabel["text"] = ""
    gui.vsLabel.grid(row = 2, column = 1, columnspan = 1)

    gui.playerChoice["text"] = "Rock"
    gui.computerChoice["text"] = "Rock"
    gui.master.update()
    time.sleep(0.6)

    gui.playerChoice["text"] = "Paper"
    gui.computerChoice["text"] = "Paper"
    gui.master.update()
    time.sleep(0.6)

    gui.vsLabel["text"] = "vs"
    gui.playerChoice["text"] = str(weapons[usersGo])
    gui.computerChoice["text"] = str(weapons[computersGo])

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

    gui.rockButton["state"] = "normal"
    gui.paperButton["state"] = "normal"
    gui.scissorsButton["state"] = "normal"

def main():
    root = tk.Tk()
    gameStats = GameStats()
    app = MainGUI(root, gameStats)
    root.mainloop()

if __name__ == "__main__":
    main()