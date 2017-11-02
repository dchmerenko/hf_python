<<<<<<< HEAD:ch04_code_reuse/mymodules/vsearch.py
def search4vowels(phrase:str) -> set:
    """Return any vowels found in supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
=======
import vsearch

if __name__ == "__main__":
    phrase = input('Provide a phrase to search for letters: ')
    print(vsearch.search4letters(phrase, 'abcd'))
>>>>>>> bcf3d53ce5154af0cce2f9908747a1bb115192be:ch04_code_reuse/vsearch2.py
