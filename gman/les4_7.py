a = int(input("Sayı girin: "))
b = int(input("Sayı girin: "))
if a > b:
    print(f"{a}, {b}'den büyüktür.")
elif a == b:
    print(f"{a} ve {b} eşittir.")
else:
    print(f"{b}, {a}'den büyüktür.")