#fatura bilgiler
ocak=mart=mayıs=ağustos=ekim=aralık=31
nisan=haziran=eylül=kasım=30
şubat=28

#metreküp fiyati
birimfiyat = 4.88
#aylık kac metreküp dogalgaz kullanımi
aylikmetrekupkullanim=input("aylik kaç metre küp dogalgaz kullandiniz:? ")

#ay belirtme
donem=input("hangi ay :")


ay=eval(donem)

#günlük kullanımı
gunlukkullanma=int(aylikmetrekupkullanim)/ay

#fatura oluşturma

fatura=birimfiyat*gunlukkullanma*ay

print("günlük kullanım :\t",gunlukkullanma,"metreküp cinsinden  \n","fatura tutari:\t",fatura,"TL",sep="")

