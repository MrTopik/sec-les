num1 = input("Hello please enter a number: ")
num2 = input("Enter another number: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    final = sum // 2
    print(f"Result {final}")
except ValueError:
    print("You didn't enter a number")