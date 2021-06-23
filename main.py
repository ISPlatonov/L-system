import turtle as ttl

ttl.color('green')
ttl.speed(0)
ttl.setworldcoordinates(-1, -1, 2000, 2000)
ttl.setheading(45)
ttl.delay(0)
ttl.tracer(0, 0)

positions = list()
angles = list()

rules = {'X': 'F-[[X]+X]+F[+FX]-X',
         'F': 'FF',
         '+': '+',
         '-': '-',
         '[': '[',
         ']': ']'}

def get_pos_n_angle():
    positions.append(ttl.pos())
    angles.append(ttl.heading())

def set_pos_n_angle():
    ttl.setpos(positions.pop())
    ttl.setheading(angles.pop())

draw = {'F': lambda: ttl.fd(10),
        'X': lambda: ttl.fd(0),
        '-': lambda: ttl.left(25),
        '+': lambda: ttl.right(25),
        '[': get_pos_n_angle,
        ']': set_pos_n_angle}

# Number of iterations
n = 6
# Input string
s = 'X'

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
