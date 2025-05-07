selam = "Selamun Aleyküm"

print(selam[0]) #S
print(selam[-1]) #m
print(selam[1]) #e
print(selam[2]+selam[6]) #ln

# Karakter dizisinin uzunluğunu bulma

print(len(selam)) #14

print(selam[2:5]) #2 den başla 4 e kadar 5 dahil değil
print(selam[3:])
print(selam[:9])
print(selam[4:len(selam)])
print(selam[2:14:3]) #3 karakterde bir alır.
print(selam[::])
print(selam[::2]) #birini alır birini almaz
print(selam[::-1]) #tersten yazdırma. 1 yazarsan düz yazdırır.