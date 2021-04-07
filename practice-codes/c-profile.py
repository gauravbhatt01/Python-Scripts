# KcacheGrind.
import cProfile

def f():
    print("This is f function.")

cProfile.run('f()')