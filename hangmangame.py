#python hangman game created on 17-07-19 by Pikesh for ASKNBID internship challange

import random
import string
wordlist=[] #empty list to collect words from text file
with open('words.txt') as file: #you can give your own list of words in a text file here
    data=file.readlines()
    for line in data:
        wordlist.append(line.splitlines())
answerlist=[x for xs in wordlist for x in xs]

# Shuffling the list of words so that differnt word come in a new game
random.shuffle(answerlist)
answer=list(answerlist[0])#picking up the first element for the game


display=[]
guessed=[]
missed=[]
display.extend(answer)
guessed.extend(display)


#Replacing the length of the word with "_" seprated by a space
for i in range (len(display)):
    display[i] = "_"
print(' '.join(display))

count=0
chances=0

while count < len(answer):
    guess=input("\nGuess a word: ") #guessed input from user
    guess=guess.lower() #converting to  lowercase coz all word in list are in lowercase
    for i in range(len(answer)): #iterating to each letter to match with input of user
        if answer[i]==guess and guess in guessed:
            display[i]=guess
            count=count+1 #if guessed then increment the counter
            guessed.remove(guess) #remove underscore
    if guess not in display and guess not in missed: #counting the missed words so that chance not gets decrement if key pressed twice
        missed.append(guess)
        chances=chances+1
    if chances==6:# defining the number of chances to play game
        break
    
    print(' '.join(display)+"    |missed Words: ",*missed) #printing the result in each step. join will remove "_" with correct guessed word

CORRECT_WORDS=count #correct guessed letters
TOTAL_WORDS=len(answer) # Length of letter
accur=round((CORRECT_WORDS/TOTAL_WORDS)*100,2) #calculation of its accuracy
print("Accuracy: {}%".format(accur))

if(accur==100): #Now i think you should whats going on
    print("guessed correctly")
else:
    print("'{}' not guessed correctly".format(answerlist[0]))