class Betting(): #1-8 bet spread

    def __init__(self, true_count, one_unit = 10):
        self.betsize = one_unit
        self.true_count = true_count

    def calculate_bet_size(self):
        if self.true_count <= 1:
            result = self.betsize
        elif self.true_count == 2:
            result = 2*self.betsize
        elif self.true_count == 3:
            result = 4*self.betsize
        else:
            result = 8*self.betsize
        return result         
#---------proven to be correct for all occasions----------#