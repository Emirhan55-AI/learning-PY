name = "Emirhan"
surname ="Uysal"

print("My name is {} and surname is {}".format(name,surname))
print("My name is {1} and surname is {0}".format(name,surname))
print("My name is {s} and surname is {n}".format(n=name,s=surname))
print("My name is {} and surname is {} I'm {} years old".format(name,surname,36))
print("My name is {} and surname is {} and is {}".format(name,name,name))


# fstring

print(f"My name is {name} {name} {name}")


# Başka bir örnek 

s='12345'*10
print(s)
print(s[::5]) #Sadece 1 leri alır



# Başka bir örnek 

result = 200/700
print("Result is : {}".format(result))
print("Result is : {k:10.4}".format(k=result)) #Boşluk bırakma ve virgülden sonraki kısım Result is ile arasına 10 bosluk ve virgülden sonra 4 sayı alır.