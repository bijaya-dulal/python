
#bijaya dulal [25 Jul 2022 23:18:51]
print("welcome to love calculator!!")
you= input("enter your name:-\n")
crush= input("enter your crush name:-\n")
loweryou= you.lower()
lowercrush = crush.lower()
t=int(loweryou.count("t")) +int(lowercrush.count("t"))
r=int(loweryou.count("r")) +int(lowercrush.count("r"))
u=int(loweryou.count("t")) +int(lowercrush.count("u"))
e=int(loweryou.count("e")) +int(lowercrush.count("e"))
l=int(loweryou.count("l")) +int(lowercrush.count("l"))
o=int(loweryou.count("o")) +int(lowercrush.count("o"))
v=int(loweryou.count("v")) +int(lowercrush.count("v"))
e=int(loweryou.count("e")) +int(lowercrush.count("e"))

true= str(t+r+u+e)
love= str(l+o+v+e)

percentage= int(true + love)

if percentage <10 or percentage>90:
    print(f"your score is {percentage}, yo go like coke and mentos together")
elif percentage>= 40 and percentage <=50:
    print(f"your score is {percentage}, you are alright together")
else :
    print(f"your score is {percentage}.")