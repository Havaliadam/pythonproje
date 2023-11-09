print("not : türkçe karakter kullanmayin \n")



cumle_gir=input("cümle ve kelime giriniiz:")
yazi_tersi=""

def tersi_al(yazi,tersi):
    for i in range(len(yazi)-1,-1,-1):
        tersi+=yazi[i]
    return tersi

kelimeler=[]
for i in cumle_gir.split(' '):
    kelimeler.append(tersi_al(i,""))
cumle_tersi=tersi_al(cumle_gir,yazi_tersi)
kelime_tersi=" ".join(kelimeler)

print("""
      
      Cümlenin girilen hali :         {}
      
      Tamamen ters hali :        {}
      
      Kelime kelime ters hali :{}
      
      
      """.format(cumle_gir,cumle_tersi,kelime_tersi))



    
       