squares = [x**2 for x in range(1, 11)]
print(squares)
try:
    sentence = input("Напишите предложение")
    letters = [word[0] for word in sentence.split()]
    print(letters)
except ValueError:
    print("Заново")
try:
    words = input("слова")
    upper = [s.upper() for s in words.split()]
    print(upper)
except ValueError:
    print("Заново")
try:
    word = input("Напиши слова")
    long_words = [w for w in word.split() if len(w) > 5]
    print(long_words)
except:
    print("Заново")