// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

class Solution:
    def average(self, salary: List[int]) -> float:
        l = []
        for i in salary:
            if i != min(salary) and i != max(salary):
                l.append(i)
        return sum(l) / len(l)      
        