import palindrome
#to run, type pytest -s pytest_palindrome.py
s = input("Please enter a string: ")


def test_answer():  #test guaranteed to pass
    assert palindrome.isPalindrome("racecar") == True

def test_answer2(): #test guaranteed to fail
    assert palindrome.isPalindrome("kakapos") == True

def test_answer3(): #test will fail or pass depending on user input
    assert palindrome.isPalindrome(s) == True