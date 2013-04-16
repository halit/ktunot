ktunot
======
Student grade calculator

Usage
=====
    ktuHesapla = ktunot.KtuNot("gradesFile.txt", yourGrade)
    ktuHesapla.hesapla()

**z value** = ktuHesapla.zNotuDeger

**t value** = ktuHesapla.tNotuDeger

**average value** = ktuHesapla.ortalamaDeger

**all grade numbers** = len(ktuHesapla.notlar)

**standard deviation**= ktuHesapla.sSapmaDeger

**grades** = ktuHesapla.notlar[indexNumber]

If you want to visualization:

    ktuHesapla.gorsel("Lesson's Name")

Run
===
    python main.py
