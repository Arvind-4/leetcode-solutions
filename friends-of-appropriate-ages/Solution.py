// https://leetcode.com/problems/friends-of-appropriate-ages

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        dicto = Counter(ages)
        for me in dicto:
            my_age_count = dicto[me]
            for age in dicto:
                if not (age <= 0.5 * me + 7 or age > me):
                    if age != me :
                        count += dicto[age] * my_age_count
                    else:
                        count += int(my_age_count *(my_age_count - 1))
        return count