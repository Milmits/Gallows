# Код написан 01.11.2023
# Автор: Кучук Милан Михайлович
print("\t\tПрограмма Кучук")
print("Виселица\n")

import random

HANGMAN = (
    """
    ------
    !    !
    !
    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !
    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  -+-
    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  /-+-
    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  /-+-/
    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  /-+-/
    !    !
    !
    !
    !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  /-+-/
    !    !
    !    !
    !   !
    !   !
    !
    !
---------------    
    """,
    """
    ------
    !    !
    !    0 !  /-+-/
    !    !
    !    !
    !   !  !
    !   !  !
    !
    !
---------------    
    """
)

WORDS = ("MAMA", "DEREVO", "RIVER", "LIZA", "NEGR")
MAX_WRONG = len(HANGMAN) - 1
wrong = 0
word = random.choice(WORDS)
so_far = "_" * len(word)
used = []

print("Добро пожаловать в игру вислеица, удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Вы уже использовали такеи буквы как\n", used)
    print("На данный момент наше слово выгдлядит так:\n", so_far)
    guess = input("Введите букву")
    guess = guess.upper()
    while guess in used:
        print("Такая убква уже была использовна")
        guess = input("Введите букву")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nБуква", guess, "есть в слове")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("Такой буквы нет в слове")
        wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("К сожалению вас повесили!")
    else:
        print("Вы отгадали!")
print("Было загаданно слово", word)
