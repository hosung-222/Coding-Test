import sys
sys.setrecursionlimit(10000)

def solve(n):
    result = []
    operators = ["+", "-", " "]

    def dfs(index, expr):
        if index > n:
            eval_expr = expr.replace(' ', '')
            if eval(eval_expr) == 0:
                result.append(expr)
            return
        
        num_str = str(index)
        for op in operators:
            dfs(index+1, expr + op + num_str)

    dfs(2, '1')
    result.sort()
    for expr in result:
        print(expr)

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
    print()