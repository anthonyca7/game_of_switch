class player:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.hand = []

    def toHand(self, card):
        self.hand.append(card)

    def setPiece(self, row, column):
        self.row = row
        self.column = column
