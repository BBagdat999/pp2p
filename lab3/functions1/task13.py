from random import randrange

def Guess_the_number(name):

    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    random_number = randrange(1, 21)
    count = 0
    flag = True
    
    while flag:
        guess = int(input())
        if random_number > guess:
            print('Your guess is too low.')
        elif random_number < guess:
            print('Your guess is too high.')
        else:
            flag = False
        count += 1
    else:
        print(f'Good job, {name}! You guessed my number in {count} guesses!')


print("Hello! What is your name?")
name = input()

Guess_the_number(name)
