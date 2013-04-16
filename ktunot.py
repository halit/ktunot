class KtuNot():
    def __init__(self, dosya):
        self.dosya = dosya
        self.notlar = []
        self.notlarToplam = 0

    def dosyaAc(self):
        with open(self.dosya,"r") as dosya:
            for notx in dosya.readlines():
                self.notlar.append(self.temizlik(notx))
            for notx in self.notlar:
                self.notlarToplam = self.notlarToplam + int(notx)

    def temizlik(self, metin):
        metin = str(metin).replace("\n","").replace("\t","").replace(" ","")
        return metin