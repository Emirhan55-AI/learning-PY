# Python'da dosya işlemleri için open() fonksiyonu kullanılır.
# Genel kullanım: open(dosya_adı, erişim_modu, encoding)

# "r" modu: okuma modudur. Dosya var olmalıdır.
f = open("log.txt", encoding='utf-8')

# Dosyanın tamamını okur ve string olarak döner
print(f.read())

# İkinci kez okuma yapılırsa boş string döner çünkü cursor dosya sonuna ulaşmıştır
print(f.read())

# Cursor'un (imlecin) konumunu sıfıra alır, yani başa döner
f.seek(0)

# Tüm içeriği tekrar okur
print(f.read())

# Tekrar boş döner çünkü cursor yine sondadır
print(f.read())

# Cursor'u dosya içinde 10. karaktere alır
f.seek(10)

# O konumdan itibaren kalan kısmı okur
print(f.read())

# Cursor'u başa al
f.seek(0)

# readline() ile satır satır okuma yapılır
print(f.readline())  # 1. satır
print(f.readline())  # 2. satır
print(f.readline())  # 3. satır
print(f.readline())  # Artık okuyacak satır kalmadı, boş string döner

# Cursor'u başa al
f.seek(0)

# readlines() tüm satırları liste olarak döner
satirlar = f.readlines()
print(satirlar)  # ['1.satır\n', '2.satır\n', '3.satır']

# Liste elemanlarına indeksle erişilebilir
print(satirlar[0])  # '1.satır\n'
print(satirlar[1])  # '2.satır\n'
print(satirlar[2])  # '3.satır'

# Dosyanın açık olup olmadığını kontrol eder
print(f.closed)  # False → henüz açık

# Dosyayı kapatır
f.close()

# Artık dosya kapalı
print(f.closed)  # True

# Kapalı dosyada işlem yapılmaya çalışılırsa hata alınır. Dosyayı kapatmamızın sebebi bellekte yer kaplamaması içindir.
# f.read()  # ❌ ValueError: I/O operation on closed file.

# Dosyayı tekrar açalım
f = open("log.txt", encoding='utf-8')
print(f.read())
f.close()




# with bloğu ile dosya açmak: Bu yapı, dosyanın işimiz bittiğinde otomatik kapanmasını sağlar
with open("log.txt", encoding="utf-8") as f:
    # Dosyanın tamamını okuyalım
    icerik = f.read()
    print("İçerik:", icerik)

    # Dosya sonuna ulaşıldıktan sonra, cursor dosya sonunda olur.
    # tell() fonksiyonu, cursor'un (dosya içindeki konumun) tam olarak kaçıncı baytta olduğunu verir
    pozisyon = f.tell()
    print("Cursor şu anda dosyada {}. baytta.".format(pozisyon))

# Bu satıra geldiğimizde dosya otomatik olarak kapanmıştır

# Yeni bir örnek: Cursor hareketi ve tell() birlikte gösterilsin
with open("log.txt", encoding="utf-8") as f:
    print("İlk 10 karakter:", f.read(10))  # İlk 10 karakteri oku
    print("Cursor konumu:", f.tell())      # Şu an cursor nerede?

    f.seek(0)  # Cursor'u başa al
    print("Cursor konumu (başa alındıktan sonra):", f.tell())

    satir = f.readline()  # Bir satır oku
    print("Okunan satır:", satir)
    print("Cursor konumu (bir satır okunduktan sonra):", f.tell())