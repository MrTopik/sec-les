name = input("Enter your name: ").lower()

if name == "gordon":
    print("\nAre you Gordon Freeman?")
    opt = input("[Y/n] ").lower()
    if opt == "y" or opt == "":
        print("\nWe serve the same mystery Freeman.")
    else:
        print("Okay")