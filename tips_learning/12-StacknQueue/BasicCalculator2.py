class Solution:
    def calculate(self, s: str) -> int:
        """
        cases to consider:
            - multi digit numbers
            - string s starts with a negative number

        algo:
        - sign tracking last op
        - when meet a num, add num to cur_num (not stack)
        - when meet an op;
            + if is + or -, add signed cur_num
            + if is * or /, pop stack to get prev num and do op with curnum
        - then change sign to cur char and reset curnum
        """
        s = s.replace(' ','')
        stack = []
        i = 0
        num = 0
        sign = '+'
        
        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # // does not work for negative nums
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c

        return sum(stack)        

