# Sort Fonksiyonu: sayilar adlı orijinal liste üzerinde bir değişiklik yapar.
sayilar =[1,5,9,21,12,11,4,23,70,67,26]
sayilar.sort()
print(sayilar)

# Sorted Fonksiyonu: Orijinal listeyi değiştirmez, sıralanmış yeni bir liste oluşturur.
sonuc = sorted(sayilar)
tersineyazma= sorted(sayilar,reverse = True)
print(sonuc)
print(tersineyazma)
print(sayilar)

# Sorted Kullanımı Örnek 1
liste = ["emirhan","ahmet","ali","erezyon"]
sonuc = sorted(liste)
print(sonuc)

# Sorted Kullanımı Örnek 2
users = [
    {"username": "sadikturan", "posts": ["post 1", "post 2"], "email": "info@abc.com", "phone": "1234"},
    {"username": "ahmetyilmaz", "posts": ["post 1"], "email": "info@abcd.com"},
    {"username": "canayilmaz", "posts": ["post 1", "post 2", "post 3"]}
]

sonuc1 = sorted(users, key=len)
sonuc2 = sorted(users, key=len, reverse=True)
sonuc3 = sorted(users, key=lambda user: user["username"])
sonuc4 = sorted(users, key=lambda user: len(user["posts"]))
sonuc5 = sorted(users, key=lambda user: len(user["posts"]), reverse=True)

sonuc6 = list(map(lambda user: user["username"], sorted(users, key=lambda user: len(user["posts"]))))

print(sonuc1)
print(sonuc2)
print(sonuc3)
print(sonuc4)
print(sonuc5)
print(sonuc6)


# Sorted Kullanımı Örnek 3
kurslar = [
    {"title": "python", "count": 10000},
    {"title": "web gelistirme", "count": 20000},
    {"title": "javascript", "count": 5000}
]

sonuc1 = sorted(kurslar, key=lambda kurs: kurs["count"])
sonuc2 = sorted(kurslar, key=lambda kurs: kurs["count"], reverse=True)
sonuc3 = list(map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["count"], reverse=True)))

print(sonuc1)
print(sonuc2)
print(sonuc3)