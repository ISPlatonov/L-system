import turtle as ttl

ttl.color('green')
ttl.speed(0)
ttl.setworldcoordinates(-1, -1, 2000, 2000)
ttl.delay(0)
ttl.tracer(0, 0)

rules = {'A': 'B-A-B',
         'B': 'A+B+A',
         '+': '+',
         '-': '-'}

draw = {'A': lambda: ttl.fd(20),
        'B': lambda: ttl.fd(20),
        '+': lambda: ttl.left(60),
        '-': lambda: ttl.right(60)}

# Number of iterations
n = 6
# Input string
s = 'A'

print(set(s) and set(draw.keys()))
if (set(s) and set(draw.keys())) != set(draw.keys()):
    print('Wrong string')
else:
    print('Starting iterations')
    
    for i in range(n):
        ns = str()
        for ci in range(len(s)):
            ns += rules[s[ci]]
            print('{0} -> {1}'.format(s[ci], rules[s[ci]]))
        s = ns

    for c in s:
        draw[c]()

ttl.update()
ttl.done()
