import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_words():
    path = os.path.join(BASE_DIR, "word.txt")
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()

def show_gallows(stage):
    path = os.path.join(BASE_DIR, "gallows", f"{stage}.txt")
    with open(path, encoding="utf-8") as f:
        print(f.read())

words = load_words()
word = random.choice(words)
so_far = "_" * len(word)
used = set()
count =0
count_max = 7

print("Виселица")

while count < count_max and so_far != word:
    show_gallows(count)
    print("Слово:", " ".join(so_far))
    print("Буквы:", ", ".join(sorted(used)) if used else "-")

    guess = input("Введите букву: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Введите одну букву.")
        continue

    if guess in used:
        print("Эта буква уже была.")
        continue

    used.add(guess)

    if guess in word:
        so_far = "".join(
            guess if word[i] == guess else so_far[i]
            for i in range(len(word))
        )
    else:
        count += 1

if so_far == word:
    print("\nПобеда! Слово:", word)
else:
    show_gallows(count)
    print("\nПроигрыш. Слово было:", word)

input("\nНажмите Enter для выхода...")