def divby(divideby):
    return(42/divideby)
try:
    print(divby(10))
    print(divby(0))
    print(divby(18))
    print(divby(20))
except ZeroDivisionError:
    print('Error:Invalid  Argument.')

