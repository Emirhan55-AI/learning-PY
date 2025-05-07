import random

"""
result = dir(random)
result = help(random)
"""

"""
result = random.random() #0-1 arası rastgele sayı üretir.
result = random.random()*100
result = random.randint(1,100) #1-100 arası rastgele int sayı üretir.
result = random.uniform(10, 120) #10-120 arası rastgele float sayı üretir.
print(result)
"""

"""
names = ["ahmet","mehmet","zübeyir"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names) #Yukarıdakinin kolayı
greetings = "hello there"
result = random.choice(greetings)
print(result)
"""

liste = list(range(10)) #0-10 arası sırasıyla sayı listesi oluşturduk.
shuffles = random.shuffle(liste) #liste elemanlarını rastgele karıştırdık.

liste = range(100)
result = random.sample(liste,3) #liste içerisinden rastgele 3 sayı alır.
names = ["ahmet","mehmet","zübeyir"]
result = random.sample(names,2)
print(result)