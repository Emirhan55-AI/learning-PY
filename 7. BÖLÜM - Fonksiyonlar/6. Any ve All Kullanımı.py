"""
all Fonksiyonu:

all(iterable) fonksiyonu, bir iterable'daki tüm değerler True ise True döner. En az bir False varsa False döner.
Mantıksal olarak and işlemine benzer: Tüm koşullar sağlanmalı.

any Fonksiyonu:

any(iterable) fonksiyonu, bir iterable'daki en az bir değer True ise True döner. Tüm değerler False ise False döner.
Mantıksal olarak or işlemine benzer: Tek bir koşulun sağlanması yeterli.
"""

#ÖRNEK 1
sonuc = all([True, True, False])   # False
sonuc = all([True, True, True])    # True
sonuc = any([True, True, True])    # True
sonuc = any([True, True, False])   # True
sonuc = any([False, False, False]) # False

# And => True and True => all()
# Or => True or False => any()

#ÖRNEK 2
sayilar = [1, 3, 5, 7, 6, 52, 0]

sonuc = all([bool(sayi) for sayi in sayilar])       # False (çünkü 0 var)
sonuc = any([bool(sayi) for sayi in sayilar])       # True (en az bir değer True)
sonuc = all([sayi % 2 == 0 for sayi in sayilar])    # False (hepsi çift değil)
sonuc = any([sayi % 2 == 0 for sayi in sayilar])    # True (en az bir çift sayı var)

#ÖRNEK 3
users = ["ahmet", "çınar", "hasan"]

sonuc = all([user[0] == "a" for user in users])     # False (çünkü 'çınar' ve 'hasan' var)
sonuc = any([user[0] == "a" for user in users])     # True (çünkü 'ahmet' var)

print(sonuc)

