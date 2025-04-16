saat=float(input("Kaç saat kaldınız?:"))
if saat<=1:
    print("Tutarınız 5 lira")
elif saat>1 and saat<=5:
    print("Tutarınız " , saat*6 , " lira")
else:
    print("Tutarınız " , saat*10 , " lira")