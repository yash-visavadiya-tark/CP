from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []
        for num in nums:
            mapped_num = ''
            for ch in str(num):
                mapped_num += str(mapping[int(ch)])
            mapped_nums.append((num, int(mapped_num)))

        return [num for num, _ in sorted(mapped_nums, key=lambda x: x[1])]


if __name__ == '__main__':
    print(Solution().sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]))  # [338,38,991]
