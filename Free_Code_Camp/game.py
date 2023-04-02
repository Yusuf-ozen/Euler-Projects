from player import human_player, random_computer_player, GeniusComputerPlayer
import time


class ticTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    # we will use a single list to rep 3x3 board
        self.current_winner = None    # keep track of winner 

    def print_board(self):
        # This is just getting on the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |') 



    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc(tells us what number corresspponds to what box)
        number_board = [[str(i) for i in range(j*3, (j + 1) * 3)] for j in range(3)]

        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') 



    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for(i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)     

        # return moves


    def empty_squares(self):
        return ' ' in self.board


    def num_empty_squares(self):
        return self.board.count(' ')



    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true,
        # if invalid. return false

        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False



    def winner(self, square, letter):
        # winner if 3 in a row anywhere .. we have to check all possibilities!
        # first lets check the row
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1) * 3 ]
        if all([spot == letter for spot in row]):
            return True

        # check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True


        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to to win a diagonal
        if square % 2 ==0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal 
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True


        # if all oof these fail

        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter! Or none for a tie 
    if print_game:
        game.print_board_nums()


    letter = 'X'   # starting letter 
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that 
    # which braeks the loop)

    while game.empty_squares():
        if letter == '0':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!


        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')   # just empty line 


            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')

                return letter

            # after we made our move, we need to alternate letters
            letter = '0' if letter == 'X' else 'X'   # switches player
            # if letter == 'X':
            #     letter = '0'

            # else:
            #     letter = 'X' 


            # BUT WAIT WHAT IF WE WON 


            # tiny break to make things a little easier to read
            if print_game:
                time.sleep(0.8)


    if print_game:
            print('It\'s a tie!')   

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):

        x_player = random_computer_player('X')
        o_player = GeniusComputerPlayer('0')
        t = ticTacToe()
        result = play(t, x_player, o_player, print_game=False)

        if result == 'X':
            x_wins += 1

        elif result == 'O':
            o_wins += 1

        else:
            ties += 1


    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, {ties} and ties.')