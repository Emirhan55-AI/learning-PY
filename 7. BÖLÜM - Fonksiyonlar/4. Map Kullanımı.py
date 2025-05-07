"""
Map Fonksiyonu,bir iterable (örneğin bir liste veya tuple) üzerinde bir fonksiyonu uygulamak için kullanılır. 
map() fonksiyonu, belirtilen fonksiyonu her bir öğeye uygular ve sonuçları bir map object olarak döndürür. 
Bu nesne, gerekirse list(), tuple() veya diğer veri türlerine dönüştürülebilir.

map(function, iterable)
function: Uygulanacak fonksiyon. Bu, yerleşik bir fonksiyon, lambda fonksiyonu veya önceden tanımlanmış bir 
fonksiyon olabilir.
iterable: Fonksiyonun uygulanacağı veri koleksiyonu.

Python 3'te map() bir iterator döner. Sonuçlara erişmek için bu nesneyi list() veya tuple() gibi bir yapıya 
dönüştürmeniz gerekir.
Büyük veri koleksiyonlarıyla çalışırken map() bellekte bir liste oluşturmaz; bunun yerine öğeleri gerektiği 
zaman hesaplayan bir iterator sağlar.
"""
# Map Fonksiyonu Kullanımı
def square(num):
    return num**2

lists = [1,3,5,9,12,15]
sonuc = list(map(square,lists))
print(sonuc)
#or
sonuc2 = list(map(lambda a:a**2,lists))
print(sonuc2)

# Örnek 2
sayilar_str = ["1","3","5","9","12","15"]
sonuc3 = list(map(int,sayilar_str)) #int fonksiyonu str yi inte çevirir.
print(sonuc3)

# Örnek 3
isimler = ["emirhan","ahmet","necati"]
caps = list(map(str.capitalize,isimler))
print(caps)

# Örnek 4
kullanicilar = [ {"ad":"ali","soyad":"numan"},
{"ad":"ahmet","soyad":"paşa"}
]
sonuc4 = list(map(lambda kisi:kisi["ad"],kullanicilar))
print(sonuc4)