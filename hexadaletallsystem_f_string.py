import math
a = 10

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# binaært
print(f"{a:b}")

# scientific standardform
print(f"{a:e}")
print(f"{a:.0e}")

# prosent
print(f"{a:%}")
print(f"{a:.0%}")

x = 0.8


print(f'{math.cos(x) = }') #bruker = tegnet
print(f'{math.sin(x) = }')

def mymax(x, y):

    return x if x > y else y

a = 3
b = 4

print(f'Størst av {a} og {b} er {mymax(a, b)}')#roper på funksjonen


#the objects must have either __str__() or __repr__()


