# selamlar en son paytınu 3 ay once denedim saygılar

import time

print("hesap magina")
time.sleep(1)

def toplama():
    ilk = input("ilk sayı gir hemen : ")
    ikinci = input("ikinci sayı gir hemen : ")
    time.sleep(1)

    print(int(ilk)+int(ikinci))

def cikarma():
    ilk = input("ilk sayı gir hemen : ")
    ikinci = input("ikinci sayı gir hemen : ")
    time.sleep(1)

    print(int(ilk)-int(ikinci))

def carpma():
    ilk = input("ilk sayı gir hemen : ")
    ikinci = input("ikinci sayı gir hemen : ")
    time.sleep(1)

    print(int(ilk)*int(ikinci))

def bolme():
    ilk = input("ilk sayı gir hemen : ")
    ikinci = input("ikinci sayı gir hemen : ")
    time.sleep(1)

    print(int(ilk)/int(ikinci))

soru = input("hangi islemi yabcan hemen sole : ")

if soru == "toplama":
    toplama()

elif soru == "cikarma":
    cikarma()

elif soru == "carpma":
    carpma()

elif soru == "bolme":
    bolme()

else:
    print("dogru sole la")
