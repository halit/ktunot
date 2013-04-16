import ktunot

ktuHesapla = ktunot.KtuNot("notlar.txt", 30)
ktuHesapla.hesapla()

print "z notu " + str(ktuHesapla.zNotuDeger)
print "t notu " + str(ktuHesapla.tNotuDeger)
print "ortalama " + str(ktuHesapla.ortalamaDeger)
print "toplam not " + str(len(ktuHesapla.notlar))
print "standart sapma " + str(ktuHesapla.sSapmaDeger)

ktuHesapla.gorsel("Bilgisayar Muh. Giris")