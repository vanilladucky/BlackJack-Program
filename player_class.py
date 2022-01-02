from counting_technique import *

class Player():

    def __init__(self, players_starting_card_list : list):
        self.cards = players_starting_card_list
        
    def total(self):
        total = Counting(self.cards())
        result = total.count()
        return result 

    def hit(self, new_card): #when basic strategy tells us to hit
        self.cards().append(new_card)
        pass

    def stand(self): #end turn; always has to be the last call and player's turn will end
        pass

    def double(self, new_card): #double the bet amount and end turn after this
        self.hit(new_card)
        self.stand()
        pass

    def split(self, new_card_1, new_card_2): #will split into two list(hands)
        self.cards = [
            [self.cards[0], new_card_1],
            [self.cards[1], new_card_2]
        ]
#---------proven to be correct for all occasions----------#