from random import *
print("You have 10 Guesses")
list = ["apple", "mango", "banana", "grapes", "watermelon"]

fruit = choice(list)
length = len(fruit)
list1 = []
for i in range(length):
    list1.append("_")
list3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(list1)
m = 10
while m > 0:

    guess = input("guess an aplhabet: ").lower()
    try:
        list3.remove(guess)
    except:
        print("You already choose this alphabet or incorrect input")
        continue
    n = 0
    for i in range(len(fruit)):
        if fruit[i] == guess:
            list1[i] = guess
            n = 1

    if n == 0:
        print("incorrect guess")
        m -= 1
        print("no of guesses left =", m)

    if "_" not in list1:
        print("You Win")
        m=5
        break

    print(list3)
    print(list1)
    print("````````````````````````````````````````````````````````````````")

if m != 5:
    print("You Lose")



