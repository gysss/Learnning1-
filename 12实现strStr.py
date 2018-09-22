"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。


"""


def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    lenb = len(needle)
    if (lenb == 0):
        return 0
    if (needle in haystack):
        return haystack.find(needle)
    else:
        return -1

def main():
    print(strStr('Hello', 'll'))

if __name__ == '__main__':
    main()
