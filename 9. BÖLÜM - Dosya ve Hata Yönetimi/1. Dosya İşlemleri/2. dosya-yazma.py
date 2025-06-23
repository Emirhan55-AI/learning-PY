# "w": Write (Yazma) modu
# Bu modda dosya açılırsa:
#  - Eğer dosya mevcut değilse oluşturulur.
#  - Eğer dosya zaten varsa içeriği tamamen silinir ve yeniden yazılır.

# Dosyayı yazma modunda açıyoruz
with open("dosya.txt", "w", encoding="utf-8") as file:
    # write() fonksiyonu ile metin dosyaya yazılır
    # "\n" satır sonu karakteridir, her ismin ayrı satıra yazılmasını sağlar
    file.write("AI\n")
    file.write("Emirhan Uysal\n")
    # with bloğu bitince dosya otomatik olarak kapanır



# Şimdi dosyayı okuma modunda açıyoruz
with open("dosya.txt", "r", encoding="utf-8") as file:
    # Dosyadaki her satır için döngü başlatılır
    for i in file:
        # Satırları ekrana yazdırır
        # end="" → print sonunda fazladan bir boş satır oluşmaması için varsayılan "\n" kaldırılır
        print(i, end="")