import turtle as ttl
from random import randint

ttl.color('green')
ttl.speed(0)
ttl.setworldcoordinates(-1000, 0, 2000, 2000)
ttl.setheading(90)
ttl.delay(0)
ttl.tracer(0, 0)
ttl.hideturtle()
ttl.pensize(10)

positions = list()
angles = list()
pensizes = list()
lengths = list()

rules = {'X': 'F[@[-X]+X]',
         'F': 'F',
         '+': '+',
         '-': '-',
         '[': '[',
         ']': ']',
         '@': '@'}

def get_data():
    global l
    positions.append(ttl.pos())
    angles.append(ttl.heading())
    pensizes.append(ttl.pensize())
    lengths.append(l)

def set_data():
    global l
    ttl.setpos(positions.pop())
    ttl.setheading(angles.pop())
    ttl.pensize(pensizes.pop())
    l = lengths.pop()

# Number of iterations
n = 11
# Input string
s = 'X'
# Lines start length
l = 200

def get_child_lines():
    global l
    if ttl.pensize() > 0:
        ttl.pensize(ttl.pensize() - 1)
    if l > 60:
        l -= 20

draw = {'F': lambda: ttl.fd(l),
        'X': lambda: ttl.fd(l),
        '-': lambda: ttl.left(randint(0, 45)),
        '+': lambda: ttl.right(randint(0, 45)),
        '[': get_data,
        ']': set_data,
        '@': get_child_lines}

print(set(s) and set(draw.keys()))
if (set(s) and set(draw.keys())) != set(draw.keys()):
    print('Wrong string')
else:
    print('Starting iterations')
    
    for i in range(n):
        ns = str()
        for ci in range(len(s)):
            ns += rules[s[ci]]
            #print('{0} -> {1}'.format(s[ci], rules[s[ci]]))
        s = ns

    for c in s:
        draw[c]()

ttl.update()
ttl.done()
