# Imports
        
class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'silver': 2, 
                          'provision': 2,
                          'gold': 2,
                          'iron': 2,
                          'sheep': 2}
        self.crew = []  # List of CrewMember objects
        self.worker = "white" # worker color
        self.hand = []  # List of Card objects

    def __str__(self):
        card_names = [card.name for card in self.hand]
        crew_names = [card.name for card in self.crew]
        return f"""
Player Name: {self.name}    
Worker Color: {self.worker}
Resources: {self.resources}
Hired Crew: {crew_names}
Cards: {card_names}
"""

    def visit_building(self, building):

        # Check that you are allowed to visit the building
        if (self.worker is None) ^ (building.worker is None) and self.worker in building.accepted_workers:

            # Perform the action
            print(f'{self.name} is visiting the {building.name}')
            building.action(self)

            # swap the workers
            if self.worker == None:
                self.worker = building.worker
                building.worker = None
            elif building.worker == None:
                building.worker = self.worker
                self.worker = None
            else: 
                print('The player and the building both had a worker, mistakes were made')

        else:
            print("sorry this action is not permitted")
    
    def draw_card(self, deck, num_cards):
        self.hand += deck.draw(num_cards)

    def discard_card(self, num_cards_keep):
        while len(self.hand) > num_cards_keep:
            print("Your Hand:")
            for i, card in enumerate(self.hand):
                print(f"{i + 1}. {card.name}")

            try:
                player_input = int(input('Enter the index of the card you wish to discard: ')) - 1
                if 0 <= player_input < len(self.hand):
                    discarded_card = self.hand.pop(player_input)
                    print(f"You have discarded the {discarded_card.name}")
                else:
                    print("Invalid input. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")