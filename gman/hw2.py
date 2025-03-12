from datetime import datetime
cyear = datetime.now().year
def soru1():
    num = False
    while num == False:
        giris1 = input("Birinci sinav notunuzu girin: ")
        giris2 = input("Ikinci sinav notunuzu girin: ")
        giris3 = input("Ucuncu sinav notunuzu girin: ")
        try:
            giris1 = int(giris1)
            giris2 = int(giris2)
            giris3 = int(giris3)
            num = True
            ort = (giris1 + giris2 + giris3) / 3
            print(f"3 notunuzun ortalamasi {ort}")
        except ValueError:
            print("Tekrar deneyin")
def soru2():
    kgir = int(input("Kisa kenari girin: "))
    ugir = int(input("Uzun kenari girin: "))
    cevre = (ugir*2)+(kgir*2)
    alan = (ugir*kgir)
    print(f"Dikdortgenin Alani: {alan} Cevresi: {cevre}")
def soru3():
    gsayi = int(input("Bir sayi girin: "))
    print(f"{gsayi} sayisinin karesi {gsayi**2}'dir")
def soru4():
    ad = input("Adinizi girin: ")
    dtarih = int(input("Dogum yilinizi girin: "))
    yas = cyear - dtarih
    print(f"Merhaba {ad} yasiniz {yas}'dir")
def soru5():
    ad2 = input("Adinizi girin: ")
    kitap = int(input("Bu yil okudugunuz kitap sayisi: "))
    print(f"{ad2} bu yil {kitap} okudu")
test = False
while test == False:
    opt = input("Sayi girin: ")
    try:
        opt = int(opt)
        test = True
    except ValueError:
        print("Bir sayi girmediniz")

match opt:
    case 1:
        soru1()
    case 2:
        soru2()
    case 3:
        soru3()
    case 4:
        soru4()
    case 5:
        soru5()
    case _:
        print("Bu secenek yok")
        exit(0)
