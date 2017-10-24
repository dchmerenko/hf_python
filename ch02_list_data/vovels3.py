vovels = ['a','e','i','o','u']

found = []
word = input("Provide a phrase to search for vovels: ")

for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)
            print(letter)
