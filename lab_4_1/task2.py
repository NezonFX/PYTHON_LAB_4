from bs4 import BeautifulSoup
import requests
import os

csv_file = open("countries_data.csv", "w", encoding='utf-8')
csv_file.write("country,city,area,population\n")
file = open("countries.txt","r", encoding='utf-8')
for line in file:
    if line == "":
        continue
    capital = ""
    area = ""
    population = ""
    cache = "cache/"+ line.strip() +".html"
    if os.path.exists(cache):
        print("Из кэша: ", line)
        cache_file = open(cache,"r",encoding='utf-8')
        html = cache_file.read()
        cache_file.close()
    else:
        print("Скачиваем: ",line)   
        url = f'https://en.wikipedia.org/wiki/{line.strip()}'
        headers = {
        'User-Agent': 'CountriesProject/1.0 (student@example.com)'
        }
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        html = response.text
        
        cache_file = open(cache,"w",encoding='utf-8')
        cache_file.write(html)
        cache_file.close()
        

        soup = BeautifulSoup(response.text,'lxml')
        title = soup.find('span',class_='mw-page-title-main')
        title = title.text

        infobox = soup.find('table', class_='infobox')

        if infobox:
            capital_th = None
            for th in infobox.find_all('th'):
                th_text = th.get_text(strip=True).lower()
                if 'capital' in th_text:
                    capital_th = th
                    break
            if capital_th:
                capital = capital_th.find_next_sibling('td').find('a').get_text(strip=True)

            area_th = None
            for th in infobox.find_all('th'):
                th_text = th.get_text(strip=True).lower()
                if 'total' in th_text:
                    area_th = th
                    break
            if area_th:
                raw_area = area_th.find_next_sibling('td').get_text(strip=True)
                if 'km2' in raw_area:
                    new_area = raw_area.split('km2')[0].strip()
                    area = new_area.split('[')[0].strip()

            population_th = None
            for th in infobox.find_all('th'):
                th_text = th.get_text(strip=True).lower()
                if 'estimate' in th_text:
                    population_th = th
                    break
            if population_th:
                raw_population = population_th.find_next_sibling('td').get_text(strip=True)
                population = raw_population.split('[')[0].strip()
        csv_file.write(f"{title},{capital},{area},{population}\n")
file.close()
csv_file.close()
