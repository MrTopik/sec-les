#marketten alınan iki ürünün fiyatları klavyeden ayrı  ayrı giriliyor,fiyatların toplamı 200'den küçükse direk ödemesi yapılıyor.200'den büyükse %25 indirim uygulanıyor

urun1=float(input("İlk ürünün fiyatını giriniz:"))
urun2=float(input("İkinci ürünün fiyatını giriniz:"))
urun1+=urun2
if urun1>200:
    urun1*=0.75
    print("İndirim ile tutarınız=" , urun1)
else:
    print("Tutarınız=" , urun1)