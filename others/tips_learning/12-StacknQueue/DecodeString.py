class Solution:
    def decodeString(self, s: str) -> str:
        """
        use a stack: 
        - add each chars into stack 
        - when meet with a closing bracket, pop out all chars until meet an opening bracket
        - next, pop out one more (guaranteed a num)
        - then push back into stack the result (num times the chars popped out)
        
        => use a temp list to store popped out chars
        """
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                
                # pop the open bracket
                stack.pop()

                # pop the number k
                temp_k = []
                while stack and stack[-1].isnumeric():
                    temp_k.append(stack.pop())
                k = int("".join(reversed(temp_k)))
                
                # push in the decoded part
                for _ in range(k):
                    for num in reversed(temp):
                        stack.append(num)
        return "".join(stack)
