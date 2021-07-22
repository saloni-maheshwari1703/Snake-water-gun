import random
list = ['s','w','g']
chance = 5
no_of_chance = 0
computer_point = 0
human_point = 0
print("\t\t\t\tSnake,Water,Gun\n\n")
print("s for Snake \nw for Water \ng for Gun\n")
while(no_of_chance < chance):
    _input = input("Snake,Water,Gun\n")
    _random = random.choice(list)
    if _input == _random :
        print("Tie both get 0 points\n")
    elif (_input =='s') and (_random =='g') :
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif (_input =='g') and (_random =='w') :
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif (_input =='w') and (_random =='s') :
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    else :
        print("u enter wronge input\n")
    no_of_chance = no_of_chance + 1
    print(f"{no_of_chance} chance is use out of {chance}\n")
print("game over !!!\n")
if computer_point == human_point :
    print("Game is tie\n")
elif computer_point > human_point :
    print("computer wins the game\n")
else :
    print("human wins the game\n")
