class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0
        j = n-1
        for _ in range(0, n-1):
            if numbers[i] + numbers[j] > target:
                while (j>i and numbers[i] + numbers[j] > target):
                    j = j-1
            if numbers[i] + numbers[j] < target:
                while (i<j and numbers[i] + numbers[j] < target):
                    i = i+1
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
        
        return [i+1,j+1]