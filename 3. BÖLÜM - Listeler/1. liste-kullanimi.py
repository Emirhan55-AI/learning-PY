"""
String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanıdır ve her bir elemana indeks numarası ile ulaşabiliriz.
Yine aynı mantıkla list veri tipinde ise tek bir karakter yerine farklı veri tiplerindeki bilgileri gruplayabiliyoruz. 

Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.

List, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Tuple, elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.

Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.

Listeler for döngüsüyle yazdırılır.

"""


"""
message = "Selamun Aleyküm Mübarek".split() #Listeye çevirdik split metoduyla. Yani str to list yaptık.  
print(message)
print(message[1])
"""


my_list = [1,2,3]
my_list2 = ['bir',2,True,5.6]
print(my_list)
print(my_list2)
print(my_list + my_list2)
print(my_list[0]+ my_list[2]+my_list2[3])



list1 =['bir','iki','uc']
list2 =['dort','bes','alti']
list3 = [['bir','iki','uc'],['dort','bes','alti']]
numbers = list1+list2
print(numbers)
print(list3[0][1]+" "+list3[1][2])


# liste içinde liste

userA = ["Emirhan",21]
userB = ["Uysal",5.3]
users= [userA ,userB]
print(users)
print(users[0][1])


# for döngüsüyle liste yazdırma

my_List = ["bir","iki","dort"]

for i in my_List:
    print(i)