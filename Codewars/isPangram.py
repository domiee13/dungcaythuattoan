# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# Example
# pangram = "The quick, brown fox jumps over the lazy dog!"
# Test.assert_equals(is_pangram(pangram), True)

import string

#My solution
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s.lower():
            return False
    return True

#Best solution 
def isPangram(s):
    return set(string.ascii_lowercase)<=set(s.lower())