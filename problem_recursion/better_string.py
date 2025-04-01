def betterString(s1, s2):
        # Code here
        lis1 = []
        lis2 = []
        result1 = set()
        result2 = set()
        
        def _sub(arr, i, lis, res):
            if len(arr) == i:
                res.add(tuple(lis))
                return
            lis.append(arr[i])
            _sub(arr, i+1, lis, res)
            
            lis.pop()
            _sub(arr, i+1, lis, res)
        
        _sub(s1, 0, lis1, result1)
        _sub(s2, 0, lis2, result2)
        
        # print(result1)
        # print(result2)
        if len(result1) >= len(result2):
            return s1
        else:
            return s2
        
if __name__ == '__main__':
    print(betterString("abc", "def"))

# not optimized solution.
# test cases passing 1010 /1116
# https://www.geeksforgeeks.org/problems/better-string/1?utm_source=youtube