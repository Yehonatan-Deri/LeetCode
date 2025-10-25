from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        result = []
        while i <= n:
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(f"{i}")

            i += 1

        return result
