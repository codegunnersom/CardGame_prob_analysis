# PROBLEM STATEMENT

# In Front of you is a shuffled deck of cards. All 52 cards lie face down. 
# Half the cards are red, and half the cards are black. 
# I will proceed to flip over the cards one by one. If the last card I flip over is red, you'll win a dollar. 
# Otherwise you'll lose a dollar.
# Here's a twist. 
# You can ask me to halt the game at any time. 
# Once you say halt, I will flip over the next card and end the game.
# The next card will serve as the final Card.
# We can play the game as many times as you like. The deck will be reshuffled every time. After each round, we'll exchange money
# What is your best appraoch to winning this Game 




# BUILDING THE GAME

import random
import time

#Category of cards
Cards = ['Red', 'Black']

#Red Cards = 26
red_card_list = []

#Black Cards = 26
black_card_list = []

#All 52 Cards to simulate a pack
for i in range(1,27):
    j = str(i)
    #Adding Red cards
    red_card = j+"R"
    red_card_list.append(red_card)
    #Adding Black Cards
    black_card = j+"B"
    black_card_list.append(black_card)

global full_pack
full_pack = red_card_list + black_card_list

#+==================================================================================
# GAME LOGIC

#prompt function
def wanna_play():
    #prompt to start the game
    while True:
        global usr_input
        usr_input = input("\nWould you like to start the game (1 : yes, 2 : No)")
        # 1
        if usr_input == "1":
            #breaks the loop and proceeds to parent loop
            break
        # 2
        if usr_input == "2":
               print("Game Aborted")
               break
        
        else:
             print("\nInvalid response, please try again")



# main game function
def start_game():
    while True:
         wanna_play()
         if usr_input == "2":
              break
         
         # Taking money for balance
         bal_input = input("Enter an amount of money you want to bet : ")
         bal = int(bal_input)

         # Starting game
         print("\nLets Start the Game")
         print("\nEvery second, i'll flip a card, you tell me halt and I'll flip the next card and stop")

         # Shuffling Deck
         print("Shuffling Deck")
         random.shuffle(full_pack)
         shuffled_deck = full_pack

         current_ite = 0
         for i in shuffled_deck:
              current_card =  i

              #last card
              if current_ite == 51:
                   print(f"last card : {i}")
                   current_card = str(current_card)
                   if current_card in black_card_list:
                        print("You lose, you lost a dollar")
                        print(f"\nYour Balance : {bal - 1} dollars")
                        print(f"Exchanging Money, Now you have {bal + 1 } dollars")
                        break
                   else :
                        print("You Won !!! Its a red card")
                        print(f"Your Balance : {bal + 1} dollars")
                        print(f"Exchanging Money, Now you have {bal - 1} dollars")
                        break
                   


              current_ite += 1

              #Choice to Continue or halt
              usr_choice = input("Enter or 'halt' : ")
              if usr_choice == "halt":
                   print(f"Final Card = {current_card}")
                   current_card = str(current_card)
                   if current_card in black_card_list:
                        print("You lose, you lost a dollar")
                        print(f"\nYour Balance : {bal - 1} dollars")
                        print(f"Exchanging Money, Now you have {bal + 1 } dollars")
                        break
                   else :
                        print("You Won !!! Its a red card")
                        print(f"Your Balance : {bal + 1} dollars ")
                        print(f"Exchanging Money, Now you have {bal - 1} dollars")
                        break
                   

              #if continue 
              print(f"{current_ite}st Card : ")
              print(i)

              # for last card
              if current_ite == 52:
                   break
            
 #+======================================================================             

#INITIALIZING THE GAME

start_game()
#wanna_play()
    

            






