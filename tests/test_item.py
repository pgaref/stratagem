__author__ = 'MACSAMI'

import unittest
from models.item import Item
from models.user import User
from models.bid import Bid

class TestItem(unittest.TestCase):
    def setUp(self):
        #init users
        self.user1 = User('John')
        self.user2 = User('Paul')
        #init bids
        self.bid1 = Bid(10, self.user1)
        self.bid2 = Bid(6, self.user2)
        #init items
        self.item1 = Item('Item1')
        self.item1.new_bid(self.bid1, self.bid2)
        self.item2 = Item('Item2')

    def test_init(self):
        self.assertEqual(self.item1.name, 'Item1', 'incorrect name for item')

    def test_new_bid(self):
        self.bid3 = Bid(12,self.user1)
        self.item2.new_bid(self.bid3)
        self.assertEqual(len(self.item2.bids), 1, 'invalid number of bids')

    def test_get_max_bid(self):
        self.assertEqual(self.item1.get_winning_bid().value, 10, 'incorrect max bid when not None')
        self.assertEqual(self.item2.get_winning_bid(), None, 'incorrect max bid when None')


if __name__ == '__main__':
    unittest.main()