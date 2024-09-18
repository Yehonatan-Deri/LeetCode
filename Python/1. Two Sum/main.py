# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}

    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic.get(target - nums[i]), i]
        dic[nums[i]] = i

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
