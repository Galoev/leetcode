from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        cur_dist = 0
        i = 0
        
        if seats[0] != 1:
            while seats[i] != 1:
                i += 1
                cur_dist += 1
            max_dist = max(max_dist, cur_dist)
            cur_dist = 0
        
        while i < len(seats):
            i += 1
            while i < len(seats) and seats[i] != 1:
                cur_dist += 1
                i += 1
            if i == len(seats) and seats[-1] != 1:
                max_dist = max(max_dist, cur_dist)
                continue

            dist = cur_dist // 2 + cur_dist % 2
            max_dist = max(max_dist, dist)
            cur_dist = 0
    

        return max_dist

if __name__ == "__main__":
    # seats = [1,0,0,0,1,0,1]
    seats = [0,1,0,0,0,0]
    print(Solution().maxDistToClosest(seats))