def palindrome(n):
    string = ""
    for i in n:
        if i.isalnum():
            string += i.lower()

    return string == string[::-1]

print(palindrome("A man a plan a canal Panama"))
print(palindrome("Hello"))