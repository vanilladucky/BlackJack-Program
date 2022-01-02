from card_class import CardDeck
from player_class import *
from dealer_class import * 
from betting_class import *
from basic_strategy_dictionary_class import *
from counting_technique import *
from winlosspayout_class import *

print("Shall we start the game?")
answer = input("Y,N ")
if answer == "Y":
    pass
else:
    raise Exception("Program has been stopped")


print("Shuffling cards now")
cards = CardDeck(6)
print("Done shuffling cards\n")
player_starting_amount = 1000

while len(cards.deck_of_cards) > 4:
    
    # Just some simple dealing out of cards to start with
    player = Player(cards.starting_draw)
    dealer = Dealer(cards.starting_draw)
    
    # Decide on the betting size 
    bet = Betting(cards.true_count())
    
    temp = dealer.total()
    
    #dealer's turn
    #let dealer go first because we need to account for doubles win and loss below and this is the only way i figured
    if dealer.total() >= 17:
        dealer.stand()
    else:
        while dealer.total() <= 16:
            temp = cards.additional_draw()
            dealer.hit(temp)
    
    game_result = [] #an idea to add all the results here so that we can just +betting * number of players and -betting * number of dealers in this list
    
    #the first step is to check whether the player has a blackjack 
    if player.total() == 21:
        if temp == 21:
            continue
        else:
            player_starting_amount += (1.5*bet)
            continue
              
            
    #this is where the real deal happens 

    
    
    else: #player goes first
        basic_strategy = BasicStrategyDictionary(player.cards, dealer.cards[0])
        action_to_take = basic_strategy.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
        
        #can only split up to a maximum of 2 times for simplicity sake
        if action_to_take == 'Split':
            player.split(cards.additional_draw(), cards.additional_draw())
            
            player_1 = Player(player.cards[0])
            basic_strategy_1 = BasicStrategyDictionary(player_1.cards, dealer.cards[0])
            action_to_take_1 = basic_strategy_1.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
            
            if action_to_take_1 == "Split":
                player_1.split(cards.additional_draw(), cards.additional_draw())
                
                player_1_1 = Player(player_1.cards[0])
                basic_strategy_1_1 = BasicStrategyDictionary(player_1_1.cards, dealer.cards[0])
                action_to_take_1_1 = basic_strategy_1.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                
                player_1_2 = Player(player_1.cards[1])
                basic_strategy_1_2 = BasicStrategyDictionary(player_1_2.cards, dealer.cards[0])
                action_to_take_1_2 = basic_strategy_1.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
            
            else: #if the action to take is either 'Stand', 'Hit', 'Double'
                while action_to_take != 'Stand':
                    if action_to_take == 'Hit':
                        player_1.hit(cards.additional_draw) #will have updated new hands
                        basic_strategy = BasicStrategyDictionary(player_1.cards, dealer.cards[0])
                        action_to_take = basic_strategy.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                    else: #when it is a Double
                        player_1.double(cards.additional_draw) #will have updated new hand
                        action_to_take == "Stand"
            
            player_2 = Player(player.cards[1])
            basic_strategy_2 = BasicStrategyDictionary(player_2.cards, dealer.cards[0])
            action_to_take_2 = basic_strategy_2.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
            
            if action_to_take_2 == "Split":
                player_2.split(cards.additional_draw(), cards.additional_draw())
                
                player_2_1 = Player(player_2.cards[0])
                basic_strategy_2_1 = BasicStrategyDictionary(player_2_1.cards, dealer.cards[0])
                action_to_take_2_1 = basic_strategy_1.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                
                player_2_2 = Player(player_2.cards[1])
                basic_strategy_2_2 = BasicStrategyDictionary(player_2_2.cards, dealer.cards[0])
                action_to_take_2_2 = basic_strategy_1.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                
            else: #if the action to take is either 'Stand', 'Hit', 'Double'
                while action_to_take != 'Stand':
                    if action_to_take == 'Hit':
                        player_2.hit(cards.additional_draw) #will have updated new hands
                        basic_strategy = BasicStrategyDictionary(player_2.cards, dealer.cards[0])
                        action_to_take = basic_strategy.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                    else: #when it is a Double
                        player_2.double(cards.additional_draw) #will have updated new hand
                        action_to_take == "Stand"
            
        else: #if the action to take is either 'Stand', 'Hit', 'Double'
            original_action_to_take = action_to_take
            while action_to_take != 'Stand':
                if action_to_take == 'Hit':
                    player.hit(cards.additional_draw) #will have updated new hands
                    basic_strategy = BasicStrategyDictionary(player.cards, dealer.cards[0])
                    action_to_take = basic_strategy.action_to_take() #will be 'Split' 'Double', 'Hit','Stand'
                else: #when it is a Double
                    player.double(cards.additional_draw) #will have updated new hand
                    action_to_take == "Stand"
            winlose = WinLossPayout(player.cards, dealer.cards)
            who_won = winlose.result()
            if who_won == 'player':
                if original_action_to_take == 'Double':
                    player_starting_amount += (2*bet)
                else:
                    player_starting_amount += bet
            elif who_won == 'dealer':
                if original_action_to_take == 'Double':
                    player_starting_amount -= (2*bet)
                else:
                    player_starting_amount -= bet
            else:
                continue
                    
    
    #after this the loop will restart and a new round of blackjack is played