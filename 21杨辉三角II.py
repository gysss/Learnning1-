"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return []
    elif rowIndex == 1:
        return [1,1]
    else:
        temp = [1,1]
        for i in range(3,rowIndex+2):
            ans = [1]
            for j in range(1,i-1):
                ans.append(temp[j-1]+temp[j])
            ans.append(1)
            temp = ans
        return ans

if __name__ == '__main__':
    print(getRow(2))

