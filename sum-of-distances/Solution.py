// https://leetcode.com/problems/sum-of-distances

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d={}
        for i in range (len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[]
                d[nums[i]].append(i)
            else:
                d[nums[i]].append(i)
        answer=[0]*(len(nums))
        for key,val in d.items():
            suff=sum(val) 
            pre=0
            s=len(val)
            p = 0
            for i in val:
                pre+=i 
                p+=1
                suff-=i
                s-=1
                answer[i]=(-pre+p*i-s*i+suff)
        return answer
