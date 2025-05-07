# Veri Alma (input):

x=input("Birinci sayıyı gir : \n")
y =input("İkinci sayıyı gir :")
print(x+y)
print(type(x+y))

# Kullanıcıdan alınan tüm veriler str'dir. Bunları gerektiğinde dönüştürmeyi unutma.


# Veri Dönüşümü:

total = int(x) + int(y)
print(total)
print(type(total))

#Bu dönüşümleri str,float,int,bool için yapabilirsin.

a =2.5
a=int(a)
print(a)

k=float(input("Sayı gir : "))
print("NUMBER : ",int(k))


# DAİRE HESABI:

pi=3.14
r=float(input("Birinci sayiyi gir : \n"))
alan = pi*(r**2)
cevre = 2*pi*r
print("Yuvarlamadan once cevre : ",cevre)
cevre = round(cevre,3) #sayı yuvarlama
print("alan \n " + str(alan) +"\n" + "cevre \n" +str(cevre))


# Kaçış Karakterleri:

"""
\n (Yeni Satır) → Alt satıra geçmeyi sağlar.

\t (Sekme) → Boşluk bırakır, bir tab kadar kaydırır.

\\ (Ters Eğik Çizgi) → \ karakterini normal bir karakter olarak yazmamızı sağlar.

\' (Tek Tırnak) → Tek tırnaklı (') string içinde tek tırnak kullanabilmemizi sağlar.

\" (Çift Tırnak) → Çift tırnaklı (") string içinde çift tırnak kullanmamızı sağlar.

\b (Geri Silme) → Önceki karakteri siler.

"""


