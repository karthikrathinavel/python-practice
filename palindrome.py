def palindrome_check(s):
    return s == s[::-1]
s = input("Enter your string: ")
result = palindrome_check(s)
if(result == True):
    print("Palindrome")
else:
    print("Not a palindrome")
