from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

################################################################################
# This part prepares preliminary links - links for lists of links :)
################################################################################
url = 'https://www.worlddata.info/capital-cities.php' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'class':re.compile('fl_.*')})

links = ['https://www.worlddata.info' + tag['href'] for tag in tags]

################################################################################
# This part prepares links for countries
################################################################################
i = 0

for link in links:
    print(link)
    i = i + 1
print(i)

d = pd.DataFrame({'name':[], 'region':[], 'area':[], 'local_name':[], 'export':[], 'import':[]})

for link in links[:100]:
    print(link)

    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        capital = bs.find('div',string = 'Capital:').next_sibling.text
    except:
        capital = ''
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    
    try:
        region = bs.find('div',string = 'Region:').next_sibling.text
    except:
        region = ''
    
    try:
        area = bs.find('div',string = 'Area:').next_sibling.text
    except:
        area = '' 
    
    try:
        local_name = bs.find('div',string = 'Local name:').next_sibling.text
    except:
        local_name = ''

    try:
        exp = bs.find('td',string = 'Exportations:').next_sibling.text
    except:
        exp = ''

    try:
        imp = bs.find('td',string = 'Importations:').next_sibling.text
    except:
        imp = ''
        
    try:
        death_penalty = bs.find('a',string = 'Death penalty').parent.next_sibling.text
    except:
        death_penalty = ''
        
    try:
        p_temp = bs.find('div',string = 'Birthrate:').parent.text
        birth_rate = p_temp.replace("Birthrate:", "")
    except:
        birth_rate = ''
        
    try:
        roadways = bs.find('td',string = 'Roadways:').next_sibling.text
    except:
        roadways = ''
    
    try:
        airports = bs.find('a',string = re.compile('(.*)Airport(.*)')).parent.next_sibling.text
    except:
        airports = ''
    
    countries = {'capital':capital, 'name':name, 'region':region, 'area':area, 'local_name':local_name, 'export':exp, 'import':imp, 'death_penalty':death_penalty, 'birth_rate':birth_rate, 'roadways':roadways, 'airports':airports}
    
    d = d.append(countries, ignore_index = True)
    print(d)

################################################################################
# This part saves data to csv.
################################################################################
d.to_csv('countries_bs.csv')

