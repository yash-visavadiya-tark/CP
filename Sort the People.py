from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name, _ in sorted(zip(names, heights), key=lambda x: -x[1])]


if __name__ == '__main__':
    print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))  # ["Mary","Emma","John"]
    print(Solution().sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))  # ["Bob","Alice","Bob"]
