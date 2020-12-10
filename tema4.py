import json
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Python_(genus)"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
# preluare tabel care se gaseste in dreapta paginii wikipedia legata de specia de sarpe Python
tab = soup.find("table", {"class":"infobox biota"})
table_body = tab.find('tbody')
'''
pentru a prelua elementele tabelului, in urma verificarii paginii cu inspect
am observat ca acestea se afla intre tag-ul <tr> </tr>
 '''
rows = table_body.find_all('tr')

''' 
afisarea elemenentelor sub forma unor ellemente din matrice 
'''
for row in rows:
    data = row.find_all('td')
    data = [elem.text.strip() for elem in data]
    if (data and data[0] == 'Kingdom:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Phylum:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Class:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Order:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Suborder:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Family:'):
        print(data[0] + " " + data[1])
    if (data and data[0] == 'Genus:'):
        print(data[0] + " " + data[1])

# scrierea intr-un fisier de tip HTML a elementelor aflate intre tag-urile <td> </td>
with open("output1.html", "w", encoding='utf-8') as file:
    file.write(str(row.find_all('td')))

