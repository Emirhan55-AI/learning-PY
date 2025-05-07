import math #Modül dahil etmek.
import math as islem #math kütüphanesine islem takma adını verdik. Böylelikle math. yerine islem. olarak kullanabiliriz.

#YÖNTEM 1
"""
value = dir(math) #Kullanılabilir fonksiyonları gösterir.
value2 = help(math) #Tüm fonksiyonların nasıl kullanıldığını gösterir.
value3 = help(math.ceil) #Sadece ceilin kullanımını gösterir.
"""

"""
value = islem.cos(20)
value2 = islem.sqrt(49)
"""

#YÖNTEM 2
"""
from math import * #Tüm math fonksiyonlarını artık math. yazmadan kullanabilirsin.
value = sqrt(49)
value2 = sinh(35)
"""
"""
from math import factorial,ceil #Sadece dahil ettiğin fonksiyonları kullanabilirsin.
value = factorial(6)
value2 = sin(30) #Bunu kullanamazsın.
"""

def sqrt(x):
    print("x : "+str(x))
    
from math import sqrt
value = sqrt(20)

#Burada def ile tanımlanan sqrt yerine from math ile tanımladığımız sqrt kullanılır. Aynı isimli fonksiyonlardan hangisi en son yazılırsa o kullanılır.