def subset(nums):
    lis = []
    result = []
    i =0
    _subset(i, lis, nums, result)
    for i in result:
        print(i)

def _subset(i, lis, arr, result):
    if i == len(arr):
        result.append(list(lis))
        return
    
    lis.append(arr[i])
    _subset(i+1, lis, arr, result)

    lis.pop()
    _subset(i+1, lis, arr, result)


if __name__ == "__main__":
    subset([1,3])