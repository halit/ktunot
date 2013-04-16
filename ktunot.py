class KtuNot():
    def __init__(self, dosya, kullaniciNot):
        self.dosya = dosya
        self.kullaniciNot = kullaniciNot
        self.notlar = []
        self.notlarToplam = 0
        self.standartToplam = 0

    def hesapla(self):
        self.dosyaAc()
        self.ortalama()
        self.sSapma()
        self.zNotu()
        self.tNotu()

    def sSapma(self):
        import math
        for notx in self.notlar:
            self.standartToplam = float(self.standartToplam + (float(notx) - self.ortalamaDeger) ** 2)
        self.sSapmaDeger = math.sqrt(self.standartToplam / (len(self.notlar) - 1))

    def tNotu(self):
        self.tNotuDeger = float(10 * self.zNotuDeger + 50)

    def zNotu(self):
        self.zNotuDeger = float((float(self.kullaniciNot) - self.ortalamaDeger) / self.sSapmaDeger)

    def ortalama(self):
        self.ortalamaDeger = float(float(self.notlarToplam) / len(self.notlar))

    def dosyaAc(self):
        with open(self.dosya,"r") as dosya:
            for notx in dosya.readlines():
                self.notlar.append(self.temizlik(notx))
            for notx in self.notlar:
                self.notlarToplam = self.notlarToplam + int(notx)

    def temizlik(self, metin):
        metin = str(metin).replace("\n","").replace("\t","").replace(" ","")
        return metin

    def gorsel(self, dersAdi):
        from pylab import *
        from Tkinter import *
        import matplotlib.pyplot as plt
        import collections

        subreddits = collections.Counter(self.notlar)
        sdata = subreddits.items()
        sdata = sorted(sdata, key=lambda x: x[1], reverse=True)
        plt.figure(1)
        plt.subplot(211)
        plt.title(str(dersAdi))
        xlabel("Notlar")
        ylabel("Kisi Sayisi")
        plt.bar(map(lambda x:float(x[0]),sdata),map(lambda x:float(x[1]),sdata),alpha=5)
        grid(True)