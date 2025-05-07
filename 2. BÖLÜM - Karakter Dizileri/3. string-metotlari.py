message = "    Bismillah. Rahman! rahim"
# Bu metotların her biri orijinali asla değiştirmez yeni bir değere atanarak farklı bir veri olur.



# 1.KISIM: 
'''
message =message.upper()
message =message.lower()
message =message.title() #Her harfin başını büyük yapar
message =message.capitalize() #İlk harfi büyük yapar
sonuc = "abc".islower() #Yazılan yazı küçük mü = True (.isupper()) dersen büyük mü diye sorarsın.
sonuc= message.count(.) #Kaç tane . var cümlede onu bulur.
sonuc = message.isalpha() #cümle içerisinde ki karakterler harflerden mi oluşuyor.
'''

# 2.KISIM: 
'''
message =message.strip() #Baştaki boşluğu kaldırır.
message =message.split() #Mesaj liste haline gelir.
message =message.split('.')  #Noktadan itibaren ayırır kelimeleri
message =message.split('!') #Ünlemden sonra ayırır kelimeyi
sonuc = message.index("Rahman") #bu kelime kaçıncı indexten başlıyor onu verir.
'''

# 3.KISIM: 
'''
message = ' '.join(message) #Aralara boşluk ekler
message = '*'.join(message) #Aralara * ekler
message = '---'.join(message)

index = message.find("Bismillah") #bağlantılı2 cümle içinde Bismillahı arar
print(index) #bağlantılı2 Bismillah kaçıncı indexte onu yazar Eğer cümlede öyle bir kelime yoksa -1 döner.

isFound = message.startswith(' ') #Cümle boşlukla mı başlıyor
isFound2 = message.startswith('B') #Cümle büyük B ile mi başlıyor onu bulur.
isFound3 =message.endswith("m")
print(isFound)
print(isFound2)
print(isFound3)
'''

# 4.KISIM: 

'''
message = message.replace('Bismillah','ALLAH') #Bismillah yerine ALLAH yaz
message = message.replace(' ','*') #Boşluk yerine yıldız ekle.
message = message.replace('Bismillah','Rahman').replace('rahim','Rahim')
'''

# 5.KISIM: 
'''
message = message.center(100) #100 karakter sağdan soldan boşluk bırakır.
message = message.center(50,'!') #O boşluklara ünlem koyar.
'''


'''
print(message)
print(message[2]) #bağlantılı 
'''

#GOOGLE'DAN STRİNG METHODS BULABİLİRSİN.