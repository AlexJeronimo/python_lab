def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


# print(search4vowels('ou yeah'))


# help(search4vowels)


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


# phrase1 = 'life, the universe, and everything'
# letters1 = 'aeiou'
#
# print(search_for_letters(phrase1, letters1))
# print(search_for_letters(phrase1))
