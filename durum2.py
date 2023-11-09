from bs4 import BeautifulSoup
import requests

# isteği yaparken web tarayıcı bilgisini göndereceğimizden headers kısmına bunu tanımlıyoruz.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# weather adında ve tek değer alan (city) fonksiyon tanımlıyoruz.
def weather(city):
    city = city.replace("", "+")
# get metodu ile ilgili url'e headers'ı da dahil ederek isteğimizi yapıyoruz.
# bu url'in içinde girmiş olduğumuz şehir bilgisi olacak ve cevabı bu şehir özelinde verecek.
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)

    print("Searching in google......\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + "°C")


print("enter the city name")
city = input()
city = city + " weather"

# yukarıda hazırlamış olduğumuzu weather fonksiyonunu city değişkeni ile çağırıyoruz.
weather(city)

# fonksiyon başarılı bir şekilde çalıştığında sırasıyal bize; lokasyon, zaman, bilgi ve Celcius derecesinden sıcaklığı gösterecek.