# Örnek 1
sayilar = [1,3,5,4,-1,-4,3,0,24]
sonuc = list(filter(lambda a: a<0, sayilar))
print(sonuc)

# Örnek 2
sonuc2=list(filter(lambda a:a%2==0, sayilar))
print(sonuc2)

# Örnek 3
isimler =["emirhan","ahmet","arda","köfteci yusuf XD"]
sonuc3 = list(filter(lambda a:a[0]=="a", isimler))
print(sonuc3)

# Örnek 4
sonuc4 = list(map(lambda x:x.upper(),filter(lambda a:a[0]=="a",isimler)))
print(sonuc4)

# Örnek 5
users = [
    {"username": "sadikturan", "posts": ["post 1", "post 2"]},
    {"username": "ahmetturan", "posts": []},
    {"username": "yigitbilgi", "posts": ["post 1", "post 2", "post 3"]}
]

filteredUsers = list(filter(lambda u: len(u["posts"]) > 0, users))
sonuc = list(map(lambda u: u["username"], filteredUsers))

sonuc = [user["username"].upper() for user in users if len(user["posts"]) > 0] #List comprehension ile daha kolay.

print(sonuc)
