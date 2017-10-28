import vsearch

if __name__ == "__main__":
    phrase = input('Provide a phrase to search for letters: ')
    print(vsearch.search4letters(phrase, 'abcd'))
