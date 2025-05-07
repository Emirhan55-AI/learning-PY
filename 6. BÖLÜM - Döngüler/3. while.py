# while koşullu durumlarda kullanılır.

#Sonsuz döngü 
# x=0
# while True:
#     print(x)

#1-100 e kadar olan sayılar
x=0
while x<100:
    print(x) #önce yazmak 0'ı dahil eder.
    x+=1

#Tek ve çift sayıları yazdırmak
t=0
while t<=100:
    if t%2==0:
        print(f'{t} sayisi cifttir.')
    else:
        print(f'{t} sayisi tektir.')
    t+=1

#Kullanıcıdan ismini girene kadar adını isteme
name ='' #Bu bir False değere eşittir
while not name.strip(): #Yani not name demek = True demektir.
    name =input("İsminizi girin : ")
    print(f'Hoşgeldiniz {name}')