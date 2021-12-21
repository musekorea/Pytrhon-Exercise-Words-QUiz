from db import words  # db.py occurs Error
import random

print("*" * 39)
print("⭐ Welcome to OOP terminology test ⭐")
print("*" * 39)

quiz = list(words.values())  # in List
quiz = random.sample(quiz, len(quiz))  # This has a Return

for word in quiz:
    for key, value in words.items():
        if value == word:
            result = key
            break
        else:
            continue

    while True:
        answer = input(f"{word} in English ➡  ")
        if answer.lower() == result.lower():
            print("💚 Correct")
            break
        else:
            print("❌ Wrong answer, try again")
            continue

print("🏆 Great Job!!!")
