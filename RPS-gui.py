

#1. import tkinter
import tkinter as tk

# create randomization
import random

#2. define custom class name as RPscounter
class RPscounter(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Rock, Paper, Scissors: The Game That Saved the Galaxy")
      
 #3. create Rock, Paper Scissors choices
    self.choices = ["Rock", "Paper", "Scissors"]

#4. create game logic
    self.userChoice = tk.StringVar()
    self.computerChoice = tk.StringVar()
    self.results = tk.StringVar()
    self.wins = tk.StringVar()
    self.games = tk.StringVar()
    self.userScore = 0
    self.computerScore = 0
    self.totalRounds = 0
    self.maxRounds = 5
    self.createWidgets()
    self.gameReset()

#5. create and place widgets and shapes
  def createWidgets(self):
  #title instructions and labels
    #title
    self.title_label = tk.Label(self, text="Rock, Paper, Scissors: The Game That Saved the Galaxy")
    self.title_label.grid(row=0, column=0, columnspan=5)
    #subtitle instrustions
    self.instructions_label = tk.Label(self, text="Hitchhiker, Deep Thought challenges you to rock, paper, scissors. Beat it 5 times and get the Ultimate Answer. Ready?")
    self.instructions_label.grid(row=1, column=0, columnspan=3)
    #User
    tk.Label(self, text="You Chose:").grid(row=4, column=0, sticky="w")
    tk.Label(self, textvariable=self.userChoice).grid(row=4, column=1)
    #Computer
    tk.Label(self, text="Deep Thought Chose:").grid(row=5, column=0, sticky="w")
    tk.Label(self, textvariable=self.computerChoice).grid(row=5, column=1)
    #Results
    tk.Label(self, text="Result:").grid(row=6, column=0, sticky="w")
    tk.Label(self, textvariable=self.results).grid(row=6, column=1)
    #add reset button
    tk.Button(self, text="Reset", command=self.gameReset).grid(row=7,column=1)
    #add copyright for Hitchhiker's Guid to the Galaxy
    self.space = tk.Label(self, text="")
    self.space.grid(row=8, column=0, columnspan=5)
    self.copyright1 = tk.Label(self, text="Game based on Deep Thought from The Hitchhiker's Guide to the Galaxy copyright D. Adams")
    self.copyright1.grid(row=9, column=0, columnspan=5)
    self.copyright2 = tk.Label(self, text="No infriengement intended. For educational use only. Not affiliated or endorsed by author or publisher.")
    self.copyright2.grid(row=10, column=0, columnspan=5)
    self.space = tk.Label(self, text="")
    self.space.grid(row=11, column=0, columnspan=5)
#6. widgets for rock, paper, scissors
    #rock
    rockShape_label = tk.Label(self, text="Rock").grid(row=2, column=0)
    rockShape = tk.Canvas(self, width=50, height=50)
    rockShape.create_oval(10, 10, 40, 40, fill='light salmon', outline='black')
    rockShape.grid(row=3, column=0)
    rockShape.bind('<Button-1>', lambda event:     self.play("Rock"))
    #paper
    paperShape_label = tk.Label(self, text="Paper").grid(row=2, column=1)
    paperShape = tk.Canvas(self, width=50, height=50)
    paperShape.create_rectangle(10, 10, 40, 40, fill='white', outline='black')
    paperShape.grid(row=3, column=1)
    paperShape.bind('<Button-1>', lambda event: self.play("Paper"))
    #scissors
    scissorShape_label = tk.Label(self, text="Scissors").grid(row=2, column=2)
    scissorShape = tk.Canvas(self, width=50, height=50)
    scissorShape.create_polygon(10, 40, 40, 40, 25, 10, fill='light sky blue', outline='black')
    scissorShape.grid(row=3, column=2)
    scissorShape.bind('<Button-1>', lambda event: self.play("Scissors"))
  #define game reset
  def gameReset(self):
    #score tally
    self.userChoice.set("")
    self.computerChoice.set("")
    self.results.set("")
    self.userScore = 0
    self.computerScore = 0
    self.totalRounds = 0
    
#9. Set and define game play
  def play(self, userChoice):
    if self.totalRounds < self.maxRounds:
        self.userChoice.set(userChoice)
        computerChoice = random.choice(self.choices)
        self.computerChoice.set(computerChoice)

        #9.1 if tie no winner value 0
        if userChoice == computerChoice:
            self.results.set("Don't Panic! It's a Tie!")

        #9.2 of not a tie print winner of round
        #user wins
        elif (userChoice == "Rock" and computerChoice == "Scissors") or \
            (userChoice == "Scissors" and computerChoice == "Paper") or \
            (userChoice == "Paper" and computerChoice == "Rock"):
            self.results.set("You win this round!")
            self.userScore += 1

        #computer wins
        else:
            self.results.set("Deep Thought wins this round!")
            self.computerScore += 1
        self.totalRounds += 1

#10. Announce winner after 5 rounds. If Tie no winners
    if self.totalRounds == self.maxRounds:
        if self.userScore > self.computerScore:
            self.results.set("You win! The Ultimate Answer to Life, Everything, and the Universe is 42!")
        elif self.userScore < self.computerScore:
            self.results.set("End of the Galaxy. Computer wins!")
        else:
            self.results.set("A Tie! Reset the Galaxy!")
          
#11. Tally Counter
    #WINS
    tk.Label(self, text="Wins:").grid(row=13, column=0, sticky="w")
    tk.Label(self, textvariable=self.wins).grid(row=13, column=0)
    self.wins.set(self.userScore)
    #Game Number
    tk.Label(self, text="Games:").grid(row=13, column=2, sticky="w")
    tk.Label(self, textvariable=self.games).grid(row=13, column=2)
    self.games.set(self.totalRounds)
#12. End of program
if __name__ == "__main__":
    app = RPscounter()
    app.mainloop()