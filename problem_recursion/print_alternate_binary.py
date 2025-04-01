def generate_binary_strings(n: int):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]
    result = []
    for s in generate_binary_strings(n-1):
        a = s
        result.append(s + "0")
        if s[-1] != "1":
            result.append(s + "1")
        
    return result

# Example usage
arr = generate_binary_strings(3)
for i in arr:
      print(i,end=' ')

# This code is contributed by Susobhan Akhuli
