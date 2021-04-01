import random

def play():
    
    player =""
    computer = random.choice(['r','p','s'])

    
    while (player != "r") or (player != "p") or (player != "s"):
        player = input("what do you select? rock(r), paper(p) or sciscors(s): ")
        print("please select a valid choice")
        
        
        if player == computer:
            return "it's a tie"
        if is_win(player, computer):
            return "you win"
                
        return "you lost"

def is_win(player1, cpu):
    if (player1 =="r" and cpu == "s") or (player1 =="s" and cpu == "p") or (player1 =="p" and cpu == "r"):
        return True


print(play())