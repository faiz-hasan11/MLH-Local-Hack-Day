from bs4 import BeautifulSoup
import requests
try:
    url = 'https://localhackday.mlh.io/build'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    names = soup.find_all('h3',class_='hero-sub-head event')
    sorted_names = []
    for name in names:
        sorted_names.append(name.text)
    sorted_names = list(set(sorted_names))
    for i in range(len(sorted_names)):
        for j in range(i+1,len(sorted_names)):
            if sorted_names[i] > sorted_names[j]:
                temp = sorted_names[i]
                sorted_names[i] = sorted_names[j]
                sorted_names[j] = temp
    for i in sorted_names:
        print(i)
except:
    print("Connection Error.Retry!")