symbol = input("Укажите символ для замены: ")

with open("keys.txt", "r") as file_keywords:
    words_to_replace = file_keywords.read().splitlines()

with open("data.txt", "r") as file_text:
    content = file_text.read()

for word in words_to_replace:
    content = content.replace(word, symbol * len(word))

with open("result.txt", "w") as file_result:
    file_result.write(content)

print("Обработка завершена. Итог записан в result.txt.")
