import sys

def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def partition(s, i , j):
    if i >=j or isPalindrome(s, i, j):
        return 0
    
    res = sys.maxsize

    for _ in range(i, j):
        cuts = 1 + partition(s, i, _) + partition(s, _ + 1, j)
        res = min(res, cuts)
    return res

def palindromic_partition(s):
    return partition(s, 0, len(s) - 1)

if __name__ == "__main__":
    s = "aab"
    print(palindromic_partition(s)) # 1
    s = "a"
    print(palindromic_partition(s)) # 0
    s = "ab"
    print(palindromic_partition(s)) # 1