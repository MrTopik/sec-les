sayi = int(input("Sayı girin: "))
print("Girdiğiniz sayı çifttir"*(sayi%2==0) + "Girdiğiniz sayı tektir"*(not(sayi%2==0)))