__author__ = 'MACSAMI'

class Item(object):
	def __init__(self, name):
		self.name = name
		self.bids = []

	def new_bid(self, *bids):
		for bid in bids:
			self.bids.append(bid)

	def get_winning_bid(self):
		if len(self.bids) == 0:
			return None
		else:
			max_bid = self.bids[0]
			for bid in self.bids[1:]:
				#get the first max bidder
				if bid.value > max_bid.value:
					max_bid = bid
				else:
					pass
			return max_bid

