"""
Pythonda isimsiz olarak tanımladığımız fonksiyonlara lambda fonksiyonları denir. 

Örneğin bir sayının karesini mi kübünü mü almak istediğinizden emin değilsiniz bu durumda bir 
fonksiyon içerisinde lambda tanımlaması yaparak istediğimiz bir aşamada geriye çalıştırılabilir 
bir fonksiyon döndürebilirsiniz.

Python'da lambda, tek satırlık fonksiyonlardır. Bir ya da daha fazla parametre kabul ederler, 
ancak tek bir işlem yapabilirler. 
"""
#Normal bir fonksiyonun çalışması
def square(num): return num**2
number = square(20)
print(number)

#Lambda' nın çalışması 
sonuc = (lambda a: a**2)(5)
print(sonuc)
#or
kupAl = lambda a: a**3
sonuc2 = kupAl(25)
print(sonuc2)

#Lambda Örnek 1
toplama = lambda a,b,c: a+b+c
print(toplama(20,35,45))

#Lambda Örnek 2: Fonkisyon içinde kullanımı.
def MyFunc(n):
    return lambda a:a*n

carpma1 = MyFunc(5)
carpma2 = MyFunc(10)

sonuc1 = carpma1(20)
sonuc2 = carpma2(35)

print(sonuc1)
print(sonuc2)