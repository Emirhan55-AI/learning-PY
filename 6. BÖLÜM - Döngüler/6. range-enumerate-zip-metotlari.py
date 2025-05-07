# range: tek başına da kullanılabilir.

# for item in range(50,100,20):
#     print(item)


# print(list(range(5,100,10)))


# enumerate: index numarası sağlar.

# greeting = 'Hello'
# for index, item in enumerate(greeting,1):
#     print(f'index: {index} letter: {item}')


# zip: Birden fazla listeleri birleştirir.

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)