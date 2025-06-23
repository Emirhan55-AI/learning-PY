# "a": Append (Eklemek) modu.
#       Dosya yoksa oluşturur.
#       Varsa içeriği silmeden en sona ekleme yapar.

# "r+": Hem Read (okuma) hem Write (yazma) modudur.
#       Dosya mevcut olmalıdır, yoksa hata verir.
#       Dosyanın başından itibaren hem okuyabilir hem de üzerine yazabilirsiniz.

with open("dosya2.txt", "r+", encoding="utf-8") as file:
    # file.seek(20) → bu satır yorumda. Aktif olsaydı, cursor 20. bayta giderdi.
    # Dosyanın tamamını, o anki cursor konumundan itibaren okur
    print(file.read())  

    # Cursor şu anda dosya sonunda olduğu için, yazılacak veri sona eklenmiş gibi olur
    # Bu satır, dosyaya "yeni satır" ifadesini ekler
    file.write("yeni satır\n")

# NOT: Eğer yukarıdaki seek() satırı aktif olsaydı, yazma işlemi cursor'un o andaki konumundan itibaren başlardı.
# Bu durumda "yeni satır" yazısı, önceki içeriğin ortasına yazılabilir (üzerine yazma - overwrite).

with open("dosya2.txt", "a", encoding="utf-8") as file:
    file.write("Bu satır append ile eklendi.\n")
    file.write("Dosyanın sonuna veri ekleniyor.\n")
