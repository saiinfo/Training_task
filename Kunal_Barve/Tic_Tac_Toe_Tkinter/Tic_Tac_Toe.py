import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        #initializing required parameters
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.label = tk.Label(self.root ,text = f"Player {self.current_player}'s  turn" ,font = ("normal",16))
        self.create_board()
        
    def create_board(self):
        # create the board of size 3 x3 
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        self.label.grid(row=3, column=0, columnspan=3)
    def click(self, row, col):
        #On click 
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()
    
    def switch_player(self):
        # switching the player
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s turn")
    
    def check_win(self):
        # checking horizontal ,vertical and diagonal condition
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False
    
    def check_draw(self):
        # check if there is any empty cell
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True
    
    def reset_board(self):
        # reset the board
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text="")
        self.current_player = "X"
    
    def run(self):
        # continuously listen to the event
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
