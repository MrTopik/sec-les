sayi1=int(input("İlk sayıyı girin:"))
sayi2=int(input("İkinci sayıyı girin:"))
op=str(input("İşlem giriniz:"))
if op=="*":
    print("Sonuç:" , sayi1*sayi2)
elif op=="/":
    print("Sonuç:" , sayi1/sayi2)
elif op=="+":
    print("Sonuç:" , sayi1+sayi2)
elif op=="-":
    print("Sonuç:" , sayi1-sayi2)
elif op=="^":
    print("Sonuç:" , sayi1**sayi2)
elif op=="%":
    print("Sonuç:" , sayi1%sayi2)
else:
    print("Yanlış operatör girdiniz")