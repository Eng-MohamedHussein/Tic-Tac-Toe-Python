"""[Tic Tac Toe Game implentation]

    Structure:
        [Main]:         	[The game is created as a loop inside the main function.
                                inside the Main function there is an object of class
                                in addtion to a set of seperate functions]
        [Class]:            [The game board is created, updated, printed through this class.
                                The class also helps by checking for the winner]
        [Functions]:        [These are a set of sepearte functions that uses the object of
                                the class to performe the game step for step]
    """

#!________________________________[Board Class]_____________________________________________


class Board():
    def __init__(self):
        self.Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def setBoard(self):

        for i in range(0, 3):
            for j in range(0, 3):
                self.Board[i][j] = "-"

    def printBoard(self):
        print("   1| 2 | 3 |")
        for i in range(0, 3):
            print(i+1, end="")
            for j in range(0, 3):
                print(f'  {self.Board[i][j]}|', end="")
            print()

    def updateBoard(self, p1, p2, num):
        if num == 1:
            self.Board[p1-1][p2-1] = "x"
        elif num == 2:
            self.Board[p1-1][p2-1] = "o"
        self.printBoard()

    def checkWinner(self, num):

        if num == 1:  # checking the first player

            # checking the diagonals

            if self.Board[0][0] == "x" and self.Board[1][1] == "x" and self.Board[2][2] == "x":
                return True
            elif self.Board[0][2] == "x" and self.Board[1][1] == "x" and self.Board[2][0] == "x":
                return True

            # checking the rows.

            elif self.Board[0][0] == "x" and self.Board[0][1] == "x" and self.Board[0][2] == "x":
                return True
            elif self.Board[1][0] == "x" and self.Board[1][1] == "x" and self.Board[1][2] == "x":
                return True
            elif self.Board[2][0] == "x" and self.Board[2][1] == "x" and self.Board[2][2] == "x":
                return True

            # checking the columns

            elif self.Board[0][0] == "x" and self.Board[1][0] == "x" and self.Board[2][0] == "x":
                return True
            elif self.Board[0][1] == "x" and self.Board[1][1] == "x" and self.Board[2][1] == "x":
                return True
            elif self.Board[0][2] == "x" and self.Board[1][2] == "x" and self.Board[2][2] == "x":
                return True
            else:
                return False

        elif num == 2:  # checking the second player

            # checking the diagonals

            if self.Board[0][0] == "o" and self.Board[1][1] == "o" and self.Board[2][2] == "o":
                return True
            elif self.Board[0][2] == "o" and self.Board[1][1] == "o" and self.Board[2][0] == "o":
                return True

            # checking the rows.

            elif self.Board[0][0] == "o" and self.Board[0][1] == "o" and self.Board[0][2] == "o":
                return True
            elif self.Board[1][0] == "o" and self.Board[1][1] == "o" and self.Board[1][2] == "o":
                return True
            elif self.Board[2][0] == "o" and self.Board[2][1] == "o" and self.Board[2][2] == "o":
                return True

            # checking the columns

            elif self.Board[0][0] == "o" and self.Board[1][0] == "o" and self.Board[2][0] == "o":
                return True
            elif self.Board[0][1] == "o" and self.Board[1][1] == "o" and self.Board[2][1] == "o":
                return True
            elif self.Board[0][2] == "o" and self.Board[1][2] == "o" and self.Board[2][2] == "o":
                return True
            else:
                return False


# !_________________________________________________[Main]________________________________________


def main():

    player1 = ""
    player2 = ""
    currentPlayer = ""
    playernumber = 0
    row, column, turns = 0, 0, 0

    B = Board()
    B.setBoard()
    # B.printBoard()

    player1, player2 = getPlayers()
    currentPlayer, playernumber = setPlayers(
        player1, player2, currentPlayer, playernumber)
    while True:
        if playernumber > 2 or playernumber <= 0:
            currentPlayer, playernumber = setPlayers(
                player1, player2, currentPlayer, playernumber)

        else:
            break

    while turns < 2:
        row, column = getEntry()
        B.updateBoard(int(row), int(column), playernumber)

        if B.checkWinner(playernumber):
            print(f"the winner is player{playernumber}")
            break
        currentPlayer, playernumber = changePlayer(
            player1, player2, currentPlayer, playernumber)
        row, column = getEntry()
        B.updateBoard(int(row), int(column), playernumber)
        if B.checkWinner(playernumber):
            print(f"the winner is player{playernumber}")
            break

        currentPlayer, playernumber = changePlayer(
            player1, player2, currentPlayer, playernumber)
        row, column = getEntry()
        B.updateBoard(int(row), int(column), playernumber)
        if B.checkWinner(playernumber):
            print(f"the winner is player{playernumber}")
            break
        currentPlayer, playernumber = changePlayer(
            player1, player2, currentPlayer, playernumber)

    # print(f"the first player is {player1}")
    # print(f'the second player is {player2}')
    # print(f'the current player is {currentPlayer}')
    # print(f'the Row is {row} and the column is {column}')


#!______________________________[Functions Implementation]_________________________________________


def getPlayers():
    p1 = input("Please enter the name of the first plyer\n")
    p2 = input("Please enter the name of the second plyer\n")

    return p1, p2


def setPlayers(p1, p2, current, num):
    x = int(input("who is playing first?\n"))
    if x == 1:
        current = p1
        num = 1
    elif x == 2:
        current = p2
        num = 2
    else:
        print("invalid entry!")
        print("Please try again.")
        num = x
    return current, num


def changePlayer(p1, p2, current, num):
    if current == p1:
        current = p2
        num = 2
    elif current == p2:
        current = p1
        num = 1
    return current, num


def getEntry():
    r, c = input("please enter the number of Row and Column\n").split()
    return r, c


if __name__ == '__main__':
    main()
