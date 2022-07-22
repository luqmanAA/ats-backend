
import sys

class TicTacToe:

    def __init__(self) -> None:
        # self.game_board = [['0']*3]*3
        self.game_board =[0]*9
        self.player1 = ""
        self.player2 = ""
        
    
    def draw_game_board(self):
        # for i in self.game_board:
        #     for j in range(len(i)):
        #         print(i[j], end = '   ')
        #     print()
        # print()

        print(f"{self.game_board[6]}  | {self.game_board[7]} | {self.game_board[8]}\n")
        print(f"{self.game_board[3]}  | {self.game_board[4]} | {self.game_board[5]}\n")
        print(f"{self.game_board[0]}  | {self.game_board[1]} | {self.game_board[2]}")

    def start_game(self):
        print("******* Welcome, the game board has 9 places and it's played by selecting place position i.e 1-9. *******")
        self.draw_game_board()
        self.player1 += input("Enter the first player's name: ")
        self.player2 += input("Enter the second player's name: ")
    
    def play_game(self):
        self.start_game()
        print(self.player1, self.player2)
        self.turn = "X"
        self.player_turn = self.player1

        for i in range(10):
            self.draw_game_board()
            self.move = int(input(f"It's your turn {self.player_turn}. Move to which place?: ")) - 1
            if self.game_board[self.move] == 0:
                self.game_board[self.move] = self.turn
            else:
                print("Place is filled")
            
            if self.game_board[6] == self.game_board[7] == self.game_board[8] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[3] == self.game_board[4] == self.game_board[5] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[0] == self.game_board[1] == self.game_board[2] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[0] == self.game_board[3] == self.game_board[6] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[1] == self.game_board[4] == self.game_board[7] != 0:
                return self.check_winner(self.turn)
            
            elif self.game_board[2] == self.game_board[5] == self.game_board[8] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[0] == self.game_board[4] == self.game_board[8] != 0:
                return self.check_winner(self.turn)
                
            elif self.game_board[2] == self.game_board[4] == self.game_board[6] != 0:
                return self.check_winner(self.turn)
                

            if self.turn == "X":
                self.turn = "O"
                self.player_turn = self.player2
            else:
                self.turn = "X"
                self.player_turn = self.player1

    def check_winner(self, turn):
        self.draw_game_board()
        print("Game over")

        if turn == "X":
            return (f"{self.player1} won!")
        return(f"{self.player2} won!")

tic = TicTacToe()
print(tic.play_game())
