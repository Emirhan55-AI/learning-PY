# x = 5
# y = 10
# z = 20

# x, y, z = 5, 16, 20

# a,b,c = 10,20,(30,40) c bir tupledir. c 30 ve 40 ı içerir.

# d = 10,20 d yine bir tupledir.

# x, y = y, x
# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5
# x %= 5          # x = x % 5
# y //= 5         # y = y // 5
# y **= z         # y = y ** z


values = 1, 2, 3, 4, 5 #z basında * olmasaydı  hata verirdi çünkü fazlalık oluşurdu.* koyarak z yi liste haline getirdik.

print(values)
print(type(values))

x, y, *z = values

print(x, y, z)
print(x, y, z[1])
