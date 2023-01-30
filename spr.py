

import random
print("wel come to the sissor paper rock")
playagain=True

while playagain:
  choice=int(input("enter\n0. for sissor \n1.for paper \n2. for rock\n"))
  if(choice ==0):
    my_choice= 'sissor'
  elif(choice==1):
    my_choice="Paper"
  elif(choice==2):
    my_choice="rock"
  else:
    my_choice="invalid" 


  print(f"your choice is {my_choice}")
  rnum=random.randint(0,2) 
  if(rnum==0):
    c_choice= 'sissor'
  elif(rnum==1):
    c_choice="Paper"
  else:
    c_choice="rock"


  print(f"computer choice is {c_choice}")
  if(choice<3 and choice>=0):
    if(choice!=rnum):
      if(choice==0):
        if(rnum==1):
              print("you win")

        else:
              print("you lose")

      elif(choice==1):
          if(rnum==0):
              print("you lose")
          else:
              print("you win")
      else:
          if(rnum==0):
              print("you win")
          else:
              print("you lose")
    else:
      print("no one win draw")
  else:
    print("please enter valid num")
  print("\U0001f600")            
  again=input('do you want to play again? type y for yes and n for no' )
  if again=="y":
    pass

  else:
    playagain=False
            
      