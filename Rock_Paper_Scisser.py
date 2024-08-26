# Rock wins against scissors
# ; paper wins against rock;
#  and scissors wins against paper.

# Rock = 1
# Paper =0
# Scissor = -1
import random

computer =random.choice([1,0,-1])

youstr = (input("Enter Your Choice ="))

youDict={ "R":1,"P":0,"S":-1}

reverseDict={1:"Rock",0:"Paper",-1:"Scissor"}
you=youDict[youstr]

print(f"Computer Choice ..{reverseDict[computer]} | You choice... {reverseDict[you]}")
if(computer==you):
    print("Match Draw...")
else:
    if(computer == 1 and you == 0):
        print("You Win ..")
    elif(computer == 1 and you == -1):
        print("You Loss ..")
    elif(computer == 0 and you == 1):
        print("You loss ..")
    elif(computer == 0 and you == -1):
        print("You Win ..")
    elif(computer == -1 and you == 0):
        print("You loss ..")
    elif(computer == -1 and you == 1):
        print("You Win ..")
    else:
        print("Some thing wrong enter....")

