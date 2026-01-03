class flashcards:
    def __init__(self,word,meaning):
        self.word=  word
        self.meaning=meaning
    def __str__(self):
        return self.word+' ('+self.meaning+')'
flash=[]
print('welcome to the flashcard application')
while(True):
    word=input('enter a word to add to flashcard')
    meaning=input('enter the meaning of the word')
    flash.append(flashcards(word,meaning))
    option=int(input('enter 0.,if you want to add another flash card or to exit type 1'))

    if(option):
        break
print('/n Your flashcards')
for i in flash:
    print('>',i)
