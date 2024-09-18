import random
def Q_14(arr:list)->list:
    n = len(arr)
    for i in range(n):
        index = random.randint(i, n-1)
        # swap
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
    return arr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    print(Q_14(arr1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
