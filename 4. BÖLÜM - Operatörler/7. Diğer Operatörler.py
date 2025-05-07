# Identity Operator: is

# x = y = [1, 2, 3]
# z = y

# print(x==y) # True, bu durumda sadece değerlerin aynı olup olmadığına bakar.
# print(x==z)
# print(x is y) # Burada sonuç false olur çünkü ikisi farklı objelerdir.
# print(x is z) # True


x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x==y)
print(x is y)
print(x is not y)


# Membership Operator: in

x = ['apple','banana']
print('banana' in x)

name = 'Çınar'
print('a' in name)
print('a' not in name)
