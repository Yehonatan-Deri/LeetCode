from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_pointer = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[end_pointer] = nums1[m - 1]
                m -= 1
            elif nums1[m - 1] <= nums2[n - 1]:
                nums1[end_pointer] = nums2[n - 1]
                n -= 1
            end_pointer -= 1

        while n > 0:
            nums1[end_pointer] = nums2[n - 1]
            n -= 1
            end_pointer -= 1


# Test cases
def test_case_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected_output = [1, 2, 2, 3, 5, 6]

    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected_output, f"Test case 1 failed. Expected: {expected_output}, got: {nums1}"
    print("Test case 1 passed")


def test_case_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected_output = [1]

    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected_output, f"Test case 2 failed. Expected: {expected_output}, got: {nums1}"
    print("Test case 2 passed")


def test_case_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected_output = [1]

    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected_output, f"Test case 3 failed. Expected: {expected_output}, got: {nums1}"
    print("Test case 3 passed")


def test_case_4():
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    expected_output = [1, 2, 3, 4, 5, 6]

    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected_output, f"Test case 4 failed. Expected: {expected_output}, got: {nums1}"
    print("Test case 4 passed")


if __name__ == '__main__':
    # test_case_1()
    # test_case_2()
    # test_case_3()
    test_case_4()