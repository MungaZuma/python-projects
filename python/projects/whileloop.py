print("enter a between  1 and 5")

tries = 0

while tries < 3 :

    geuss = int(input("enter number: "))

    if geuss < 5 :
        print(" you have picked a valid number.")
        break

    else:
        print("your tries are over")
        tries += 1
        
    if tries == 3:
        print(" you have exhausted your tries.")