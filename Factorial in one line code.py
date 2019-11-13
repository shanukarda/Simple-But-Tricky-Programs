# Find factorial in one line code

import functools
print(functools.reduce(lambda x,y:x*y, tuple(range(1,int(input())+1))))