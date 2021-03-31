import random

def gesi(x):
    randomNo = random.randint(1,x)
    jaribu = 0

    while jaribu != randomNo:
        jaribu = int(input(f"chagua nambari kati ya 1 na {x}: "))
        
        if jaribu < randomNo:
            print("pole jaribu tena. nambari uliochagua iko chini.")
        elif jaribu > randomNo:
            print("pole jaribu tena. nambari uliochagua iko juu.")

    print(f"Hongera umechagua namba sahihi: {randomNo}")

gesi(20)