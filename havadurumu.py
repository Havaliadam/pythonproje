import re
import requests

url="https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html"

site=requests.get(url).content.decode("utf-8")

r_gunduz="<td>24°</td>"
r_gece="<td>17°</td>"
r_tarih=" <td>7 Kas Sal</td>"
r_havadurumu="""<th> 
<a href="https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html" title="İstanbul Hava Durumu" target="_blank">Hava durumu</a>
</th>"""

r_yagis="<th>Yağiş</th>"

comp_gundud=re.compile(r_gunduz)
comp_gece=re.compile(r_gece)
comp_tarih=re.compile(r_tarih)
comp_havaduruöu=re.compile(r_havadurumu)
comp_yagis=re.compile(r_yagis)

gunduz=[]
gece=[]
tarih=[]
havadurumu=[]
yagis=[]
for i in re.findall (r_gunduz,site):
    gunduz.append(i)
for i in re.findall(r_gece,site):   
    gece.append(i)
for i in re.findall(r_tarih,site):   
    tarih.append(i)
for i in re.findall(r_havadurumu,site):   
    havadurumu.append(i)
for i in re.findall(r_yagis,site):   
    yagis.append(i)
                    
print("*"*70)
print("                adana hava durumu")
print("*"*70)
for i in range(0,len(tarih)):
    
    print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], yagis[i], gunduz[i], gece[i], havadurumu[i]))
    print("-" * 75)