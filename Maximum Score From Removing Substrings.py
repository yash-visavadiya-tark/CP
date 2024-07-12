class Solution:
    def maximum_gain(self, s: str, x: int, y: int) -> int:
        total_score = 0

        if x > y:
            s, score = self.remove_all_occurences(s, x, 'a', 'b')
            total_score += score
            s, score = self.remove_all_occurences(s, y, 'b', 'a')
            total_score += score
        else:
            s, score = self.remove_all_occurences(s, y, 'b', 'a')
            total_score += score
            s, score = self.remove_all_occurences(s, x, 'a', 'b')
            total_score += score

        return total_score

    def remove_all_occurences(self, s: str, score_per_removal: int, start: str, end: str) -> list:
        stack = []
        score = 0

        for c in s:
            if c == end and stack and stack[-1] == start:
                stack.pop()
                score += score_per_removal
            else:
                stack.append(c)

        return [''.join(stack), score]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximum_gain("cdbcbbaaabab", 4, 5))  # 19
    print(sol.maximum_gain("aabbaaxybbaabb", 5, 4))  # 20
