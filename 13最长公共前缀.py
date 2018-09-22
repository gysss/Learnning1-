def longestCommonPrefix( strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    minlen = 999
    if (len(strs) == 0):
        return ans
    if (len(strs) == 1):
        return strs[0]
    for i in range(len(strs)):
        minlen = minlen if minlen < len(strs[i]) else len(strs[i])
    for j in range(0, minlen):
        temp = 0
        for k in range(1, len(strs)):
            if (strs[0][j] in strs[k][j]):
                temp = temp + 1
        if (temp != (len(strs) - 1)):
            ans = strs[0][0:j]
            return ans
    return strs[0][0:minlen]

def main():
    print(longestCommonPrefix(["aa", "a"]))

if __name__ == '__main__':
    main()
