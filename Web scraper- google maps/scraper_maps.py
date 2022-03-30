from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time 
import string
import openpyxl
import os
import csv
import re



driver = webdriver.Firefox()
wait = WebDriverWait(driver,5)


driver.get('http://www.google.com/maps')
#driver.maximize_window()


widget=driver.find_element_by_class_name("VfPpkd-LgbsSe")
button=driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div/button')
button.click()


button=driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/button")
button.click()
button=driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div/button")
button.click()
button=driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div[2]/div[1]/div/button")
button.click()
button=driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/form/div/button")
button.click()

#Finding the search box 
searchbox=driver.find_element_by_id('searchboxinput')
location= "Wielkopolskie"
searchbox.send_keys(location)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
cancelbut=driver.find_element_by_class_name('gsst_a')
time.sleep(2)
cancelbut.click()
searchbox.send_keys("domy modulowe")
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

driver.execute_script("function sleep(ms) {  return new Promise(resolve => setTimeout(resolve, ms));} var x = document.getElementsByClassName('siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc siAUzd-neVct-Q3DXx-BvBYQ'); var y = x[1]; y.setAttribute('class','siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc siAUzd-neVct-Q3DXx-BvBYQ siAUzd-neVct-YbohUe-bnBfGc'); y.setAttribute('id','essa'); var z = document.getElementById('essa'); z.scrollTop=z.scrollHeight;sleep(20);z.scrollTop=z.scrollHeight")
time.sleep(2)
driver.execute_script("var z = document.getElementById('essa'); z.scrollTop=z.scrollHeight;")
time.sleep(2)

#entries = driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

wb= openpyxl.load_workbook("C:/Users/MAXJ/Documents/Python/Web scraper- google maps/modulowe.xlsx")
sheetname=wb.get_sheet_names()[0]
print(sheetname)
sheet=wb[sheetname]
sheet.title ="modulowe"

f = open("firmy.csv",'w')
writer = csv.writer(f)    

href=[]

href =driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
#print(href)
dummy = 0
links = []
for entry in href:
    links.append(entry.get_attribute("href"))

for entry in links:
    print(entry)
    #href = driver.find_element_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd").get_attribute("href")
    driver.get(entry)
    time.sleep(5)

    data_format = []
    #name = driver.find_element_by_class_name("x3AX1-LfntMc-header-title-title").text
    name = driver.find_element_by_class_name("gm2-headline-5").text
    data = driver.find_elements_by_class_name("QSFF4-text") 
    print(name)
    print(data)

    for smallData in data:
        Essa = smallData.text
        try:
           sheet.append([name,Essa])
           row = ("{},{},{}").format(name,data)
           print(row)
           writer.writerow(row)
        except IndexError:
            pass
    time.sleep(2)
    #labels=[]
    #name= entry.find_element_by_class_name('qBF1Pd').text
    #adress= entry.find_element_by_class_name('ZY2y6b-RWgCYc').text
    #phone = entry.find_element_by_class_name('ZY2y6b-RWgCYc').text
    #company = entry.find_element_by_class_name('CUwbzc-content').text
    #re.split(r'[.\n]', company)
    #print(company)

    #Try/except  to write the extracted info in the Excel file pass if doessn't exist 
    #try:
        #sheet.append([location,company])
        #row = ("{},{},{}").format(location,company)
        #print(row)
        #writer.writerow(row)
    #except IndexError:
        #pass
 
#saving the excel file 
f.close()
wb.save("modulowe.xlsx")
