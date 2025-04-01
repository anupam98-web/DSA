from typing import *

def combinationSum3(k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        res = []
        def _sub(i, n, lis, arr, res, target, k):
            if i == n:
                if sum(list(lis)) == target and len(list(lis)) == k:
                    res.append(list(lis))
                return

            lis.append(arr[i])
            _sub(i+1, n , lis, arr, res, target, k)
            
            lis.pop()
            _sub(i+1, n, lis, arr, res, target, k)

        _sub(0, len(nums), [], nums, res, n, k)
        return res

if __name__ == '__main__':
     combinationSum3(3, 7) # [[1,2,4]]