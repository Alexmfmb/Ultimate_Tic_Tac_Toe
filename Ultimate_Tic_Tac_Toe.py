import random as rnd

#TO DO: Draw mechanism in Win-check

class Board():
    def __init__(self) -> None:
        self.owner = "."
        self.won = False

        #creating 3x3 array of Fields
        self.field_arr = [[".",".","."],[".",".","."],[".",".","."]]
        
    def win_check(self):
        for i in range(3):
            #rows won
            if self.field_arr[i][0] == self.field_arr[i][1] == self.field_arr[i][2] and self.field_arr[i][0] != ".":
                self.owner = self.field_arr[i][0]
                self.won = True

            #cols won
            elif self.field_arr[0][i] == self.field_arr[1][i] == self.field_arr[2][i]and self.field_arr[0][i] != ".":
                self.owner = self.field_arr[0][i]
                self.won = True

        #diags won
        if self.field_arr[0][0] == self.field_arr[1][1] == self.field_arr[2][2] and self.field_arr[0][0] != ".":
                self.owner = self.field_arr[0][0]
                self.won = True
        if self.field_arr[0][2] == self.field_arr[1][1] == self.field_arr[2][0] and self.field_arr[0][2] != ".":
                self.owner = self.field_arr[0][2]
                self.won = True
        
        if self.won:
            for i in range(3):
                for j in range(3):
                    self.field_arr[i][j] = self.owner

        
class Main_board():
    def __init__(self) -> None:
         #creating 3x3 Array of Boards
        self.board_arr = [[Board(),Board(),Board()],[Board(),Board(),Board()],[Board(),Board(),Board()]]

        self.owner = "."
        self.won = False
        
    def win_check(self):
        #goes through all winning combinations and changes self.won
        for i in range(3):
            for j in range(3):
                self.board_arr[i][j].win_check()

        for i in range(3):
            #rows won
            if self.board_arr[i][0].owner == self.board_arr[i][1].owner == self.board_arr[i][2].owner and self.board_arr[i][0].owner != ".":
                self.owner = self.board_arr[i][0].owner
                self.won = True

            #cols won
            elif self.board_arr[0][i].owner == self.board_arr[1][i].owner == self.board_arr[2][i].owner and self.board_arr[0][i].owner != ".":
                self.owner = self.board_arr[0][i].owner
                self.won = True

        #diags won
        if self.board_arr[0][0].owner == self.board_arr[1][1].owner == self.board_arr[2][2].owner and self.board_arr[0][0].owner != ".":
                self.owner = self.board_arr[0][0].owner
                self.won = True
        if self.board_arr[0][2].owner == self.board_arr[1][1].owner == self.board_arr[2][0].owner and self.board_arr[0][2].owner != ".":
                self.owner = self.board_arr[0][2].owner
                self.won = True
    
    def show_status(self):
        #show status of game as printed string
        st = 25* "-" + "\n" 
        for board_row in range(3):
            for field_row in range(3):
                st += "| "
                for board_col in range(3):
                    for field_col in range(3):
                        #show content of fields
                        st += f"{self.board_arr[board_row][board_col].field_arr[field_row][field_col]}" + " "
                    st += "| " 
                    #divides cols of boards
                st += "\n"   
                #new line after each row of fields
            st += 4*"-" + str(3*board_row + 1) + 7*"-" + str(3*board_row + 2) + 7*"-" + str(3*board_row + 3) + 4*"-" +"\n" 
            #divides rows of boards

        print(st) #print current status of the main_board

       


def main():
    #Game of two players making random moves
    random_game = input("Game against a random Bot? [Y] ")

    in_dict = {"1":[0,0], "2":[0,1], "3":[0,2],
              "4":[1,0], "5":[1,1], "6":[1,2],
              "7":[2,0], "8":[2,1], "9":[2,2]}
    
    rev_in_list = [["1","2","3"],["4","5","6"],["7","8","9"]]
    
    #set start parameters
    main_board = Main_board()
    players = ["X","O"]
    Game_end = False
    player_turn = players[0]
    board_turn = "ANY"
    turn_counter = 0

    print(20*"." + "Game started" + 20*".")

    while(Game_end == False):
        
        #show status
        main_board.show_status()

        turn_counter += 1
        print(f"TURN NO {turn_counter}. TURN OF PLAYER {player_turn}")

        #selecting starting board
        if(board_turn == "ANY"):
            if(random_game == "Y" and player_turn == players[1]):
                b_inp = str(rnd.randint(1,9))
            else:
                b_inp = input(f"Player {player_turn} selects board by entering board ID: ")
            
            
            #checking input:
            while(b_inp not in in_dict.keys() or main_board.board_arr[in_dict[b_inp][0]][in_dict[b_inp][1]].won == True):
                if(random_game == "Y" and player_turn == players[1]):
                    b_inp = str(rnd.randint(1,9))
                else:
                    b_inp = input(f"Invalid input: {b_inp}, valid IDs are 1 to 9. Enter new input: ")
            
            b_inp = in_dict[b_inp] #inp is now list
            board_turn = b_inp #setting board for current round
            

        #Turn input 
        if(random_game == "Y" and player_turn == players[1]):
            inp = str(rnd.randint(1,9))
        else:
            inp = input(f"Player {player_turn} has to play on Board {rev_in_list[board_turn[0]][board_turn[1]]}. Enter Field ID: ")
        

        #checking validity of input
        while(inp not in in_dict.keys() or main_board.board_arr[board_turn[0]][board_turn[1]].field_arr[in_dict[inp][0]][in_dict[inp][1]] != "."):
            if(random_game == "Y" and player_turn == players[1]):
                inp = str(rnd.randint(1,9))
            else:
                inp = input(f"Invalid input: {inp}, valid IDs are 1 to 9. Enter new input: ")

        inp = in_dict[inp] #inp is now list

        #saving input on board
        main_board.board_arr[board_turn[0]][board_turn[1]].field_arr[inp[0]][inp[1]] = player_turn

        #make win-check
        main_board.win_check()

        #Set next board to play on
        if main_board.board_arr[inp[0]][inp[1]].won: #if player has to play on board which is already won, he can choose the next board
            board_turn = "ANY"
        else: board_turn = inp

        #Set turn to other player
        if(player_turn == players[0]): player_turn = players[1]
        elif(player_turn == players[1]): player_turn = players[0]

        #check game end
        if(main_board.won): Game_end = True

        print(50 * "#")


    print(25 * "🌟")
    print(f"PLAYER {main_board.owner} HAS WON THE GAME")
    print(25 * "🌟")
    input("Press any key to exit")


if __name__ == "__main__":
    main()