import ktunot

ktuNotHesapla = ktunot.KtuNot("notlar.txt", 60)
ktuNotHesapla.hesapla()

print "z notu " + str(ktuNotHesapla.zNotuDeger)
print "t notu " + str(ktuNotHesapla.tNotuDeger)
print "ortalama " + str(ktuNotHesapla.ortalamaDeger)
print "toplam not " + str(ktuNotHesapla.notlarToplam)
print "standart sapma" + str(ktuNotHesapla.sSapmaDeger)