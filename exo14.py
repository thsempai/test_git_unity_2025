word = input("Word!!!!!!!!!!!!!!!!!!!!!!!!!!!: ")
count_words = 1

while word != "end":
    if word[0] == "t":
        print(f"{word}!")
    word = input("Mot: ")
    count_words += 2

print(f"Nombre de mots: {count_words}")