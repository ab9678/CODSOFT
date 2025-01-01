import random
userPoints = 0
compPoints = 0
while(1):

    inp = ["r","p","s"]
    print("\nRock, Paper, Scissor, -----cut!!!\n\n")
    user = input("You->> ")

    comp = random.choice(inp)
    print("Computer->> ",comp)
    if user in inp:
        if ((user,comp) == ("s","p")) or ((user,comp) == ("r","s")) or ((user,comp) == ("p","r")):
            print("winner is user!!")
            userPoints+=1
        elif ((user,comp) == ("p","s")) or ((user,comp) == ("s","r")) or ((user,comp) == ("r","p")):
            print("winner is computer")
            compPoints+=1
        else:
            print("Its a tie")
    else:
        print("Invalid input")
    print(f"User: {userPoints},Comp: {compPoints}")

# scissor beats paper 
# rock beats scissior
# paper beats rock