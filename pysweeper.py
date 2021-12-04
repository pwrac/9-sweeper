# /pysweeper-tkinter/pysweeper.py
# pysweeper by Aidan Clark

## TODO ##
# TK: Include display for flags and time
# TK: Add buttons for reset or new game
# Add and complete win condition
# Complete lose condition

from random import randint
from tkinter import *
import time

class pysweeper:

    def __init__(self):
        self.row, self.col, self.bombs = self.ask()
        self.flags = self.bombs
        self.items, self.vlayer = self.generate_boards(self.row, self.col, self.bombs)
        # Items board contains bombs and number values
        # vlayer board determines whether a cell is unswept (2), flagged (1), or revealed (0)

        self.cell = [[]] ## IMPORTANT: Cells are retrieved with self.cell[column][row]
        self.cell_size = 25

        self.running = False
        self.time = 0

        self.rt = Tk()
        self.x = self.col*self.cell_size
        self.y = self.row*self.cell_size
        self.reset_btn = Button(self.rt, text='Reset', command=lambda:self.restart())
        self.flag_lbl = Label(self.rt, text=f"Flags: {self.flags}")
        self.time_lbl = Label(self.rt, text=f"{self.time:03}")

        self.reset_btn = Button(self.rt, text='Reset', command=lambda : self.restart())
        self.flag_lbl = Label(self.rt, text=f"Flags: {self.flags}")
        self.time_lbl = Label(self.rt, text=f"{self.time:03}")

        self.rt.title('pysweeper')
        self.rt.geometry(f"{self.x}x{self.y+2*self.cell_size}")
        self.rt.resizable(0, 0)

        self.cellSetup()
        self.window()
        self.rt.mainloop()

    ### INIT FUNCTIONS ###
    def ask(self):
        diff = int(input("Select a difficulty: [0=Easy, 1=Intermediate, 2=Expert, 3=Custom]\n>> "))
        if diff == 0:
            rows, columns, bombs = 9, 9, 10
        if diff == 1:
            rows, columns, bombs = 16, 16, 40
        if diff == 2:
            rows, columns, bombs = 16, 30, 99
        if diff == 3:
            columns = int(input("Width:\n>> "))
            rows = int(input("Height:\n>> "))
            bombs = int(input("Amount of Bombs:\n>> "))
<<<<<<< HEAD
=======
        self.running = True
>>>>>>> 6a79ecbb83351688da1391bdea8c05846a468463
        return rows, columns, bombs

    def generate_boards(self, row, col, bombs):
        arr1 = [[0 for _ in range(col)] for _ in range(row)]
        arr2 = [[2 for _ in range(col)] for _ in range(row)]
        b_placed = 0
        while b_placed < bombs:
            rand_row = randint(0, row-1)
            rand_col = randint(0, col-1)
            if arr1[rand_row][rand_col] == 9:
                continue
            arr1[rand_row][rand_col] = 9
            b_placed += 1

        for r in range(row):
            for c in range(col):
                if arr1[r][c] == 9:
                    continue
                arr1[r][c] = self.count(arr1, r, c)
        return arr1, arr2

    def count(self, arr, row, col):
        prox = 0
        for r in range(max(0, row-1), min(self.row-1, (row+1))+1):
            for c in range(max(0, col-1), min(self.col-1, (col+1))+1):
                if c == col and r == row:
                    continue
                if arr[r][c] == 9:
                    prox += 1
        return prox

    def cellSetup(self):
        # column/row loop order reversed due to how tkinter places buttons
        # Refer to important warnint on line 13 on retrieving cells
        for r in range(self.col):
            self.cell.append([])
            for c in range(self.row):
                self.cell[r].append(Button(self.rt))
                self.cell[r][c].place(x=r*self.cell_size, y=c*self.cell_size, width=self.cell_size, height=self.cell_size)

        self.reset_btn.place(x=0, y=self.y+self.cell_size, width=2*self.cell_size, height=self.cell_size)
        self.flag_lbl.place(anchor=NE, y=self.y+self.cell_size, x=self.x, width=3*self.cell_size, height=self.cell_size)
        self.time_lbl.place(anchor=N, y=self.y+self.cell_size, x=int(self.x/2), width=2*self.cell_size, height=self.cell_size)

    ### GAME FUNTIONS ###
    def sweep(self, row, col):
        self.vlayer[row][col] = 0
        if self.items[row][col] == 9: # Lose Condition: Clicking a bomb
            return False
        if self.items[row][col] > 0: # Do not sweep surrounding cells
            return True
        for r in range(max(0, row-1), min(self.row-1, (row+1))+1):
            for c in range(max(0, col-1), min(self.col-1, (col+1))+1):
                if self.vlayer[r][c] == 0: # If cell is already swept or flagged, ignore
                    continue
                if self.vlayer[r][c] == 1:
                    continue
                self.sweep(r, c)
        return True

    def handle_left_click(self):
        if not self.running:
<<<<<<< HEAD
            print("Running")
=======
>>>>>>> 6a79ecbb83351688da1391bdea8c05846a468463
            self.running = True

        ix = (self.rt.winfo_pointerx() - self.rt.winfo_rootx()) // self.cell_size # Column Index
        iy = (self.rt.winfo_pointery() - self.rt.winfo_rooty()) // self.cell_size # Row Index

        sweep_bool = self.sweep(iy, ix)
        if self.running and not sweep_bool:
            self.gameOver()

        # print(f"Row: {iy}, Col: {ix}, Item: {self.items[iy][ix]},  vLayer: {self.vlayer[iy][ix]}, Flags: {self.flags}")
        self.updateCells()

    def handle_right_click(self):
        if not self.running:
<<<<<<< HEAD
            print("Running")
=======
>>>>>>> 6a79ecbb83351688da1391bdea8c05846a468463
            self.running = True

        ix = (self.rt.winfo_pointerx() - self.rt.winfo_rootx()) // self.cell_size # Column Index
        iy = (self.rt.winfo_pointery() - self.rt.winfo_rooty()) // self.cell_size # Row Index

        if self.vlayer[iy][ix] == 0:
            return
        elif self.vlayer[iy][ix] == 1:
            self.vlayer[iy][ix] = 2
            self.flags += 1
            self.flag_lbl.config(text=f"Flags: {self.flags}")
            self.cell[ix][iy].config(text="")
        elif self.vlayer[iy][ix] == 2:
            self.vlayer[iy][ix] = 1
            self.flags -= 1
            self.flag_lbl.config(text=f"Flags: {self.flags}")
            self.cell[ix][iy].config(text="|◤", fg="#d22")

        # print(f"Row: {iy}, Col: {ix}, Item: {self.items[iy][ix]},  vLayer: {self.vlayer[iy][ix]}, Flags: {self.flags}")
        self.updateCells()

    def gameOver(self):
        print("Game Over")
        self.vlayer = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.updateCells()
        self.running = False
<<<<<<< HEAD
        print("Not running")
=======
>>>>>>> 6a79ecbb83351688da1391bdea8c05846a468463

    def gameWin(self):
        return ## TODO:

    ### TK FUNCTIONS ###
    def updateCells(self):
        COLOR=["#7F7F7F", "#0024F9", "#017D1F", "#FF0A01", "#00107C", "#810403", "#007F80", "#F700ED", "#FFC100", "#000000"]
        for r in range(self.row):
            for c in range(self.col):
                if self.vlayer[r][c] == 2 or self.vlayer[r][c] == 1:
                    continue
                if self.vlayer[r][c] == 0:
                    self.cell[c][r].config(relief=SUNKEN, text=str(self.items[r][c]), fg=COLOR[self.items[r][c]], activeforeground=COLOR[self.items[r][c]])

    def window(self):
<<<<<<< HEAD
        self.rt.bind("<Button-1>", lambda x : self.handle_left_click())
        self.rt.bind("<Button-3>", lambda y : self.handle_right_click())

    def restart(self):
        self.rt.destroy()
        self.__init__()
=======
        self.cellSetup()
        self.rt.bind("<Button-1>", lambda x : self.handle_left_click())
        self.rt.bind("<Button-3>", lambda y : self.handle_right_click())
        self.rt.mainloop()
>>>>>>> 6a79ecbb83351688da1391bdea8c05846a468463

    def restart(self):
        self.rt.destroy()
        self.__init__()

### END PYSWEEPER CLASS

def printb(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end=" ")
        print()
    print()

def main():
    game = pysweeper()

if __name__ == "__main__":
    main()
