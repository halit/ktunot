class KtuNot():
    def __init__(self, dosya):
        self.dosya = dosya
        self.notlar = []
        self.notlarToplam = 0
        self.standartToplam = 0

    def hesapla(self):
        pass

    def sSapma(self):
        import math
        for notx in self.notlar:
            self.standartToplam = float(self.standartToplam + (float(notx)-self.ortalama())**2)
        return math.sqrt(float(self.standartToplam / len(self.notlar) - 1 ))

    def tNotu(self):
        pass

    def zNotu(self):
        pass

    def ortalama(self):
        return float(self.notlarToplam/len(self.notlar))

    def dosyaAc(self):
        with open(self.dosya,"r") as dosya:
            for notx in dosya.readlines():
                self.notlar.append(self.temizlik(notx))
            for notx in self.notlar:
                self.notlarToplam = self.notlarToplam + int(notx)

    def temizlik(self, metin):
        metin = str(metin).replace("\n","").replace("\t","").replace(" ","")
        return metin