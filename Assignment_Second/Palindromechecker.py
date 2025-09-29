# Palindrome
def palindrome(s):
    if s == s[::-1]:
        print(f"The word {s} is palindrome")
    else:
        print(f"The word isn't {s} is palindrome")


string = str(input("Enter a word "))
palindrome(string)
