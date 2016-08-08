import collections, copy
Card = collections.namedtuple('Card',['rank','suit'])

class Deck(object):

	def __int__(self):

		''' Initializes a deck of cards.'''

		ranks = [str(n) for n in range(2,11)] + list('JQKA')
		suits = 'spades diamonds clubs hearts'.split()

		self._cards = [Card(rank,suit) for rank in ranks for suit in suits]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, key):
		return self._cards[key]

	def flipBackSequence(self, deck = None):

		''' returns the sequence of cards, in order, if you drew the top card, put the next card at the back of the deck,
		and then repeated until only one card remained (in which case it would be returned.)'''

		if deck == None:
			deck = copy.deepcopy(self)

		if len(deck) == 1: # only one item left in the deck:
			return [deck[0]]

		else:
			topCard, secondCard = deck[0:2]

			deck = deck[1:]

			deck.insert(len(deck) + 1, secondCard)

			return [topCard] + flipBackSequence(self, deck)
			

