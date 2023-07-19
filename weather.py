# importing library
import requests
from bs4 import BeautifulSoup

# enter city name
city = "mumbai"

# creating url and requests instance
url = "https://www.google.com/search?q=weather+" + city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str_data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
data = str_data.split('\n')
time = data[0]
sky = data[1]

# getting all div tag
list_div = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = list_div[5].text

# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]


temp = temp.encode('utf-8').decode('utf-8')
time = time.encode('utf-8').decode('utf-8').strip()
sky = sky.encode('utf-8').decode('utf-8').strip()
other_data = other_data.encode('utf-8').decode('utf-8').strip()

# printing all data
print("Temperature is", temp)
#print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
# printing all data
print("Temperature is", temp.encode('utf-8'))
print("Time: ", time.encode('utf-8'))
print("Sky Description: ", sky.encode('utf-8'))
print(other_data.encode('utf-8'))
