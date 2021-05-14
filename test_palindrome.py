import unittest
import palindrome

s = input("Please enter a string: ")

class Testing(unittest.TestCase):
    def test_isPalindrome(self):    #guaranteed success
        result = palindrome.isPalindrome("racecar")
        self.assertTrue(result)
        
    def test_isPalindrome2(self):   #guaranteed failure
        result = palindrome.isPalindrome("kakapos")
        self.assertTrue(result)

    def test_isPalindrome3(self):   #pass or fail depending on input
        result = palindrome.isPalindrome(s)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()