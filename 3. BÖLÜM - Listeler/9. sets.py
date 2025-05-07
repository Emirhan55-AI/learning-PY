fruits = {'orange','banana','mango'} #set tanımlaması {} arasına yapılır.
#print(fruits[0]) listeden farkı , indekslenmez yani sıralı bir düzen yoktur. indekslenemez listedir.Tekrarlanamaz ve güncellenemez. Eleman silebilir veya ekleyebilirsin.


#Elemanlara döngü ile ulaşılır.
for x in fruits : 
    print(x)



fruits.add('cherry') #listeye cherry eklendi.
fruits.update(['mango','apple','melon']) #listede aynı eleman bulunmaz eklesen de görünmez (2 tane birden) 
print(fruits)


fruits.remove('mango') #mango kelimesi kalkar.remove yerine discard yazmak da aynı işlemi yapar.
fruits.pop() #elemanlar sıralı olmadığından rastgele bir kelimeyi kaldırır.
fruits.clear() #tüm elemanlar silinir.



MY_list = [1,2,3,4,5,1,2]
print(MY_list) #aynı degerler bu listede görünür.
print(set(MY_list)) #constructer ile mylisti gönderirsek aynı degerler görünmez.