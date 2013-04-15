"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from Game import gameboard


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TestBoard(TestCase):
    def test_board_height(self):
        """
        Tests that the board is 6 pieces wide
        """
        game = gameboard.GameBoard()
        testBoard = game.board
        boardHeight = len(testBoard)
        self.assertEqual(boardHeight, 6)

    def test_board_width(self):
        """
        Tests that the board is 6 pieces high
        """
        game = gameboard.GameBoard()
        testBoard = game.board
        for row in testBoard:
            boardWidth = len(row)
            self.assertEquals(boardWidth, 6)

    def test_board_init(self):
        """
        Tests that the board is initialized with face-down cards (card 54)
        """
        game = gameboard.GameBoard()
        testBoard = game.board
        for row in testBoard:
            for card in row:
                self.assertEqual(card, 54)

    def test_board_start(self):
        """
        Tests that generating the cards on the board does not produce duplicates
        """
        game = gameboard.GameBoard()
        game.start()
        testBoard = game.board
        testBin=[]
        for row in testBoard:
            for card in row:
                self.assertNotIn(card, testBin)
                testBin.append(card)
