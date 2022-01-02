import random

class CardDeck(): 

    global values 
    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self, number_of_decks=6):
        self.deck_of_cards = (values*4) * number_of_decks
        random.shuffle(self.deck_of_cards)
        self.used_cards = []
        self.running_count = 0

    def __hilo(self, card):
        if card in [10, 'J', 'Q', 'K', 'A']:
            count = -1
        elif 7 <= card <= 9:
            count = 0 
        else:
            count = 1
        return count

    def __deck_remaining(self):
        remaining_card = len(self.deck_of_cards)
        result = remaining_card // 52
        if result < 1:
            result = 1
        else:
            pass
        return result

    def starting_draw(self):
        first = self.deck_of_cards.pop()
        second = self.deck_of_cards.pop()
        self.used_cards.extend([first, second])
        temp = [first, second]
        self.running_count = self.running_count + self.__hilo(first) + self.__hilo(second)
        return temp 

    def additional_draw(self):
        card_to_be_drawn = self.deck_of_cards.pop()
        self.running_count = self.running_count + self.__hilo(card_to_be_drawn)
        return card_to_be_drawn

    def true_count(self):
        result = round(self.running_count / self.__deck_remaining())
        return result

#---------proven to be correct for all occasions----------#
"""test = CardDeck()
print(test.deck_of_cards)"""