import random
playing=True
num=str(random.randint(1,10))
while playing:
    guess=input('Guess a number between 1 to 10')
    if num == guess:
        print('correct')
        print('the number was',num)
    else:
        print('you have guessed wrong')
