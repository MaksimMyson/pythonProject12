text = input("Введіть текст: ")
reserved_words = input("Ведіть список  зареєстрованих слів: ")
words = text.split()
for i in range(len(words)):
    word = words[i].strip('.,!?').lower()
    if word in reserved_words:
        words[i] = words[i].upper()
        new_text = ' '.join(words)
        print("Замінений текст:")
        print(new_text)
