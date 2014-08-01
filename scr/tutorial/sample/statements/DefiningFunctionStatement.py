def fib(n):
    a,b = 0,1
    while a < n:
        print a,
        a, b = b, a + b

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def ask_ok(prompt, retries=4, complaint="Yes or no, please!"):
    while True:
        ok = raw_input(prompt)
        if ok in ('y','ye','yes'):
            return True
        elif ok in ('n','no','not','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok('yes or no???: ')