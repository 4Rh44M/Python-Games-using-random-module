import random
word_list=["Apple","Pen","Stomach","Arrow","Computer","Python","Cartoon"]
random_word= random.choice(word_list)
random_word=random_word.lower()
display=list('_'*len(random_word))
lives=5
while lives>0 and '_' in display:
    print(f"\n{"".join(display)}")
    user_guess=input("Guess an alphabet: ").lower()
    if user_guess in random_word:
        print("Correct Guess!!")
        for i in range(len(random_word)):
            if random_word[i] == user_guess:
               display[i] = user_guess
    else:
        lives-=1
        print("Wrong Guess\nLives left: "+str(lives))
if '_' not in display:
    print("You Won!!!")
else:
    print("You Lost! Word was: " + random_word)