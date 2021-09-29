# black jack game
from math import *
from random import *
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(player, string):
    drawn = choice(list)
    player.append(drawn)
    print(f"{string} drawn card is {drawn}")


user = []
computer = []

playing = True

while playing:
    draw_card(computer,"Computer")
    draw_card(user, "User")
    draw_card(user, "User")
    draw_again = input("Do u want to draw next card?, write 'yes' or 'no': ")
    if draw_again == "yes":
        draw_card(user, "User")
        print(f"Your total points are {sum(user)}")
    else:
        print(f"Your total points are {sum(user)}")
    if sum(user) > 21:
        print(f"Your total {sum(user)} is greater than 21")
        print("Therefore, You lose")
        break


    win = 0

    for i in range(2):
        if sum(computer) < sum(user):
            draw_card(computer, "Computer")
            if sum(computer) > 21:
                print(f"Computer total {sum(computer)} is greater than 21")
                print("Therefore, You lose")
                break
        if sum(computer) > sum(user):
            print(f"Computer total points are {sum(computer)}")
            print("You lose..!!")
            win = 1
            playing = False
            break
        elif sum(computer) == sum(user):
            print(f"Computer total points are {sum(computer)}")
            print("Game Drawn")
            playing = False
            break


    if win == 0:
        print(f"Computer total points are {sum(computer)}")
        print("You win")
        playing = False



