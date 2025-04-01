def subsetSums(self, arr):
		# code here
        res = []
        
        def _sub(i, n, lis, arr, res):
            if i == n:
                if len(lis) == 0:
                    res.append(0)
                else:
                    res.append(sum(list(lis)))
                return
            
            lis.append(arr[i])
            _sub(i+1, n, lis, arr, res)
            
            lis.pop()
            _sub(i+1, n, lis, arr, res)
            
        _sub(0, len(arr), [], arr, res)
        
        return res