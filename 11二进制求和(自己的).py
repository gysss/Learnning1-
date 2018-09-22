def addBinary(a, b):

    m = int(a, 2)
    n = int(b, 2)

    return bin(m + n)[2:]

def main():
    print(addBinary('1001', '11001'))


if __name__ == '__main__':
    main()
