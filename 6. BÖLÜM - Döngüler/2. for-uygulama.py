sayilar = [1,3,5,7,9,12,21]
#1.ÖRNEK
'''for ucunkati in sayilar:
    if ucunkati%3==0:
        print(ucunkati)'''   
#2.ÖRNEK
'''sayi=0
for toplam in sayilar:
    sayi = sayi+toplam
print(sayi)'''
#3.ÖRNEK
'''for kare in sayilar:
    if kare%3==0:
     kare = kare**2
     print(kare)'''
#4.ÖRNEK
'''sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
for karaktersayisi in sehirler:
    if len(karaktersayisi)<=5:
        print(karaktersayisi)'''
#5.ÖRNEK
urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]
#Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
     fiyat = int(urun['price'])
     toplam += fiyat
print('toplma ürün fiyatı: ', toplam)


#Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
     if (int(urun['price']) <= 5000):
         print(urun['name'])
