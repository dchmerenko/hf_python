def search4letters(phrase:str, letters:str='aieou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


if __name__ == "__main__":
    phrase = input('Provide a phrase to search for letters: ')
    print(search4letters(letters='abcd', phrase=phrase))
