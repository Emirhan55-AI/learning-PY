# key - value : Bir bilgiye ulaşmak için anahtar-bilgiye ihtiyaç duyulur. Sıralanabilir,güncellenebilir,tekrarlanamaz.

# plakalar = { 'kocaeli' : 41, 'istanbul': 34 }
# print(plakalar['kocaeli']) --> 41
# print(plakalar['istanbul']) --> 34


# plakalar['ankara'] = 6 --> veri ekledik
# plakalar['kocaeli'] = 19 --> veriyi değiştirdik


# print(plakalar)



users = {
    'sadikturan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

print(users['cinarturan']['roles'][0])

