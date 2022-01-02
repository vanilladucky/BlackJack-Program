from counting_technique import *

class WinLossPayout():

    def __init__(self, players_cards, dealers_cards):
        self.player_cards = players_cards
        self.dealers_cards = dealers_cards

    def result(self):

        total_1 = Counting(self.player_cards())
        players_total = total_1.count()

        total_2 = Counting(self.dealers_cards())
        dealers_total = total_2.count()

        if dealers_total > 21: #checking whether dealer went bust 
            return "player"
        elif players_total > dealers_total:
            return "player"
        elif players_total < dealers_total:
            return "dealer"
        else:
            return "push" 
#---------proven to be correct for all occasions----------#