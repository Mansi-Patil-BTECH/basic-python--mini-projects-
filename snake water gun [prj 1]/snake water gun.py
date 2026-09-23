#the snake water gun game 
print("Snake, Water , Gun...\nwish you luck..\nlets see what does computer choooseee🤔")
print("_________________________________ \nGame starts")
import random

def game_winner(user, computer):
    if user == computer:
        return None
    # Snake vs Water
    if user == "s" and computer == "w":
        return True
    if user == " w" and computer == "s":
        return False
    # Water va Gun
    if user == "w" and computer == "g":
        return True
    if user == " g" and computer == "w":
        return False
    # Gun vs Snake
    if user == "g" and computer == "s":
        return True
    if user == " s" and computer == "g":
        return False

rand_no = random.randint(1, 3)


print("Computer's turn : Snake {s} , Water {w} , Gun{g}")
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"


user = input("Your turn : Snake {s} , Water {w} , Gun{g}\n").lower()

result = game_winner(user,computer) #Return true if you win..False if you lose...None if its a Draw
print(f"\nYour choice : {user}")
print(f"\nComputer's choice : {computer}")

if result is None:
    print("Its a draw!")
elif result is True :
    print("You are the winner!")
else:
    print("Computer is the winner!")

print("THANK YOU!👍")  

print("Run the program again to play the next turn (😭beginer level programer naa)")