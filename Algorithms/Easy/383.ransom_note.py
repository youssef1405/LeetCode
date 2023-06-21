import collections

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # solution 1
    ransom_dic = collections.Counter(ransomNote)
    mag_dic = collections.Counter(magazine)

    for letter, letter_count in ransom_dic.items():
        if letter not in mag_dic or mag_dic[letter] < letter_count:
            return False
    return True

    # solution 2

    # sorted_r = sorted(ransomNote)
    # sorted_m = sorted(magazine)
    # i = 0
    # check = ''
    # for letter in sorted_r:
    #     while i < len(sorted_m):
    #         if letter == sorted_m[i]:
    #             check += letter
    #             i+=1
    #             break
    #         i += 1
    # return check == ''.join(sorted_r)
            