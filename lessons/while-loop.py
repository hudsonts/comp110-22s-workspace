x: float = -5
y: float = 1
z: float = 0

x = x - 1
if x < y:
    z = x ** y / 2
else:
    if x == y: 
        z = y % x
    else:
        x = x / 2
        z = y - x
    z = z + 1
print(z)
