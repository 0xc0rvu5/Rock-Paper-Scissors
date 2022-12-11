'''
rock, paper, scissors
'''

import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to the rock, paper scissors game!')

def move(choice):
    match choice:
        case 'rock':
            print(ROCK)
        case 'paper':
            print(PAPER)
        case 'scissors':
            print(SCISSORS)
        case 0:
            print(ROCK)
        case 1:
            print(PAPER)
        case 2:
            print(SCISSORS)

CHOICE = input('What is your move? "rock", "paper", "scissors"\n').lower()
#create secondary variable to check results
CHOICE_1 = CHOICE
move(CHOICE)

print('Computer\'s choice:')
CHOICE = random.randint(0,2)
#create secondary variable to check results
CHOICE_2 = CHOICE
move(CHOICE)

CHECK = [CHOICE_1, CHOICE_2]

WIN = [['rock', 2], ['paper', 0], ['scissors', 1]]
TIED = [['rock', 0], ['paper', 1], ['scissors', 2]]
LOSE = [['rock', 1], ['paper', 2], ['scissors', 0]]

if CHECK in WIN:
    print('~/!\~ You are the Winner ~/!\~')
if CHECK in TIED:
    print('**You tied**')
if CHECK in LOSE:
    print('**You lose**')

