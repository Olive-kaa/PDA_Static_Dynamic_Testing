import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('clubs', 11)
        self.card3 = Card('spades', 8)
        self.cardGame = CardGame()

    def test_check_for_ace(self):
        self.assertEquals( True, self.cardGame.check_for_ace(self.card1))

    def test_check_for_not_ace(self):
        self.assertEquals( False, self.cardGame.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEquals( self.card2, self.cardGame.highest_card(self.card1, self.card2))


        

    # def test_total_card_value(self):
    #     # cards=[self.card1, self.card2, self.card3]
    #     self.assertEquals( "You have a total of 13", self.cardGame.cards_total(cards))