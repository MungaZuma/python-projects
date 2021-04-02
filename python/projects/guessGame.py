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

# gesi(20)

def compGesi(z):
    chini = 1
    juu = z
    jibu =""

    while jibu != "s":  
        if chini != juu:
            randno = random.randint(chini,juu)
        else:
            randno = chini
        
        jibu = input(f"je {randno} iko juu(j), chini(C) au sahihi(s): ")

        if jibu == "j":
            juu = randno - 1
        elif jibu == "c":
            chini = randno + 1

    print(f"hongera bwana computer, {randno} , ndio jibu sahihi")

compGesi(50)