username = "Emirhan"
password =12345
password = str(password)
username2=input("Kullanıcı adını girin: \n")
password2=input("Şifrenizi girin: \n")



'''if username==username2 and password==password2 : 
    print(f'Hoşgeldiniz {username} Bey -> Şifreniz : {password}')
else : 
    print("Bilgiler yanlış !!!emir")'''



#2.ÖRNEK
if username==username2:
    if password==password2:
         print("Hoşgeldiniz")
    else:
          print("parola yanlış")     
else:
     print("username yanlış")    



# elif kullanımı 

# x = int(input('x: '))
# y = int(input('y: '))

# if x > y:
#     print('x y den büyük')
# elif x == y:
#     print('x y eşit')
# else:
#     print('y x den büyük')



num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')
