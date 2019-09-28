import random

class Board():
    '''
    '''

    def __init__(self, size = 3):
        self.size = size **2
        self.row = size
        self.column = size
        rows = list(range(0,self.row))
        columns = list(range(0,self.column))
        self.box = {row:{column:None for column in columns} for row in rows}
        return

    def update_box(self, turn):
        while (self.box[self.row][self.column] != True) | self.box[self.row][self.column] != False:
            if turn // 2 != 0:
                self.box[self.row][self.column] = True
            elif turn // 2 == 0:
                self.box[self.row][self.column] = False
        else:
            print("Box already taken!")
        return

    def check_winner(self, turn):
        if turn // 2 == 0:
            if self.box[0][0] == True & self.box[0][1] == True & self.box[0][2] == True:
                winner = True
                print("The winner is x")
            elif self.box[1][0] == True & self.box[1][1] == True & self.box[1][2] == True:
                winner = True
                print("The winner is x")
            elif self.box[2][0] == True & self.box[2][1] == True & self.box[2][2] == True:
                winner = True
                print("The winner is x")
            elif self.box[0][0] == True & self.box[1][0] == True & self.box[2][0] == True:
                winner = True
                print("The winner is x")
            elif self.box[0][1] == True & self.box[1][1] == True & self.box[2][1] == True:
                winner = True
                print("The winner is x")
            elif self.box[0][2] == True & self.box[1][2] == True & self.box[2][2] == True:
                winner = True
                print("The winner is x")
            elif self.box[0][0] == True & self.box[1][1] == True & self.box[2][2] == True:
                winner = True
                print("The winner is x")
            elif self.box[0][2] == True & self.box[1][1] == True & self.box[2][0] == True:
                winner = True
                print("The winner is x")
        else:
            if self.box[0][0] == False & self.box[0][1] == False & self.box[0][2] == False:
                winner = True
                print("The winner is o")
            elif self.box[1][0] == False & self.box[1][1] == False & self.box[1][2] == False:
                winner = True
                print("The winner is o")
            elif self.box[2][0] == False & self.box[2][1] == False & self.box[2][2] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][0] == False & self.box[1][0] == False & self.box[2][0] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][1] == False & self.box[1][1] == False & self.box[2][1] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][2] == False & self.box[1][2] == False & self.box[2][2] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][0] == False & self.box[1][1] == False & self.box[2][2] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][2] == False & self.box[1][1] == False & self.box[2][0] == False:
                winner = True
                print("The winner is o")
            elif self.box[0][0] == False & self.box[0][1] == False & self.box[0][2] == False & self.box[1][0] == False & self.box[1][1] == False & self.box[1][2] == False & self.box[2][0] == False & self.box[2][1] == False & self.box[2][2] == False:
                 draw = True
                 print("It's a draw!")
            return


class Player():
    """
    This class has one attribute: Name
    """

    def __init__(self, name):
        self.name = name
        return

    def turn(self, i):
        """
        Input: from player

        Output: row and column
        """
        l_i = i.split(":")
        self.row = l_i[0]
        self.column = l_i[1]
        return


class Game(Board):
    '''
    '''

    def __init__(self):
        return

    def start_the_game(self):
        """
        Input: The two names of the players
        Output: Decides which player is x and o. The x player always plays first
        """
        size = input("Enter the desired number of rows: ")

        name_1 = input("Player 1 enter your name: ")
        player_1 = Player(name_1)

        name_2 = input("Player 2 enter your name: ")
        player_2 = Player(name_2)

        names_l = [name_1, name_2]
        names_s = set(names_l)

        x_l = [random.choice(names_l)]
        x_s = set(x_l)

        o_s = names_s.difference(x_s)

        print(str(x_s) + " has been assigned x and will play first!")
        return

    def the_game(self):
        """
        Input:
        """
        turn = 0
        winner = False
        draw = False
        if winner == False | draw == False:
            turn += 1
            i = input("Enter the row and column with colon in between: ")
            Player.turn(self, i)
            Board.update_box(self, turn, self.box)
            Board.check_winner(self, turn, self.box)
        elif winner == True:
            print("The Game is now over!")
        elif draw == True:
            print("The Game is now over!")
        return
