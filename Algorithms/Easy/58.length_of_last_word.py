# Solution 1
def lengthOfLastWord(s):
    return len(s.split()[-1])


# solution 2
def lengthOfLastWord(s):
    len_of_last_word = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            len_of_last_word += 1
        elif len_of_last_word > 0:
            break
    return len_of_last_word
