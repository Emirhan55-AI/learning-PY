# markalar.txt dosyasını ekleme (append) modunda açıyoruz
# Dosyanın sonuna "6-Bmw\n" satırını ekler
with open("markalar.txt", "a") as file:
    file.write("6-Bmw\n")

# markalar.txt dosyasını hem okuma hem yazma (read+write) modunda açıyoruz
# Bu blok yorum satırına alınmış ama açıklamak gerekirse:
# 1. Dosyadaki tüm içeriği okur
# 2. Başına "1-Toyota\n" ekler
# 3. Dosya konumunu başa sarar
# 4. Güncellenmiş veriyi dosyaya yazar
# with open("markalar.txt", "r+", encoding="utf-8") as file:
#     markalar = file.read()
#     markalar = "1-Toyota\n" + markalar
#     file.seek(0)
#     file.write(markalar)

# markalar.txt dosyasını hem okuma hem yazma modunda açar
# Bu sefer satır satır okuma ve araya veri ekleme işlemi yapılır
with open("markalar.txt", "r+", encoding="utf-8") as file:
    markalar = file.readlines()                 # Tüm satırları liste olarak okur
    markalar.insert(2, "3-Renault\n")           # Listenin 3. satırına "3-Renault\n" ekler (indeks 2)
    file.seek(0)                                # Dosya başına döner
    # Aşağıdaki döngü, her bir satırı teker teker yazmak içindi ama yorum satırı yapılmış
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)                   # Tüm listeyi dosyaya satır satır yazar

# markalar.txt dosyasını sadece okuma modunda açar ve içeriği ekrana yazdırır
with open("markalar.txt", "r", encoding="utf-8") as file:
    print(file.read())                          # Dosyanın tüm içeriğini yazdırır
