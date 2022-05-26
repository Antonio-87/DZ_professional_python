from stack import Stack

def balancer(data):
    stack = Stack()
    a_open, a_close = "(", ")"
    b_open, b_close = "[", "]"
    c_open, c_close = "{", "}"
    for s in data:
        if s == a_open or s == b_open or s == c_open:
            stack.push(s)
        elif s == a_close or s == b_close or s == c_close:
            if stack.isEmpty():
                return f'Несбалансированно'
            else:
                stack.pop()
    return f'Сбалансированно'

pattern = '[([])((([[[]]])))]{()}'
pattern_1 = '{{[(])]}}'
print(balancer(pattern))
print(balancer(pattern_1))

