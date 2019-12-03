import random

class Card:
	# this class deals card and show
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of the {self.suit} "


class Deck:
	def __init__(self):
		self.deck = []  # start with an empty list

		#No need to specify self variables since using global variabls
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))#each card in this deck has two attributes suit and rank

	def __str__(self):
		#initialize an empty list to store all the combination of the card
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return 'Cards in this deck are :' + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		dealt_card = self.deck.pop()
		return dealt_card


class Hand:
	def __init__(self):
		self.cards = []  # start with an empty list as we did in the Deck class
		self.value = 0   # start with zero value
		self.aces = 0    # add an attribute to keep track of aces

	def add_card(self,card):
		self.cards.append(card)
		if card.rank != 'Ace':
			self.value += values[card.rank]
		else:
			ace_value = int(input('Do you want to use Ace as 1 or 11?'))
			self.value += ace_value


class Chips:
	def __init__(self):
		self.total = chip_value  # This can be set to a default value or supplied by a user input
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):#chips=Chips()
	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet?'))
		except ValueError:
			print('Sorry, a bet must be an integer')
		else:
			if chips.bet>chips.total:
				print('Sorry, your bet can not be exceed',chips.total)
			else:
				break


def hit(deck, hand):
	hand.add_card(deck.deal())
	if hand.value >21:
		print('You busted')
	else:
		pass


def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("Would you like to Hit or Stand? Enter h or s").upper()

		if x[0] == 'H':
			hit(deck,hand)
		elif x[0] == 'S':
			print("Player stands. Dealer's turn")
			playing = False
		else:
			print('Please choose again')
			continue
		break


def show_some(player,dealer):
	print("\n Dealer's Hand:")
	print("<card hidden>")
	print(' ',dealer.cards[1])
	print("\n Player's Hands:", *player.cards, sep='\n')


def show_all(player,dealer):
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)


def player_busts(chips):
	print("Player busts!")
	chips.lose_bet()


def player_wins(chips):
	print("Player wins!")
	chips.win_bet()


def dealer_busts(chips):
	print("Dealer busts!")
	chips.win_bet()


def dealer_wins(chips):
	print("Dealer wins!")
	chips.lose_bet()


def push():
	print("Dealer and Player tie! It's a push.")



#---------------------Game Start-----------------------------------#
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
		 'Queen':10, 'King':10, 'Ace':[1,11]}
chip_value = int(input('How much chips do you want to buy?'))
playing = True

while True:
	# Print an opening statement
	print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
	    Dealer hits until she reaches 17. Aces count as 1 or 11.')

	#shuffle deck
	deck = Deck()
	deck.shuffle()

	#deal 2 cards to player
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	#deal 2 cards to dealer
	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#Player chips
	player_chips = Chips()

	take_bet(player_chips)

	#Show one of dealer's hand and all of player's hand
	show_some(player_hand,dealer_hand)

	while playing:
		hit_or_stand(deck,player_hand)#if player choose Stand then turn will be change to Dealer

		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_chips)
			break

	# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			hit(deck, dealer_hand)

		# Show all cards if Dealer stops playing
		show_all(player_hand, dealer_hand)

		# Run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_chips)

		else:
			push()

	# Inform Player of their chips total
	print("\nPlayer's winnings stand at", player_chips.total)

	# Ask to play again
	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thanks for playing!")
		break
