import random, sys, time
indent = 0
indentincreasing = True

try:
    while True:
        print(' ' * indent, end = '')
        print('********')
        if indentincreasing:
            indent = indent +1
            if indent == 20:
                indentincreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentincreasing = True
except KeyboardInterrupt:
    sys.exit()
