a = 5 #global scope
b = 2
def a_plus_b():
    a = 3 #lokal scope
    return a + b
print (a_plus_b())
print (a + b)
