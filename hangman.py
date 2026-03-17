import random
word_list = [
    "apple", "mango", "guitar", "planet", "shadow", "bridge", "castle",
    "dragon", "forest", "jungle", "mirror", "needle", "orange", "parrot",
    "quartz", "rabbit", "silver", "temple", "umbrella", "velvet", "wallet",
    "xenon", "yellow", "zipper", "basket", "candle", "desert", "engine",
    "feather", "garden", "hammer", "island", "jacket", "kitchen", "lemon",
    "marble", "napkin", "oyster", "pencil", "queen", "rocket", "sunset",
    "turtle", "unicorn", "violin", "window", "xylophone", "yogurt", "zebra",
    "anchor", "butter", "cactus", "donkey", "eagle", "falcon", "grapes",
    "honey", "igloo", "jewel", "koala", "lantern", "magnet", "noodle",
    "ocean", "panda", "quarry", "river", "snake", "tiger", "urban",
    "vapor", "wheat", "extreme", "yarn", "zombie", "almond", "biscuit",
    "cotton", "dagger", "elbow", "fudge", "goblin", "helmet", "ivory",
    "jungle", "kettle", "lizard", "melon", "nurse", "otter", "pepper",
    "quill", "riddle", "saddle", "throne", "urchin", "venom", "walrus",
    "pixel", "copper", "bronze", "fossil", "glacier", "harbor", "insect"
] 
stages = [
    """
    ________
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |     /
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|
    |
    |
    """,
    """
    ________
    |      |
    |      O
    |      |
    |
    |
    """,
    """
    ________
    |      |
    |      O
    |
    |
    |
    """,
      """
    ________
    |      |
    |
    |
    |
    |
    """
  
]

random_word= random.choice(word_list)
random_word=random_word.lower()
display=list('_'*len(random_word))
lives=6
print(stages[6])
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
        print(stages[lives])
        print("Wrong Guess\nLives left: "+str(lives))
if '_' not in display:
    print("\t\tYOU WON!!!")
else:
    print("\t\tYOU LOST!!! Word was: " + random_word)
