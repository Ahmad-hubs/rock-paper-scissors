# Rock wins against scissors
# ; paper wins against rock;
#  and scissors wins against paper.

# Rock = 1
# Paper =0
# Scissor = -1
import random


print("Enter : Rock for R, Paper for P, Scissor for S \nPress any other Button Game end....")


while True :

    computer =random.choice([1,0,-1])
    computerDict={ 1:"R",0:"P",-1:"S"}
    com=computerDict[computer]

    reverseDict={1:"Rock",0:"Paper",-1:"Scissor"}
    youreverseDict={"R":"Rock","P":"Paper","S":"Scissor"}

    youstr =input("Enter Your Choice =")

    if  youstr != "R" and youstr != "P" and youstr != "S":
        print("Some input wrong enter....")
        print("Game End....")
        break
    elif(com==youstr):
        print("Match Draw...")
    else:
        if (com == "R" and youstr == "P"):
            print("You Win ..")
        elif (com == "R" and youstr == "S"):
            print("You Loss ..")
        elif (com == "P" and youstr == "R"):
            print("You loss ..")
        elif (com == "P" and youstr == "S"):
            print("You Win ..")
        elif (com == "S" and youstr == "P"):
            print("You loss ..")
        elif (com == "S" and youstr == "R"):
            print("You Win ..")

    print(f"Computer Choice ..{reverseDict[computer]} | You choice... {youreverseDict[youstr]} \n")
    
    

