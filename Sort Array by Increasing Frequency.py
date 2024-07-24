﻿from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))


if __name__ == '__main__':
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))  # [3,1,1,2,2,2]
    print(Solution().frequencySort([2, 3, 1, 3, 2]))  # [1,3,3,2,2]
    print(Solution().frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))  # [5,-1,4,4,-6,-6,1,1,1]
