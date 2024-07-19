from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []

        for row in matrix:
            min_index = row.index(min(row))
            min_value = row[min_index]

            if all(row[min_index] >= matrix[i][min_index] for i in range(len(matrix))):
                lucky_numbers.append(min_value)

        return lucky_numbers


if __name__ == '__main__':
    print(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
