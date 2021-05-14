import unittest
import wordCount

s = input("Please enter a sentence: ")

class Testing(unittest.TestCase):
    def test_wordCount(self):     #test guaranteed to pass
        result = wordCount.countWords("This is an activity")
        self.assertEqual(result, 4)

    def test_wordCount2(self):    #test guaranteed to fail
        result = wordCount.countWords("This is not")
        self.assertEqual(result, 43)

    def test_wordCount3(self):    #test will fail only if the word count (result) = 0
        result = wordCount.countWords(s)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()