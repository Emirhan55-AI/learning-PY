numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# 1. KISIM
val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

# 2. KISIM: Ekleme
numbers.append(49)
numbers.append(59)
letters.append("emirhan")
numbers.insert(3, 78) # 3. indekse 78 sayısını ekle. 3. indeks değişmez bir sağa kayar.
numbers.insert(-1,52)
letters.insert(0,"ahmet")

#3. KISIM: Silme
# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)

#4. KISIM: Sıralama
numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()
print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

#5. KISIM
print(numbers.count(10))
print(letters.count('a'))
print(numbers.index(10))

numbers.clear()
print(numbers)