from typing import *
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def _sub(i, n, arr, lis, res, target):
            if i == n:
                if target == 0:
                    res.append(list(lis))
                return 

            else:
                if arr[i] <= target:
                    lis.append(arr[i])
                    _sub(i, n, arr, lis, res, target-arr[i])
                    lis.pop()
            _sub(i+1, n, arr, lis, res, target)

        _sub(0, len(candidates), candidates, [], res, target)
        return res


if __name__ == '__main__':
    print(combinationSum([2, 3, 6, 7], 7)) # [[2,2,3],[7]]
    print(combinationSum([2, 3, 5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
    print(combinationSum([2], 1)) # []
    print(combinationSum([1], 1)) # [[1]]
    print(combinationSum([1], 2)) # [[1,1]]
    print(combinationSum([2, 3, 6, 7], 7)) # [[2,2,3],[7]]
    print(combinationSum([2, 3, 5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
    print(combinationSum([2], 1)) # []
    print(combinationSum([1], 1)) # [[1]]
    print(combinationSum([1], 2)) # [[1,1]]
    print(combinationSum([2, 3, 6, 7], 7)) # [[2,2,3],[7]]