vovels = ['a','e','i','o','u']

word = "Milliways"
found = []

for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)
            print(letter)
