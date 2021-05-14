#Lines 6-12 are commented to make a cleaner unittest module.  
#They can be uncommented for this module to work individually.

def isPalindrome(string):
    return string == string[::-1]

# s = input("Please enter a string: ")
# bool = isPalindrome(s)

# if bool:
#     print(s + " is a palindrome!")
# else:
#     print(s + " is not a palindrome.")