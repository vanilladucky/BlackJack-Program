from counting_technique import *

class BasicStrategyDictionary(): #will return the course of action to take for the player

    def __init__(self, player_card: list, dealer_first_card: int): #player_card in a list form and dealer_first_card in integer form
        self.player_card = player_card
        self.dealer_first_card = dealer_first_card
        assert self.dealer_first_card in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A"], "Dealer's card is invalid!"

        if self.dealer_first_card == "A":
            self.dealer_first_card = 11
        total = Counting(self.player_card)

        assert total.count() < 21, "\nSum of player's cards are above 21! Something is wrong with the code flow."
        
        


    def __hardtotal(self): #absence of an Ace card or >= 3 cards in hands
        self.hard_total_dict = {'20': 'Stand',
                                '19': 'Stand',
                                '18': 'Stand', 
                                '17': 'Stand', 
                                '16': 'Stand' if 2<= self.dealer_first_card <=6 else 'Hit',
                                '15': 'Stand' if 2<= self.dealer_first_card <=6 else 'Hit',
                                '14': 'Stand' if 2<= self.dealer_first_card <=6 else 'Hit',
                                '13': 'Stand' if 2<= self.dealer_first_card <=6 else 'Hit',
                                '12': 'Stand' if 4<= self.dealer_first_card <=6 else 'Hit', 
                                '11': 'Double' if 2<= self.dealer_first_card <=10 else 'Hit',
                                '10': 'Double' if 2<= self.dealer_first_card <=9 else 'Hit',
                                '9': 'Double' if 3<= self.dealer_first_card <=6 else 'Hit', 
                                '8': 'Hit',
                                '7': 'Hit',
                                '6': 'Hit',
                                '5': 'Hit',
                                } 
        total = Counting(self.player_card)
        result = self.hard_total_dict[str(total.count())]
        return result  

    def __handle_case_soft_total(self, hand): #private method
            if 9<=hand<=10:
                return 'Hit'
            else:
                return 'Stand'

    def __softtotal(self): #has an ace card with only 2 cards in hand
        self.soft_total_dict = {'21': 'Stand',
                                '20': 'Stand', 
                                '19': 'Stand', 
                                '18': 'Double' if 3<= self.dealer_first_card <=6 else self.__handle_case_soft_total(self.dealer_first_card),
                                '17': 'Double' if 3<= self.dealer_first_card <=6 else 'Hit', 
                                '16': 'Double' if 4<= self.dealer_first_card <=6 else 'Hit', 
                                '15': 'Double' if 4<= self.dealer_first_card <=6 else 'Hit', 
                                '14': 'Double' if 5<= self.dealer_first_card <=6 else 'Hit', 
                                '13': 'Double' if 5<= self.dealer_first_card <=6 else 'Hit',
                                } 

        total = Counting(self.player_card)
        result = self.soft_total_dict[str(total.count())]
        return result  

    def __handle_case_pairs(self, hand):
            if hand == 'A' or hand == '7' or hand == '10':
                return 'Stand'
            else: 
                return 'Split'  
    
    def __pairs(self): #when card are pairs   
        self.pairs_dict = {'4': 'Split' if 2<= self.dealer_first_card <= 7 else 'Hit',
                            '6': 'Split' if 2<= self.dealer_first_card <= 7 else 'Hit', 
                            '8': 'Split' if 5<= self.dealer_first_card <=6 else 'Hit',
                            '10': 'Double',
                            '12': 'Split' if 2<= self.dealer_first_card <= 6 else 'Hit',
                            '14': 'Split' if 2<= self.dealer_first_card <= 7 else 'Hit',
                            '16': 'Split',
                            '18': 'Split' if 2<= self.dealer_first_card <=6 else self.__handle_case_pairs(self.dealer_first_card),
                            '20': 'Stand',
                            '22': 'Split'}
        
        total = CountingForPairs(self.player_card)
        result = self.pairs_dict[str(total.count())]
        return result 

    #would only need to run this function for the course of action to take 
    def action_to_take(self):
        if len(self.player_card) >= 3: #hard total
            result = self.__hardtotal()
        else: #len <= 2
            if self.player_card[0] == self.player_card[1]:
                result = self.__pairs()
            else: #if not a pair
                if 'A' in self.player_card: #soft total 
                    result = self.__softtotal()
                else: #hard total with less than 2 cards
                    result = self.__hardtotal()
        return result 

#---------proven to be correct for all occasions----------#
"""test = BasicStrategyDictionary([4, 'A'], 'A')
print(test.action_to_take())
"""