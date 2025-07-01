
print('                           Guess Game ')
print('Guess a number from 0 to 10')
print('')
#Random Number Setup.......................///
import random
n = random.randint(0,10)
x = 0
b = 3
#While loop Setup..........................///
while x < b:
    x += 1
    guess = int(input('Guess: '))
#Errors...................................///
    if guess > 10:
        print('Error! Choose a number from 0 to 10.')
    elif guess < 0:
        print('Error! Choose a number from 0 to 10.')
#Guess Setup................................///
    if guess == n:
        print('Congratulations')
        break
else:
    print('Sorry! You Failed!')
    print('The answer is', n)


