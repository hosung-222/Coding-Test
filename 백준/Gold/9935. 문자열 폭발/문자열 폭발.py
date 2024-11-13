s = input()
bumb = input()

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[len(stack)-len(bumb):len(stack)]) == bumb:
        for _ in range(len(bumb)): stack.pop()

if stack:
    print(*stack, sep="")

else:
    print("FRULA")