yas = int(input("Yaşınızı girin: "))

if yas < 18:
    print("Ehliyet alamazsınız.")
if yas > 18 or yas == 18:
    print("Ehliyet alabilirsiniz")