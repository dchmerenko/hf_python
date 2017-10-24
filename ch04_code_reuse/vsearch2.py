def search4vowels(phrase:str) -> set:
    """Return any vowels found in supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


if __name__ == "__main__":
    phrase = input('Provide a phrase to search for letters: ')
    print(search4letters(phrase, 'abcd'))
