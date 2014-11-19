def fib(old, new):
    total = 0
    while old < 4000000.0:
        if old % 2.0 == 0:
            total += old
        old, new = new, old+new
    return total

    