import wordCount
#to run, type pytest -s pytest_wordCount.py
s = input("Please enter a sentence: ")

def test_answer():      #test guaranteed to pass
    assert wordCount.countWords("This is an activity") == 4

def test_answer2():     #test guaranteed to fail
    assert wordCount.countWords("This is not") == 43

def test_answer3():     #test will fail only if the word count (result) = 0
    assert wordCount.countWords(s) != 0