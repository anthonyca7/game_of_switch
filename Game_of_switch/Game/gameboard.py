from random import choice
from Game import player


class GameBoard:
    width = 6
    height = 6

    def __init__(self):
        self.board = []
        self.turn = 1
        self.player1 = player.player()
        self.player2 = player.player()
        self.player3 = player.player()
        self.player4 = player.player()
        for x in xrange(self.width):
            self.board.append([])
            for y in xrange(self.height):
                self.board[x].append(54)
        self.player1.setPiece(5, 0)
        self.player2.setPiece(5, 5)
        self.player3.setPiece(0, 5)
        self.player4.setPiece(0, 0)

    def start(self):
        cardsLeft = range(0, 52)
        for y in xrange(self.height):
            for x in xrange(self.width):
                card = choice(cardsLeft)
                self.board[y][x] = card
                cardsLeft.remove(card)

    def takeCard(self, player, row, column):
        card = self.board[row][column]
        self.board[row][column] = 54
        if player == 1:
            self.player1.toHand(card)
        elif player == 2:
            self.player2.toHand(card)
        elif player == 3:
            self.player3.toHand(card)
        elif player == 4:
            self.player4.toHand(card)
        else:
            raise Exception('Error: player attribute should be an int from 1 to 4')
