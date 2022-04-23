def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def new_greatest(a,b,c):
    biggest = greater(a,b)
    return greater(biggest, c)
print(new_greatest(12,11,2))