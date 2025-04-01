from typing import List

def isSubsetPresent(n: int, k: int, a: List[int]) -> bool:
    memo = {}

    def _sumSubset(i: int, current_sum: int) -> bool:
        if current_sum == k:
            return True
        if i >= n or current_sum > k:
            return False
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        # Include the current element
        include = _sumSubset(i + 1, current_sum + a[i])
        
        # Exclude the current element
        exclude = _sumSubset(i + 1, current_sum)

        memo[(i, current_sum)] = include or exclude
        return memo[(i, current_sum)]

    return _sumSubset(0, 0)

if __name__ == '__main__':
    print(isSubsetPresent(94, 84, list(map(int, ("22 17 19 46 48 27 22 39 20 13 18 50 36 45 4 12 23 34 24 15 42 12 4 19 48 45 13 8 38 10 24 42 30 29 17 36 41 43 39 7 41 43 15 49 47 6 41 30 21 1 7 2 44 49 30 24 35 5 7 41 17 27 32 9 45 40 27 24 38 39 19 33 30 42 34 16 40 9 5 31 28 7 24 37 22 46 25 23 21 30 28 24 48 13".split(" ")))))) # True)


