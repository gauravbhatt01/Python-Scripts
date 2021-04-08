def range(start, stop, step = 1):
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
    return numbers

def xrange(start, stop, step =1):
    while start < stop:
        yield start
        start +=step

for i in range(0, 1000):
    pass

for i in xrange(0, 10000):
    pass