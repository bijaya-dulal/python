#strat the game
from random import randint
print("wel come to  guess the number!!!")
#choosing the level
level=str(input("choose the level easy or hard  "))
level=level.lower()
random_num=randint(1,100)

#here life is a global variable
if level=="easy":
  life=10
  
else:
    life=5 

print("you should guess the number between 1 and 100")
#define the function to check guess
def check_number(guess,random_num):
    global life
    if guess<random_num:
        print("too low")
        life-=1
    elif guess>random_num:
        print('too high')
        life-=1 
    else:
        print(f"You guess it. And the number is {random_num}") 
        life=-1
        

#guessing the number

while life>0: 
    print(f"your life is {life} ")
    guess= int(input("make a guess"))
    check_number(guess,random_num)
if life==0:
    print(f'you are out of move you lose!!!the number is {random_num}')
else:
    pass    
    
    
    
    
    
