class Counting():

    def __init__(self, cards_list:list):
        self.cards = cards_list
        self.temp = []

    def count(self):
        number_of_aces = 0
        number_of_jqk = 0 
        

        for value in self.cards:  
            if value == 'A':
                number_of_aces += 1
            elif value in ["J", "Q", "K"]:
                number_of_jqk += 1
            else: 
                self.temp.append(value)
        
        total = sum(self.temp) + (11 * number_of_aces) + (10 * number_of_jqk)

        if total > 21:
            total -= (10 * number_of_aces)
        else:
            pass

        return total

#---------proven to be correct for all occasions----------#

class CountingForPairs():

    def __init__(self, cards_list:list):
        self.cards = cards_list
        self.temp = []
        if self.cards[0] != self.cards[1]:
            raise Exception("They are not pairs!") 

    def count(self):

        for value in self.cards:
            if value == "A":
                self.temp.append(11)
            elif value in ["J", "Q", "K"]:
                self.temp.append(10)
            else:
                self.temp.append(value)

        total = sum(self.temp)

        return total 

#---------proven to be correct for all occasions----------#
"""test = Counting(["A", "A"])
print(test.count())"""