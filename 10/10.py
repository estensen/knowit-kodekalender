stack = []
data = []


with open('input.spp') as f:
    data = f.read().split('\n')


for line in data:
    for el in line:
        if el == ' ':
            stack.append(31)
        elif el == ':':
            stack = [sum(stack)]
        elif el == '|':
            stack.append(3)
        elif el == "'":
            stack.append(stack.pop()+stack.pop())
        elif el == '.':
            A = stack.pop()
            B = stack.pop()
            stack.append(A-B)
            stack.append(B-A)
        elif el == '_':
            A = stack.pop()
            B = stack.pop()
            stack.append(A*B)
            stack.append(A)
        elif el == '/':
            stack.pop()
        elif el == 'i':
            stack.append(stack[-1])
        elif el == '\\':
            last = stack.pop()
            stack.append(last+1)
        elif el == '*':
            A = stack.pop()
            B = stack.pop()
            stack.append(A//B)
        elif el == ']':
            v = stack.pop()
            if v % 2 == 0:
                stack.append(1)
        elif el == '[':
            v = stack.pop()
            if v % 2 != 0:
                stack.append(v)
        elif el == '~':
            a = stack.pop()
            b = stack.pop() 
            c = stack.pop()
            stack.append(max(a, b, c))
        elif el == 'K':
            break

print(max(stack))

