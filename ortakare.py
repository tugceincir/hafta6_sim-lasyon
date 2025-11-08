def OrtaKare(b, sayac):
    dizi = []
    uzunluk = len(str(b))

    for i in range(sayac):
        kare = b * b
        usayi = str(kare).zfill(uzunluk * 2)


        baslangic = (len(usayi) - uzunluk) // 2
        ys = usayi[baslangic : baslangic + uzunluk]

        dizi.append(ys)
        b = int(ys)

    return dizi


git add README.md
b = int(input("Başlangıç sayısını girin: "))
sayac = int(input("Kaç sayı üretilecek?: "))

sonuc = OrtaKare(b, sayac)

print("Üretilen sayılar:")
for e in sonuc:
    print(e)

