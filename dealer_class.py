from card_class import CardDeck
from counting_technique import *

class Dealer():

    def __init__(self, dealer_cards_list):
        self.cards = dealer_cards_list
        
    def total(self):
        total = Counting(self.cards())
        result = total.count()
        return result 

    def stand(self): #when count >= 17
        pass

    def hit(self, new_card): #when count <= 16
        self.cards().append(new_card)
        pass

#---------proven to be correct for all occasions----------#
"""card = CardDeck()

test = Dealer(card.starting_draw())
print(test.cards)

total = Counting(test.cards)
result = total.count()
#---------the important/necessary portion----------#
if result >= 17:
    result = test.stand()
else:
    while result <= 16:
        temp = card.additional_draw()
        result = test.hit(temp)"""


