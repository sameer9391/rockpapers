import random
t=0
while True:
    print("\n1) Rock")
    print("\n2) Paper")
    print("\n3) Scissors\n")
    selection=int(input("Enter player's Throw\n"))
    if(selection==1):
        p='Rock'
    elif(selection==2):
        p="Paper"
    else:
        p="Scissors"
    print("\n")
    print('player throws',p)
    throws=["Rock","Paper","Scissors"]
    c = random.choice(throws)
    print("computer Throws",c)
    if(c == p):
        print('Its Tie Game')
    elif(p== "Paper"):    
        if(c == "scissors"):
           print("Computer Win!")
        elif(c=="Rock"):
            print("Player Wins!")
            t=t+1
    elif(p == "Rock"):
        if(c == "Paper"):
            print("Computer Win!")
        elif(c=="scissors"):
            print('Player Wins!')
            t=t+1
    elif(p=="Scissors"):
        if(c=="Rock"):
            print("Computer Win!")   
        elif(c=="Paper"):
            print("Player Wins!")
            t=t+1
    print("\n")
    print("1)Play Again")
    print("2)Quit")
    se=int(input("Enter choice"))
    if(se==2):
        break
print("Number of times player winis=",t)
    
    
        
                
