#klavyeden girilen sayının 0-50 arasında olup olmadığını kontrol eden komut
a=int(input("Sayı girin:"))
print("0-50 arasında"*(a>=0 and a<=50) , "0-50 arasında değil"*(not(a>=0 and a<=50)))