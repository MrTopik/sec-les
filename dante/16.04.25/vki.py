boy=int(input("Boyunuzu giriniz:"))
agirlik=int(input("Ağırlığınızı girin:"))
vki=agirlik/(boy*boy)
if vki>=18 and vki<25:
    print("Normal")
elif vki>=25 and vki<30:
    print("Kilolu")
elif vki>=30 and vki<35:
    print("Obez")
elif vki>=35:
    print("Aşırı obez")
else:
    print("Zayıf")