#Value Type parametre

def changeName(n):
    n="Ahmet"
    print(n)

name="Emirhan"
changeName(name)
print(name)

#Reference Type

def change(n):
    n[0]="İstanbul"
    
lists = ["Ankara","İzmir"]
change(lists)
print(lists)

"""
Bu iki kodun farkı, parametrenin değer tipinde mi yoksa referans tipinde mi işlendiğiyle ilgilidir. 
Python'da değişkenler, veri türlerine göre value type (değer tipi) veya reference type (referans tipi) gibi 
davranır.

Burada name değişkeni, bir string'dir. Python'da stringler immutable (değiştirilemez) veri tipleridir.
changeName fonksiyonunda, n değişkenine "Emirhan" değeri kopyalanır.
n = "Ahmet" ile yeni bir değer atanır, ancak bu atama sadece fonksiyonun içindeki n değişkenine yapılır.
Fonksiyonun dışında, name değişkeni etkilenmez, çünkü sadece kopya değişmiştir.Değer tipi değişkenler, 
fonksiyona kopyalanarak geçer ve orijinal değişken dışarıda değişmeden kalır.

Burada lists, bir liste'dir. Python'da listeler mutable (değiştirilebilir) veri tipleridir.
change fonksiyonuna lists referansı ile geçirilir. Bu referans, orijinal listeyi işaret eder.
n[0] = "İstanbul" ifadesiyle, listenin ilk elemanı değiştirilir. Bu değişiklik, orijinal lists üzerinde de 
etkili olur.
Çünkü fonksiyona kopya değil, doğrudan liste referansı aktarılmıştır.
Referans tipi değişkenler, orijinal nesneyi işaret ettiği için, fonksiyon içinde yapılan değişiklikler orijinal 
nesneye yansır.
"""

#Örnek 1

def add(a,b):
    return sum((a,b))

total = add(100,125)
print(total)




#Örnek 2

def add(a,b,c=0,d=0,e=0): #0 Değerini atamak c,d,e girilmese bile en az 2 değişkeni toplamaya yarar.
    return sum((a,b,c,d,e))

total = add(100,125)
print(total)
total2=add(102,149,2.5)
print(total2) #d ve e girilmemesine rağmen toplama gerçekleşti.




#Örnek 3: Bir çok parametre varsa *params kullanılır. type = tuple için *

def add(*params):
    return sum((params))

total3 = add(10,20,-9,2.89,149,100000,54545754)
print(total3)






#Örnek 4: type=dictionary için **

def displayUser(**args):
    for key,value in args.items():
        print('{} is {} '.format(key,value))

displayUser(name="Emirhan",age=21,city="Bursa")
displayUser(name="Mehmet",age=24,city="Kocaeli",phone="2112314234")
displayUser(name="Ahmet",age=49,city="Mardin",phone="241848722",email="ahmetmardinli@gmail.com")





#Örnek 5
def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(100,200,300,40,50,key1='value1',key2='value2')