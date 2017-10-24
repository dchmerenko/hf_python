def search4vowels(phrase:str) -> set:
    """Return any vowels found in supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

if __name__ == "__main__":
    phrase = input('Provide a phrase to search for vowels: ')
    print(search4vowels(phrase))
