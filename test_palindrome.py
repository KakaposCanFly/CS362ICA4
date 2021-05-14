import unittest
import palindrome

s = input("Please enter a string: ")

class Testing(unittest.TestCase):
    def test_isPalindrome(self):    #test guaranteed to pass
        result = palindrome.isPalindrome("racecar")
        self.assertTrue(result)
        
    def test_isPalindrome2(self):   #test guaranteed to fail
        result = palindrome.isPalindrome("kakapos")
        self.assertTrue(result)

    def test_isPalindrome3(self):   #test will fail or pass depending on user input
        result = palindrome.isPalindrome(s)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()