from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re

gecko_path = '/home/olga/geckodriver'

url = 'https://www.worlddata.info/capital-cities.php'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox(options = options, executable_path = gecko_path)
driver.maximize_window()

# Actual program:
driver.get(url)
print(driver.page_source)

time.sleep(2)

# need to click on a cookie files information that hides proper button 
button = driver.find_element_by_xpath('//*[@id="cookiebtn"]')

button.click()

time.sleep(2)

buttons = driver.find_elements_by_xpath('/html/body/div[1]/div/main/div/div/table/tbody/tr/td[1]/a')

buttons_hrefs = [site.get_attribute('href') for site in buttons]

d = pd.DataFrame({'name':[], 'region':[], 'area':[], 'local_name':[], 'export':[], 'import':[]})

for value in buttons_hrefs[0:100]:
	driver.get(value)
	time.sleep(1)

	actions = ActionChains(driver)
	
	# need to click on the random place of a website to dismiss Google Add if one appears
	actions.move_by_offset(400, 477).click().perform()

	time.sleep(1)
	
	h = driver.find_element_by_xpath("//*[text()='Capital:']/following-sibling::div").text
	print(h)

	i = driver.find_element_by_xpath('/html/body/div/div/main/div[1]/div[2]/div[1]/h1').text
	print(i)

	j = driver.find_element_by_xpath('/html/body/div/div/main/div[1]/div[2]/div[3]/div[2]').text
	print(j)

	k = driver.find_element_by_xpath('/html/body/div/div/main/div[1]/div[2]/div[3]/div[4]').text
	print(k)

	l = driver.find_element_by_xpath("//*[text()='Local name:']/following-sibling::div").text
	print(l)

	m = driver.find_element_by_xpath("//*[text()='Exportations:']/following-sibling::td").text
	print(m) 

	n = driver.find_element_by_xpath("//*[text()='Importations:']/following-sibling::td").text
	print(n) 
	
	try:
		o = driver.find_element_by_xpath("//*[text()='Death penalty']/parent::td/following-sibling::td").text
		print(o) 
	except:
		o = ''
		
	try:
		p_temp = driver.find_element_by_xpath("//*[text()='Birthrate:']/parent::div").text
		p = p_temp.replace("Birthrate:\n", "")
		print(p) 
	except:
		p = ''
	
	try:
		r = driver.find_element_by_xpath("//*[text()='Roadways:']/following-sibling::td").text
		print(r) 
	except:
		r = ''
		
	try:
		s = driver.find_element_by_xpath("//*[text()='Airports']/parent::td/following-sibling::td").text
		print(s) 
	except:
		s = ''


	country = {'capital':h, 'name':i, 'region':j, 'area':k, 'local_name':l, 'export':m, 'import':n, 'death_penalty':o, 'birth_rate':p, 'roadways':r, 'airports':s}
	
	d = d.append(country, ignore_index = True)
	
	driver.back()

d.to_csv('countries_selenium.csv')

time.sleep(1)

# Close browser:
driver.quit()
