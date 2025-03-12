num1 = input("Hello please enter a number: ")
num2 = input("Enter another number please: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    result = (num1 + num2) // 2
    print(f"Result is {result}")
except ValueError:
    print("You didn't enter a number.")
