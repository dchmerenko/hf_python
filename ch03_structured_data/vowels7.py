vowels = {'aeiou'}
word = input('Provide a phrase to search for vowels: ')
found = []

found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)
