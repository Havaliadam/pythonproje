from datetime import *
dogumgunu=datetime.strptime(input("dogum gününüz giriniz(gün.ay.yil):") ,"%d.%m.%Y")

yas =datetime.now()-dogumgunu

print("bu  kadar yaşadiniz {} saniye ".format(yas.total_seconds()))




