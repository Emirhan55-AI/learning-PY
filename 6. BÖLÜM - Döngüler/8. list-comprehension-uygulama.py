# 1. Soru Çözümü
liste = [i for i in range(1,101) if i%3==0 if i%4==0]
print(liste)

# 2. Soru Çözümü
text = "Hello 12345 World"
sonuc= [i for i in text if i.isdigit()]
print(sonuc)

# 3. Soru Çözümü
sicakliklar = [20,15,0,-5,-2]
sonuc = [i if i>=4 else "buzlanma tehlikesi" for i in sicakliklar]
print(sonuc)

# 4. Soru Çözümü
ogrenciler = ["ali","ahmet","veli"]
notlar = [50,60,70]

liste = [(ogrenciler[i],notlar[i]) for i in range(0,len(ogrenciler))]
liste_dic = {key:value for (key,value) in liste if value>50}
print(liste_dic)

# 5. Soru Çözümü
liste = [(x,y) for x in range(3) for y in range(3)]
print(liste)