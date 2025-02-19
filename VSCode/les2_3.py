a = 10
print(a)

b = 5
c = "HHY"
pi = 3.14

print(a, b ,c, pi)


ocak = mart = mayis = temmuz = 30
print(ocak)

x, y, z = 100, -45, 0
print(f"x={x} y={y} z={z}")

a = input("Enter something: ")
try:
    a = int(a)
except ValueError:
    pass
print(f"The variable type of {a} is {type(a)}")