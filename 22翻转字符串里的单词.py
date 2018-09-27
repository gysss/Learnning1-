"""
给定一个字符串，逐个翻转字符串中的每个单词。
"""
def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    if s.split() == []:
        s = ""
    else:
        ans = s.split()
        ans.reverse()
        ans_str = " "
        s = ans_str.join(ans)
    return s

if __name__ == '__main__':
    s = "i dont like"
    print(reverseWords(s))
