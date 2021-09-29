print("                                                      "
      "                     STONE, PAPER AND SCISSOR GAME")
print("\n\n")
from random import *

def Pic(num):
    if num == 0:
        print('''
                       ,--.--._
                ------" _, \___)
                        / _/____)
                        \//(____)
                ------\     (__)
                       `-----"
 ''')
    if num == 1:
        print('''
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                     |    |
''')
    if num == 2:
        print('''
                    .-.  _
                    | | / )
                    | |/ /
                   _|__ /_
                  / __)-' )
                  \  `(.-')
                   > ._>-'
                  / \/
''')

n = int(input("How many times u want to play: "))
your_score = 0
comp_score = 0

while n:
    print("write 0 for stone or 1 for paper or 2 for scissor")
    num1 = int(input(">>> "))
    print("                        YOU")
    Pic(num1)
    print("\n")
    print("                      COMPUTER")
    print("\n")
    num2 = randint(0, 2)
    Pic(num2)
    if num1 == num2:
        your_score += 0
        comp_score += 0
    if (num1 == 2 and num2 ==1) or (num1 == 1 and num2 == 0) or (num1 == 0 and num2 == 2):
        your_score += 1
    if (num2 == 2 and num1 ==1) or (num2 == 1 and num1 == 0) or (num2 == 0 and num1 == 2):
        comp_score += 1

    n -= 1

if your_score > comp_score:
    print("HURRY!!! YOU WIN")
elif your_score == comp_score:
    print("OHHH!!! GAME TIED")
else:
    print("SORRY YOU LOSE")

print(f"Your score is {your_score}")
print(f"Computer score is {comp_score}")
input()