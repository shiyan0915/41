x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
numbers = x,y,z
print(sorted(numbers)[::-1])

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
minA = max(x, y, z)
maxA = min(x, y, z)
print(maxA, x+y+z-maxA-minA, minA)

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x>y>z:
    print(x,y,z)
elif x>z>y:
    print(x,z,y)
elif y>x>z:
    print(y,x,z)
elif y>z>x:
    print(y,z,x)
elif z>x>y:
    print(z,x,y)
else:
    print(z,y,x)
