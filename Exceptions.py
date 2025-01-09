import random
import string

letter = string.ascii_lowercase
words = ["apple", "banana", "cherry", "orange", "pear"]
choice = words[random.randint(0,4)]
letters = ["_"] * len(choice)
print(letters)
chances = 5
while True:
        if chances == 0:
            break
        else:
            if "_" not in letters:
                break
            else:
                try:
                    guess = input("Отгадайте букву").lower()
                    if guess not in letter:
                        print("заново пиши")
                        continue
                    else:
                        if guess in choice:
                            if choice=="apple" and guess == "p":
                                letters[1] = "p"
                                letters[2] = "p"
                                print(letters)
                            elif choice == "banana" and guess == "a":
                                letters[1] = "a"
                                letters[3] = "a"
                                letters[5] = "a"
                                print(letters)
                            elif choice == "banana" and guess == "n":
                                letters[2] = "n"
                                letters[4] = "n"
                                print(letters)
                            elif choice == "cherry" and guess == "r":
                                letters[3] = "r"
                                letters[4] = "r"
                                print(letters)
                            else:
                                index = choice.index(guess)
                                letters[index] = guess
                                print(letters)
                        else:
                            print(letters)
                            chances = chances - 1
                except ValueError:
                    print("заново")
