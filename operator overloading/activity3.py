import random
class fruitquiz:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print('what is the colour of {}'.format(fruit))
            user_answer=input()
            if (user_answer.lower()==color):
                print('Correct answer')
            else:
                print('Incorrect answer')
            options=int(input('enter 0 to continue and 1 to exit'))
            if (options):
                break
print('welcome to our fruit quiz')
Fquiz=fruitquiz()
Fquiz.quiz()