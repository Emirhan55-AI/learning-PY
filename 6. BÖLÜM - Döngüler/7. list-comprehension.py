#Temel Liste Yazımı
sayilar = []

for i in range(5):
    sayilar.append(i)
    
print(sayilar)

#List Comprehension ile Liste Yazımı
sayilar2 = [i for i in range(5)]
print(sayilar2)

#List Comprehension 2. Örnek
kurum = "revolution technology"
sonuc = [i.upper() for i in kurum]
print(sonuc)

#List Comprehension Koşullu Durum Kullanımı
sayilar = [3,5,7,12,14,19,1]
sonuc = [i for i in sayilar if i%2==0] #if burada filtreleme işlemi yapar; sadece çift sayıları listeye yazar.
print(sonuc)

#List Comprehension Koşullu Durum Kullanımı 2. Örnek
sayilar = [3,5,7,12,14,19,1]
sonuc = [i if i%2==0 else "tek sayi" for i in sayilar]
print(sonuc)

#List Comprehension Koşullu Durum Kullanımı 3. Örnek
sayilar = [3,5,7,12,14,19,1]
sonuc = [i**2 if i%2==0 else i**3 for i in sayilar]
print(sonuc)