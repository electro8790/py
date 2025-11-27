import random
import time
number=random.randint(1,100)
def intro():
    print('may i ask your name?')
    global name
    name=input()
    print(name + ", im thinking of a number between 1 to 100.")
    if number%2==0:
        x='even'
    else:
        x='odd'
    print('this is an {} number'.format(x))
    time.sleep(0.5)
    print('go ahead start guessing')
def pick():
    guessesTaken=0
    while guessesTaken<6:
        time.sleep(0.25)
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print('the guess number is too low')
                    if guess>number:
                        print('the guess is too high')
                    if guess!=number:
                        time.sleep(0.5)
                        print('try again')
                    if guess==number:
                        break
                if guess>100 or guess<1:
                    print('the number is out of range')
                    time.sleep(0.25)
                    print('please enter the number between 1-100')
        except:
            print("i don't think that is a number")
    if guess==number:
        guessesTaken=str(guessesTaken)
        print('good job you guessed my number correct')
    if guess!=number:
        print('nope the number i was thinking was'+ str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    pick()
    print('do you want to play again')
    playagain=input()
