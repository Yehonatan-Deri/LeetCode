from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = [[1]] * numRows
    print(res)
    for i in range(numRows):
        res[i] = [1] * (i + 1)
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res


def generate2(numRows: int) -> List[List[int]]:
    res = [[1]]

    for i in range(numRows - 1):
        temp_row = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp_row[j] + temp_row[j + 1])
        res.append(row)

    return res

if __name__ == '__main__':
    print(generate(5))
