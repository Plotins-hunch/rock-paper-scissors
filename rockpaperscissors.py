rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
computer_choice = int(random.randint(0,2))
rock_paper_scissors = [rock, paper, scissors]

you_choice = int(input('What do you choose. Type 0 for rock, 1 for paper, and 2 for scissor\n'))

computer_decision = rock_paper_scissors[computer_choice]
try:
    you_decision = rock_paper_scissors[int(you_choice)]
except:
    print('invalid number')
    quit()
#or: if you_choise > 2: print('invalid input')
print(f'You chose: \n {you_decision}\n')
print(f'Computer chose: \n {computer_decision}\n')
#rock wins against scissors
if you_choice == 0 and computer_choice == 2 :
  print('You won')
#paper wins against rock
elif you_choice == 1 and computer_choice == 0 :
  print('You won')
#scissors win against paper
elif you_choice == 2 and computer_choice == 1 :
  print('You won')
elif you_choice == computer_choice:
  print('It\'s a draw')
elif you_choice > 2:
    print('Invalid number')
else:
    print('You lost')