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
    st2 = False
    while st2 == False:
        kgir = input("Kisa kenari girin: ")
        ugir = input("Uzun kenari girin: ")
        try:
            kgir = int(kgir)
            ugir = int(ugir)
            st2 = True
            cevre = (ugir*2)+(kgir*2)
            alan = (ugir*kgir)
            print(f"Dikdortgenin Alani: {alan} Cevresi: {cevre}")
        except ValueError:
            print("Sayi girmediniz")
def soru3():
    st3 = False
    while st3 == False:
        gsayi = input("Bir sayi girin: ")
        try:
            gsayi = int(gsayi)
            st3 = True
            print(f"{gsayi} sayisinin karesi {gsayi**2}'dir")
        except ValueError:
            print("Sayi girmediniz")
def soru4():
    st4 = False
    while st4 == False:
        ad = input("Adinizi girin: ")
        dtarih = input("Dogum yilinizi girin: ")
        try:
            dtarih = int(dtarih)
            st4 = True
            yas = cyear - dtarih
            print(f"Merhaba {ad} yasiniz {yas}'dir")
        except ValueError:
            print("Sayi girmediniz")
def soru5():
    st5 = False
    while st5 == False:
        ad2 = input("Adinizi girin: ")
        kitap = input("Bu yil okudugunuz kitap sayisi: ")
        try:
            kitap = int(kitap)
            st5 = True
            print(f"{ad2} bu yil {kitap} kitap okudu")
        except ValueError:
            print("Sayi girmediniz")
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
