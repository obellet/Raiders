# Imports
from card import my_deck

class Building:
    def __init__(self, name, description, accepted_workers, worker, action):
        self.name = name
        self.description = description
        self.accepted_workers = accepted_workers
        self.worker = worker
        self.action = action

    def __str__(self) -> str:
        pass

# Mill 
def mill_action(player):
    ## Gain 1 provision with a black worker
    if player.worker == "black":
        player.resources['provision'] += 1
        print(f'{player.name} has gained one provision')
    ## Gain 2 provisions with a grey worker
    elif player.worker == "grey":
        player.resources['provision'] += 2
        print(f'{player.name} has gained two provisions')
    ## Choose 1 gold or 2 provisions with a white worker
    elif player.worker == "white":
        player_input = int(input('Enter 1 for two provisions and 2 for one gold: '))
        if player_input == 1:
            player.resources['provision'] += 2
            print(f'{player.name} has gained two provisions')
        elif player_input == 2:
            player.resources['gold'] += 1
            print(f'{player.name} has gained one gold')
    else:
        print("Nothing happens")

mill = Building("Mill", "Gain provisions", ['black', 'grey', 'white'], None, mill_action)

# Silversmith
def silversmith_action(player):
    if player.worker == "black":
        player.resources['silver'] += 3
        print(f'{player.name} has gained 3 silvers')
    elif player.worker == "grey" or player.worker == "white":
        player.resources['silver'] += 2
        print(f'{player.name} has gained 3 silvers')
    else:
        print("Nothing happens")

silversmith = Building('Silversmith', "Gain silver", ['black', 'grey', 'white'], None, silversmith_action)

# Gate House
def gate_house_action(player):
    player.draw_card(my_deck, 2)
    print(f'{player.name} has drawn 2 cards')

gate_house = Building('Gate House', "Draw Cards", ['black', 'grey', 'white'], None, gate_house_action)

# Town Hall
def town_hall_action(player):
    while True:
        print("Your Hand:")
        for i, card in enumerate(player.hand):
            print(f"{i + 1}. {card.name}")

        try:
            player_input = int(input('Enter the index of the card you wish to discard and play: ')) - 1
            if 0 <= player_input < len(player.hand):
                card = player.hand[player_input]
                card.play_action(player)
                player.hand.pop(player_input) 
                print(f"{player.name} has discarded the {card.name}")
                break  # Exit the loop when a valid card is selected
            else:
                print("Invalid input. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

town_hall = Building('Town Hall', "Play Cards", ['black', 'grey', 'white'], None, town_hall_action)

# Barracks
def barracks_action(player):
    while True:
        print(f"you have {player.resources['silver']} silver")
        print("Your Hand:")
        for i, card in enumerate(player.hand):
            print(f"{i + 1}. {card.name}: {card.cost} silver")

        try:
            player_input = int(input('Enter the index of the card you wish to discard and play: ')) - 1
            if 0 <= player_input < len(player.hand):
                card = player.hand[player_input]
                if card.cost <= player.resources['silver']:
                    player.crew.append(card)
                    player.hand.pop(player_input) 
                    print(f"{player.name} has recruited the {card.name} for {card.cost} silver")
                    player.resources['silver'] -= card.cost
                    break  # Exit the loop when a valid card is selected
                else: 
                    print(f'You do not have the necessary silver to hire the {card.name}')
            else:
                print("Invalid input. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

barracks = Building('Barracks', 'Hire Crew Members', ['black', 'grey', 'white'], None, barracks_action)