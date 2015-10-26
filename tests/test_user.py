__author__ = 'MACSAMI'

import unittest
from models.user import User
from models.item import Item

class TestUser(unittest.TestCase):
    def setUp(self):
        self.item1 = Item('Item1')
        self.item2 = Item('Item2')
        self.u = User('John')
        self.u.bids = [(self.item1, 10),(self.item2, 8)]

    def test_init(self):
        self.assertEqual(self.u.name, 'John', 'incorrect name for user')

    def test_get_items(self):
        self.assertEqual(self.u.get_items(),[self.item1,self.item2], 'invalid items')

    def test_get_all_bid_for_one_item(self):
        self.assertEqual(self.u.get_all_bid_for_one_item(self.item1),[10], 'invalid bids for one item')

if __name__ == '__main__':
    unittest.main()