# Fonksiyon Kullanımı 1

def sayHello():
    print("Hello")
    
sayHello()
sayHello()

for i in range(10):
    sayHello() #Bu döngüyü fonksiyon içinde tanımlarsan işin daha da kolay olur.




# Fonksiyon Kullanımı 2: Fonksiyondan Değer Döndürme

# Eğer bir fonksiyon return kullanmazsa, sadece ekrana çıktı verebilir ama bu değeri başka bir yerde değişkene atayamaz, işleyemez veya başka bir işlemde kullanamazsınız.
# Bir fonksiyon return gördüğü anda çalışmayı durdurur. return sonrası hiçbir kod çalışmaz!
# Eğer bir fonksiyonda return kullanılmazsa veya sadece return yazılırsa, fonksiyon None döndürür. Eğer bir fonksiyonun sonucunu başka bir yerde kullanmak istiyorsak, mutlaka return kullanmalıyız!

def toplam():
    return 10+20

sonuc= toplam()
print(sonuc)




# Fonksiyon Kullanımı 3: Fonksiyona Parametre Gönderme

def sayHello2(name):
    print("Hello"+" "+name)
    
sayHello2("Emirhan")




#Fonksiyon Kullanımı 4

def total(num1,num2):
    return num1+num2

toplam = total(20, 30)
print(toplam)




#Fonksiyon Kullanımı 5

def yasHesapla(dogumyili):
    return 2024-dogumyili

yasEmir=yasHesapla(2003)

print(yasEmir)





#Fonksiyon Kullanımı 6: Bir metodu başka bir metot içinde kullanmak.

def EmekliligeKacYilKaldi(dogumyili):
    yas = yasHesapla(dogumyili)
    emeklilik = 65-yas
    
    if emeklilik>0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    
    else:
        print("Zaten emekli oldunuz.")


emeklilikEmir = EmekliligeKacYilKaldi(2003)
emeklilikEmir2= EmekliligeKacYilKaldi(1920)
print(emeklilikEmir)
print(emeklilikEmir2)






#Fonksiyon Kullanımı 7: Kullanan kişiye fonksiyon hakkında bilgi verme.

def EmekliligeKacYilKaldi(dogumyili):
    '''
    Tanim: Doğum yılına göre emeklilige kac yil kaldi.
    Input: Dogum yili
    Output: Emeklilik yasi
    '''
    yas = yasHesapla(dogumyili)
    emeklilik = 65-yas
    
    if emeklilik>0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    
    else:
        print("Zaten emekli oldunuz.")

print(help(EmekliligeKacYilKaldi))





#Fonksiyon Kullanımı 8: Default Parametre

def sayHello3(name ="user"):
    print("Hello"+" "+name)

sayHello3() #Bir parametre girilmezse user yazar.




#Fonksiyon Kullanımı 9

def usAlma(taban,us=2): #Default parametre sol taraf için yazılamaz. Yani taban default parametre alamaz.
    return taban**us

sonuc= usAlma(2,3)
sonuc= usAlma(5)



#Fonksiyon Kullanımı 10: Referans değer belirleme.

def toplam(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def islem(a, b, fn=toplam):
    return fn(a, b)

sonuc = islem(10, 20)
print(sonuc)

# Burada fn referans değerdir. Yani fonksiyonu islem olarak çağırdığımzda toplama mı çıkarma mı yapacağını bilemeyeceğinden, islem(10,20,toplam) veya islem(10,20,cikarma)
# yazmamız gerekiyor. Bunu ortadan kaldırmak için default olarak toplam yapsın diyebiliriz. Default parametre yoksa islem(10,20,toplam) veya islem(10,20,cikarma) yazmalıyız.





#Fonksiyon Kullanımı 11: Keyword Arguments

def full_name(firstname: str, lastname: str, age: int=0) -> str:
    return f"Your name is {firstname} {lastname}"

sonuc = full_name("Sadık", "Turan")
sonuc = full_name(lastname="Turan", firstname="Sadık")
sonuc = full_name(lastname="Turan", firstname="Sadık")
sonuc = full_name(firstname="Sadık", lastname="Turan")

print(sonuc)

"""
Keyword arguments (anahtar kelime argümanları), fonksiyonlara parametre adlarıyla birlikte değer geçirmeyi sağlar.

Bu yöntemin avantajları:

Sıralama zorunluluğunu ortadan kaldırır

Normalde, pozisyonel argümanlarda (full_name("Sadık", "Turan")) argümanlar tanımlı sırayla geçilmelidir.
Ancak, keyword arguments kullanıldığında (full_name(lastname="Turan", firstname="Sadık")), parametre sırası önemli olmaz.
Kodun okunabilirliğini artırır

full_name("Sadık", "Turan") yerine full_name(firstname="Sadık", lastname="Turan") yazmak, kodun daha açık olmasını sağlar.
Zorunlu olmayan parametrelerle daha esnek kullanım sağlar

Eğer bazı parametreler varsayılan değer alıyorsa (age=30 gibi), yalnızca gerekli olanlar keyword olarak verilebilir.
"""
