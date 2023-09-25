# Imports
import random

class Card:
    def __init__(self, name, strength, cost, crew_action, play_action):
        self.name = name
        self.strength = strength
        self.cost = cost
        self.crew_action = crew_action
        self.play_action = play_action

    def __str__(self) -> str:
        return f"""
Card Name: {self.name}
Military Strength: {self.strength}
Hiring Cost: {self.cost}
"""

# Cards

# Barbarian
def cartographer_play_action(player):
    if player.resources['provision'] >= 1:
        player.resources['gold'] += 1
        print(f'{player.name} has gained one gold')
    else:
        print('You do not have any provision to exchange')

    
cartographer = Card('Cartographer', 3, 3, None, cartographer_play_action)
forager = Card('Forager', 1, 1, None, None)
marauder = Card('Marauder', 0, 2, None, None)

# Deck Dictionnary
deck_dict = {
    cartographer: 10,
    forager: 10,
    marauder: 10,
}
    
class Deck:
    def __init__(self, card_dict):
        self.card_dict = card_dict
        self.cards = []
        self.size = 0

        # Generate the deck based on the card_dict
        for card, quantity in card_dict.items():
            self.cards.extend([card] * quantity)

    def __str__(self):
        card_names = [card.name for card in self.cards]
        return f"""
My Cards: {', '.join(card_names)}
"""
             
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards):
        if num_cards <= len(self.cards):
            return [self.cards.pop() for _ in range(num_cards)]
        else:
            return None
        
# Create a deck using the deck_dict
my_deck = Deck(deck_dict)

# Shuffle the deck
my_deck.shuffle()

# Draw and print a few cards from the deck
# drawn_cards = my_deck.draw(5)
# if drawn_cards:
#     for card in drawn_cards:
#         print(card)
# else:
#     print("Not enough cards in the deck to draw.")