
def addBinary( a, b):
    lena = len(a)
    lenb = len(b)
    flag = False
    l = max(lena, lenb)
    ans = ''
    for i in range(1,l+1):
        t = (0 if i>lena else int(a[-i])) + (0 if i>lenb else int(b[-i])) + (1 if flag else 0 )
        flag = t/2==1
        ans = str(t%2) +ans
    return ('1' if flag else '0') + ans


def main():
    da = addBinary('11100', '101')
    print(da)

if __name__ == '__main__':
    main()
