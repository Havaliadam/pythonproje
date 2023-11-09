v=int(input("voltaj değeri giriniz:"))
i=int(input("akim değeri giriniz:"))
r=int(input("direnc değeri giriniz:"))


if v==0:
    voltaj=i*r
    print("\n"+ "voltaj değeri:"+str(voltaj)+" "+"v")
elif i==0:
    akim=v/r
    print("\n"+ "akim değeri:"+str(akim)+" "+"amper")
else:
    direnc=v/i 
    print("\n "+"direnç değeri:"+str(direnc)+" "+"direnc")       
