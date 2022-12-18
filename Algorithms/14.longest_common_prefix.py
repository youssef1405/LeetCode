
def longestCommonPrefix(strs):
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix( ["dog","racecar","car"]))
