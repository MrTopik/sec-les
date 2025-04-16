sic=int(input("Sıcaklığı girin:"))
if sic<=0:
    print("Çok soğuk")
elif sic>0 and sic<=15:
    print("Soğuk")
elif sic>15 and sic<=25:
    print("Ilık")
elif sic>25 and sic<=35:
    print("Sıcak")
elif sic>35 and sic<=50:
    print("Çok sıcak")
else:
    print("Aşırı sıcak")