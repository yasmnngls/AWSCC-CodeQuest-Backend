print ("Enter your choice: '1' for Rock, '2' for Paper, '3' for Scissors")

hp1 = int(input("PLAYER1: "))
hp2 = int(input("PLAYER2: "))

if (hp1 >= 1 and hp1 <= 3) and (hp2 >= 1 and hp2 <= 3): 

    if not hp1 == hp2:
        if (hp1 == 1 and hp2 == 3) or (hp1 == 2 and hp2 == 1) or (hp1 == 3 and hp2 == 2):
            print("\nPlayer1 Wins!\n")
        else:
            print("\nPlayer2 Wins!\n")
    else:
        print("\nIt's a tie!\n")

else:
    print("\nInputs must be a single digit number: 1, 2, or 3 only\n")


