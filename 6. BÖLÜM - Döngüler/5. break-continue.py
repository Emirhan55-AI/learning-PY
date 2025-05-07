#break döngüden tamamen çıkış yapar,continue sadece o anki döngü turunu iptal eder ve döngü devam eder.

# name = 'Sadık Turan'

# for letter in name:
#     if letter == 'ı':
#         continue buraya break yazarak kodu bir daha dene
#     print(letter)

# x = 0

# while x < 5:    
#     x+=1 eğer bunu başa değil de sona yazsaydın sürekli 2 de takılı kalacaktı. 
#     if x == 2:
#         continue
#     print(x)


# 1- 100 e kadar tek sayıların toplamı

x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'toplam: {result}')