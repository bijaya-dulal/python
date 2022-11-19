
#from xmlrpc.client import FastMarshaller


def add (num1, num2):
    return num1+num2
def subtract ( num1,num2):
    return num1-num2
def multiply(num1, num2):
    return num1* num2
def divide (num1, num2):
    return num1/num2
operations={"+":add,"*":multiply,"/":divide,"-":subtract,}

def calculator():
    should_continue = True
    first_num=float(input("enter first number:"))
    while should_continue:   
        second_num= float(input("enter second number:"))
        for symbol in operations:U
            print(symbol)
            
        operation=input("enter the symbol gien above:")
        cfunction=operations[operation]
        answer=cfunction(first_num,second_num)
        print(f"{first_num} {operation} {second_num}={answer}") 
        choice=input(f"type y if you t want to calculate further with {answer}, type n for new calculator and f for off")
        if choice=="y":
            first_num=answer
            
        elif choice=="n":

            calculator()
        else:
            print('bye')    
            should_continue=False
         
            
calculator()
