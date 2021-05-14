#Lines 8&9 are commented out to make cleaner testing modules.  
#They can be uncommented for this module to work individually.

def countWords(s):
    res = len(s.split())
    return int(res)

# s = input("Please enter a string: ")
# print ("Word count:", countWords(s))