import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self): 
        self.game = CardGame()
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("hearts", 2)
        self.card_3 = Card("hearts", 3)
       
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card_1))
   
    def test_highest_card(self):
        self.assertEqual(self.card_3, self.game.highest_card(self.card_2, self.card_3))

    def test_cards_total(self):
        cards = []
        cards.append(self.card_1)
        cards.append(self.card_2)
        cards.append(self.card_3)
        self.assertEqual("You have a total of 6", self.game.cards_total(cards))