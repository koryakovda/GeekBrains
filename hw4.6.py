import itertools
c = 0
for i in itertools.count(start=3,step=1):
    if i == 11:
        break
    print(i)
c = 0
for i in itertools.cycle(['ну', 'купи', 'слона']):
    print(i)
    c += 1
    if c > 10:
        break