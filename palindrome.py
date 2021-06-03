import re


def is_palindrome(string: str) -> bool:
    return bool(string) and string == string[::-1]


def prepare_string(string: str) -> str:
    """ Remove punctuation marks, spaces and convert to small case """
    result = re.sub(r'[^\w\s]', '', string)
    return result.lower().replace(' ', '')


def find_max_palindrome(string: str) -> str or None:
    """ Searches for a palindrome substring maximum length in the input string """
    string = prepare_string(string)
    length = len(string)
    if not length:
        return None
    all_substrings = (string[i:j+1] for i in range(length) for j in range(i, length))
    for sub in sorted(all_substrings, key=len, reverse=True)[1:]:  # Skip first sub. This is the input string
        if is_palindrome(sub):
            return sub
