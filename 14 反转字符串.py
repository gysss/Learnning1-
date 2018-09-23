def reverseString( s):
    """
    :type s: str
    :rtype: str
    """
    # 解法一：字符串转列表，反转后，列表转字符串返回
    # L = list(s)
    # L.reverse()
    # return ''.join(L)

    #解法二：直接反向返回
    return s[::-1]

def main():
    print(reverseString("Hello World"))

if __name__ == '__main__':
    main()
