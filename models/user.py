__author__ = 'MACSAMI'

from bid import Bid

class User(object):
	def __init__(self, name):
		self.name = name
		self.bids = []

	def make_bid(self, offer, item):
		bid = Bid(offer, self)
		item.new_bid(bid)
		#tuple because immutable
		couple = (item, offer)
		self.bids.append(couple)

	def get_items(self):
		#get only the first element of the tuple
		return [x[0] for x in self.bids]

	def get_all_bid_for_one_item(self, item):
		bids = []
		for bid in self.bids:
			if bid[0] == item:
				bids.append(bid[1])
			else:
				pass
		return bids



