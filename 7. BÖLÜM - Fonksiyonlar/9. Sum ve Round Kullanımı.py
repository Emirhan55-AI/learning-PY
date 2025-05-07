# Sum Fonksiyonu
sayilar = [1, 3, 5, 4, 32, 56]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 15) #Toplam sonuca 15 ekler.

products = [
    {"title": "iphone 15", "price": 60000},
    {"title": "iphone 16", "price": 70000},
    {"title": "iphone 17", "price": 80000},
    {"title": "iphone 17", "price": 0},
]

toplamFiyat = sum([urun["price"] for urun in products])
urunAdeti = len([urun for urun in products if urun["price"] > 0])
sonuc = toplamFiyat / urunAdeti

print(sonuc)

# Round Fonksiyonu
sonuc = round(5.3)
sonuc = round(5.6)
sonuc = round(5.5)
sonuc = round(1.325253, 2)
sonuc = round(1.325253, 4) #Virgülden sonra kaç basamak verdiğini yazdık.
print(sonuc)