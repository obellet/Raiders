from player import Player
from building import Building, mill, silversmith, gate_house, town_hall, barracks
from card import Card, Deck, my_deck

# Create the players
octave = Player('Octave')
# ryan = Player('Ryan')

# Create the deck of cards
print(my_deck)

# Distribute each player 5 cards for their hands 
octave.draw_card(my_deck, 3) # update to 5 for the actual game  
# ryan.draw_card(my_deck, 5)

# Player Discard down to 3 cards 
octave.discard_card(3)
# ryan.discard_card(3)


# Player go to buildings

## Mill
# octave.visit_building(mill)

## Silversmith
# octave.visit_building(silversmith)

## Gate House
# octave.visit_building(gate_house)
# print(octave)

## Town Hall
# octave.visit_building(town_hall)
# print(octave)

## Barracks
print(octave)
octave.visit_building(barracks)
print(octave)

## Armoury


## Long House

