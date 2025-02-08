lang = input("Language/Dil(English[Eng]/Turkce[Turk]): ")
if lang == "Eng":
  msg1 = "Enter radius: "
  msg2 = "Area"
  msg3 = "Circumference"
elif lang == "Turk":
  msg1 = "Yaricap girin: "
  msg2 = "Alan"
  msg3 = "Cevre"
else:
  print("This language is unknown/Bu dil bilinmiyor")
pi = 3.14
r = float(input(msg1))
alan = pi * (r**2)
cevre = 2*pi*r
print(f"{msg2} = {alan}\n{msg3} = {cevre}")
