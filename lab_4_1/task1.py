from bs4 import BeautifulSoup
import requests

csv_file = open("countries_data.csv", "w", encoding='utf-8')
csv_file.write("country,city,area,population\n")
country_list = []
file = open("countries.txt","r", encoding='utf-8')
for line in file:
    url = f'https://en.wikipedia.org/wiki/{line.strip()}'
    headers = {
    'User-Agent': 'CountriesProject/1.0 (student@example.com)'
    }
    response = requests.get(url,headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text,'lxml')
    title = soup.find('span',class_='mw-page-title-main')
    title = title.text
    country_list.append(title)
    
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
            country_list.append(capital)
            
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
                country_list.append(area)
            
        population_th = None
        for th in infobox.find_all('th'):
            th_text = th.get_text(strip=True).lower()
            if 'estimate' in th_text:
                population_th = th
                break
        if population_th:
            raw_population = population_th.find_next_sibling('td').get_text(strip=True)
            population = raw_population.split('[')[0].strip()
            country_list.append(population)
csv_file.writelines(country_list)
file.close()
csv_file.close()

