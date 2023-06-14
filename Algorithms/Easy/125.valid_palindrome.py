def isPalindrome(s):
    filtered_chars = filter(lambda ch: ch.isalnum(), s)
    lowercase_filtered_chars = map(lambda ch : ch.lower(), filtered_chars)
    filtered_chars_list = list(lowercase_filtered_chars)
    return filtered_chars_list == filtered_chars_list[::-1]
    
print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car')) 
print(isPalindrome(' '))  