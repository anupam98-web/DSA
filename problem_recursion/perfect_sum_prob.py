def perfectSum( arr, target):
		# code here
        
        def _sum(i, ar, lis, target):
            if len(ar) == i:
                if sum(list(lis)) == target:
                    # print('here')
                    return 1
                return 0
            
            lis.append(ar[i])
            l = _sum(i+1, ar, lis, target)
            
            lis.pop()
            r = _sum(i+1, ar, lis, target)
            return l + r
        
        lis = []
        res = _sum(0, arr, lis, target)
        return res


if __name__ == '__main__':
    print(perfectSum([2, 3, 5, 6, 8, 10], 10)) # 3
    print(perfectSum([1, 2, 3, 4, 5], 10)) # 3


    """
    test cases passing: 1010 /1111
    gfg link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem
    """