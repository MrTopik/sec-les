def soru1():
    print("Merhaba, Adinizi ve Soyadinizi girin: ")
    ad = input()
    yas = int(input("Yasinizi girin: "))
    ingdil = input("Ingilizce biliyor musunuz? [Y/n]: ").lower()
    fradil = input("Fransizca biliyor musunuz? [Y/n]: ").lower()
    if yas<40:
        if fradil == "y" or fradil == "":
            print("Basarili")
        elif ingdil == "y" or ingdil == "":
            print("Basarili")
        else:
            print("Basarisiz")
    else:
        print("Basarisiz")
    exit(0)
def soru2():
    sayi = int(input("Bir sayi girin: "))
    if sayi%3 == 0 and sayi%5 == 0:
        print("15'e tam bolunur")
    else:
        print("15'e tam bolunemez")
    exit(0)
def soru3():
    print("Lutfen iki sinav ve bir performans notunuzu girin: ")
    sinav1 = int(input())
    sinav2 = int(input())
    perfnotu = int(input())
    ort = (sinav1 + sinav2 + perfnotu) // 3
    if ort > 50:
        print("Basarili")
    else:
        print("Basarisiz")
    exit(0)
print("Soru numarasini girin [1/2/3]: ")
soru = int(input())
match soru:
    case 1:
        soru1()
    case 2:
        soru2()
    case 3:
        soru3()
    case _:
        print("Bu secenek yok")
