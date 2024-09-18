from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = [[1]] * numRows
    print(res)
    for i in range(numRows):
        res[i] = [1] * (i + 1)
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res



if __name__ == '__main__':
    print(generate(5))
