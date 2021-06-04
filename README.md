# palindrome
This is a simple program that finds a palindrome substring in an input string maximum length.

A simple algorithm is used:
1) We collect all the substrings. (E.g. input_string = 'abac'. all_subs = ['a', 'ab', 'aba', 'abac'])
2) Then we sort by length. (['abac', 'aba', 'ab', 'a',])
3) Check each substring if it is a palindrome. If so, we immediately return the result to the client.

* Python 3.9

# launch
To run program at the command line, enter: 

**python palindrome.py**

# test
To run tests at the command line, enter: 

**python -m unittest test_palindrome.py**
