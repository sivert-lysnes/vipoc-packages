import time
import timeit
import vipoc.motor

def t():
    vipoc.motor.off(0)

st = timeit.timeit(t, number=10000)