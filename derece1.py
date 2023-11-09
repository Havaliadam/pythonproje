derece=int(input("santigrat cinsiden derece giriniz ="))


fahreit=(derece*9/5)+32
try:
    
    print("fahreit   sonuc değeri ="+str(fahreit)+" K")
except:
    print("sonuc tip uyumsuzluğu")    