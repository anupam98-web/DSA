from typing import *

def subsetsWithDup(nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        def _sub(i, n, lis, arr, res):
            if i == n:
                res.add(tuple(lis))
                return
            
            lis.append(arr[i])
            _sub(i+1, n, lis, arr, res)
            
            lis.pop()
            _sub(i+1, n, lis, arr, res)
            
        _sub(0, len(nums), [], nums, res)
        
        return list(res)

if __name__ == "__main__":
    print(subsetsWithDup([1,2,2])) 

"""
https://leetcode.com/problems/subsets-ii/description/

"""