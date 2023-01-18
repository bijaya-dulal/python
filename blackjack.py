#blackjack game 

import random
print("welcome to the black jack game")

'''return a random card from deck 11  is ace here and jqk are =10'''
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card
user_cards = []
computer_cards =[]
is_game_over=False

'''peaking 2 cards from deck rsndomly'''
for _ in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
def sum (fcard):
    sum=0
    for x in fcard:
        sum+=x
    return sum

'''calculating sum of cards'''   
def calculate_score(cards): 
    if sum(cards) == 21 and len(cards )== 2:
      return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 
'''k'''       
while not is_game_over :         
    user_score = calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"your cards:{user_cards}, current score:{user_score}")
    print(f"computer's first card:{computer_cards[0]} ")
     
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over=True

    else:
        user_should_deal=input("type y to get another card,type n for no")
        if user_should_deal=="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score= calculate_score(computer_cards)

def compare (user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score==0:
        return ("lose, oppenet has black jack")   
    elif user_score==0:
        return ("win with  black jack")  
    elif user_score >21:
        return "you went over ,lose"     
    elif computer_score > 21:
        return "you win opponent went out"     
    elif user_score>computer_score:
        return "you win"
    else:
        return "youlose"
print(f"computer score:{computer_score}")
result=compare(user_score,computer_score)          
print(result)