class Solution:
    def reverse_parentheses(self, s: str) -> str:
        st = []

        for ch in s:
            if ch == ')':
                self.reverse_till_opening_bracket(st)
            else:
                st.append(ch)

        return ''.join(st)

    def reverse_till_opening_bracket(self, st):
        a = []

        while st and st[-1] != '(':
            a.append(st.pop())

        st.pop()

        for ch in a:
            st.append(ch)


if __name__ == '__main__':
    print(Solution().reverse_parentheses('(u(love)i)'))
