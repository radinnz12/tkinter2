import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create the game board
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Button(master, text="", width=5, height=2, command=lambda row=i, col=j: self.on_click(row, col))
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        self.current_player = "X"
        self.game_over = False

    def on_click(self, row, col):
        if not self.game_over and self.cells[row][col]["text"] == "":
            self.cells[row][col]["text"] = self.current_player
            self.check_win()
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for row in self.cells:
            if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
                self.declare_winner(row[0]["text"])
                return

        # Check columns
        for i in range(3):
            if self.cells[0][i]["text"] == self.cells[1][i]["text"] == self.cells[2][i]["text"] != "":
                self.declare_winner(self.cells[0][i]["text"])
                return

        # Check diagonals
        if self.cells[0][0]["text"] == self.cells[1][1]["text"] == self.cells[2][2]["text"] != "":
            self.declare_winner(self.cells[0][0]["text"])
            return
        if self.cells[0][2]["text"] == self.cells[1][1]["text"] == self.cells[2][0]["text"] != "":
            self.declare_winner(self.cells[0][2]["text"])
            return

        # Check for a tie
        if all(cell["text"] != "" for row in self.cells for cell in row):
            self.declare_winner("Tie")

    def declare_winner(self, winner):
        self.game_over = True
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()