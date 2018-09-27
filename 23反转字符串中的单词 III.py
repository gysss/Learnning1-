"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序
"""
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    if s.split() == []:
        s = ""
    else:
        temp = s.split()
        ans = []
        for i in temp:
            # l = list(i)
            # l.reverse()
            # ans.append("".join(l))
            ans.append(i[::-1])
        s = " ".join(ans)
    return s


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
