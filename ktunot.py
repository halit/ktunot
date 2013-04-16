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
            self.standartToplam = float(self.standartToplam + (float(notx)-self.ortalama()) ** 2)
        self.sSapmaDeger = math.sqrt(float(self.standartToplam / len(self.notlar) - 1 ))

    def tNotu(self):
        self.tNotuDeger = float(10*self.zNotu() + 50)

    def zNotu(self):
        self.zNotuDeger = float((float(self.kullaniciNot) - self.ortalama()) / self.sSapma())

    def ortalama(self):
        self.ortalamaDeger = float(self.notlarToplam / len(self.notlar))

    def dosyaAc(self):
        with open(self.dosya,"r") as dosya:
            for notx in dosya.readlines():
                self.notlar.append(self.temizlik(notx))
            for notx in self.notlar:
                self.notlarToplam = self.notlarToplam + int(notx)

    def temizlik(self, metin):
        metin = str(metin).replace("\n","").replace("\t","").replace(" ","")
        return metin