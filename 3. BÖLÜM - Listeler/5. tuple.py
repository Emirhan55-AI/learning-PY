# Tuple listesinde bir ekleme veya çıkarma işlemi yapılamaz. Bellekte daha az yer kaplar. Listeden tuplea ve tupledan listeye geçiş yapılabilir.

my_list = [1, 2, 3]
my_tuple = (1, 'iki', 3) #parantez kullanmasanda olur.
print(type(my_list))
print(type(my_tuple))
print(my_list[2])
print(my_tuple[2])
print(len(my_tuple))
print(len(my_list))



my_list = ['ali','veli']
my_tuple = ('a','b','b')
names = ('c','d','f') + my_tuple
print(names)



my_list[0] = 'ahmet'
# my_tuple[0] = 'kerim' Bu şekilde bir atama olamaz. Tuple farkı tek bir eleman üzerinde değişiklik yapamazsın,ekleyemez ve silemezsin. Genel bir değişiklik yapabilirsin.



print(my_tuple.count('b'))
print(my_tuple.index('b')) #Başka metot kullanılamaz.
print(my_list)
print(my_tuple)



#Tür Dönüşümü
my_tuple = tuple([2,3,4])
my_list = list((2,3,4))