# Bir veri tipini kullanınca (obje vs.) bellek üzerinde nasıl değerlendiriliyor.
# value types --> string , numbers

x=5
y=25
x=y
y=10
print(x,y) #y de yaptığımız güncelleme x i etkilemedi.Sadece y değişti. Çünkü hepsi farklı adreslerde farklı değerlerdir.



# reference types --> list , class

A=["orange","apple","banana"]
B=["orange","apple","banana"]
A=B
B[0] = "grape"
print(A,B)
#A da bir değişiklik yapmadığımız halde A da etkilendi. Çünkü bu listeler bir adres üzerindeler.Aynı adresi taşıdıklarından birinde değişiklik yapmak diğerlerini de değiştirir.
#Bu tipin olmasının sebebi : 500 tane ürünün olduğu bir liste olsun. Biz bu listeyi bi yerden bir yere kopyalamak istediğimizde ikinic bir kopyalama olmasın yani 500 tane ürün gelmesin performansı etkiler. Onun yerine sadece adresi gelsin. 




# value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x, y)

# reference

a = ["elma","armut"]
b = ["elma","armut"]

a = b   # adres kopyaladınız.
a[0] = "üzüm"
print(a, b)

# liste koplayama
listeA = [10,20]
# listeB = listeA.copy()     # 1.yöntem
listeB = list(listeA)        # 2.yöntem

listeB[0] = 30

print(listeA,listeB)