sayi = int(input("Bir sayı giriniz: "))
print(("50 ile 0 aralığındadır"*(50>sayi>0) + ("50'den büyüktür"*(sayi>50) + ("0'dan küçüktür"*(0>sayi)))))