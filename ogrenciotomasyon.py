#yazılımcının arge ofisi
dosya= open("ogrenci.txt")

print("""
      Ögrenci bilgi otomasyon projesi
      --------------işlemler----------
      1-öğrenci ekle
      
      """)

secim=int(input("seçim yapiniz :"))
while True:
    if secim==1:
        dosya=open("ogrenci.txt","a")
        ad=input("ögrenci ad :")
        soyad=input("ögrenci soyad :")
        no=int(input("ogrenci numara :"))
        dosya.write("\n")
        dosya.write("-----------------")
        dosya.write("oğrenci ad: "+ad)
        dosya.write("\n")
        dosya.write("oğrenci soyad: ",soyad)
        dosya.write("\n")
        dosya.write("oğrenci numara: ",str(no))
        dosya.write("\n")
        dosya.write("-----------------")
    break
dosya.close()