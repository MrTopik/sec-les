import time
import random
short = 3
long = 5
sum = short * long
print(f"The area of the rectangle is {sum}")


rand = random.randint(1, 100)
a = int(input("Enter a number: "))
print("The number you entered is ......")
time.sleep(3)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGONE\n\n")
time.sleep(1)
print(f"Oh it just returned back I think... is your number {rand}?")
quest = input("[Yes/No]:")
if quest == "Yes":
    print(f"Okay then.. that is great.... Your number is {rand}")
    exit(0)
elif quest == "No":
    print(f"Hmm in that case it is {a}")
    exit(0)
