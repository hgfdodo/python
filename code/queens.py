import random

def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(nextX-state[i]) in (0, nextY-i):
			return True
	
	return False


def queens(num,state):
    for pos in range(num):
        if not conflict(state, pos):
            if num-1 == len(state):
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    length = len(solution)
    print solution
    for pos in solution:
        print "." * pos + "*" + "." * (length-pos-1)
