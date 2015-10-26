__author__ = 'MACSAMI'

import unittest
from models.bid import Bid
from models.user import User

class TestBid(unittest.TestCase):
    def setUp(self):
        self.user = User('John')
        self.bid = Bid(10, self.user)

    def test_bid(self):
        self.assertEqual(self.bid.value, 10, 'invalid value for bid')
        self.assertEqual(self.bid.user, self.user, 'invalid user for bid')

if __name__ == '__main__':
    unittest.main()