# given a number we have to pinrt all the valid parenthesis which are valid.

def print_parenthesis(n):

    def _print_parenthesis(n, open, close, s):
        if close == n:
            print(s)
            return
        if open < n:
            _print_parenthesis(n, open+1, close, s+"(")
        if close < open:
            _print_parenthesis(n, open, close+1, s+")")
    _print_parenthesis(n, 0, 0, "")

print(print_parenthesis(4))