# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:10:42 2016

@author: 430004498
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


path_to_chromedriver = "D:\\Usuarios\\430004498\\Documentos\\chromedriver"

browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = "https://www.fiu.mx/auto/info"


def get_fiu(anio,marca,submarca,tipo,descripcion,cp):
    
    browser.get(url)

    browser.find_element_by_xpath('//*[(@id = "year")]/option[contains(text(), "'+anio+'")]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[(@id = "make")]/option[contains(text(), "'+marca+'")]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[(@id = "model")]/option[contains(text(), "'+submarca+'")]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[(@id = "type")]/option[contains(text(), "'+tipo+'")]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[(@id = "description")]/option[contains(text(), "'+descripcion+'")]').click()
    time.sleep(0.5)

    postalcode = browser.find_element_by_xpath('//*[(@id = "postalcode")]')
    postalcode.send_keys(cp)
    first_name = browser.find_element_by_xpath('//*[(@id = "first_name")]')
    first_name.send_keys("Juan")
    last_name = browser.find_element_by_xpath('//*[(@id = "last_name")]')
    last_name.send_keys("Arredondo")
    last_name_maternal = browser.find_element_by_xpath('//*[(@id = "last_name_maternal")]')
    last_name_maternal.send_keys("Zapata")
    email = browser.find_element_by_xpath('//*[(@id = "email")]')
    email.send_keys("aaa@hotmail.com")
    phone = browser.find_element_by_xpath('//*[(@id = "phone")]')
    phone.send_keys("5555874578")
    mobile = browser.find_element_by_xpath('//*[(@id = "mobile")]')
    mobile.send_keys("554578457878")
    browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "quote-now", " " ))]').click()
    
    time.sleep(60)
    
    #1-rc,2-basica,3-amplia,4-ampliaplus
    
    html_source = browser.page_source
    
    soup = BeautifulSoup(html_source,"html.parser")
    
    table = soup.find("table", { "class" : "table additional-offer" })
    
   
    
    data = []
    
    rows = table.find_all('tr')
     #AXA=rows[1].find('div',{'data-id':'AXA::2'})
    #AXA.find('div', { 'class':["",'annual'] })
    for row in rows:
        row.find
        cols = row.find_all(True, { 'class':["",'annual'] } )
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    
    precios = pd.DataFrame(data)
    
    precios = precios.iloc[1:7,[0,3,6,9]]
    
    print precios
    
    
    
    
import xlrd

wb = xlrd.open_workbook("D:\\Usuarios\\430004498\\Documentos\\Prueba_python_fiu.xlsx")

wb_cotz = wb.sheet_by_index(0)

for rows in range(wb_cotz.nrows):
    anio        = wb_cotz.row(rows)[0]
    marca       = wb_cotz.row(rows)[1]
    submarca    = wb_cotz.row(rows)[2]
    tipo        = wb_cotz.row(rows)[3]
    descripcion = wb_cotz.row(rows)[4]
    cp          = wb_cotz.row(rows)[5]
    anio        = str(int(anio.value))
    marca       = str(marca.value)
    submarca    = str(submarca.value)
    tipo        = str(tipo.value)
    descripcion = str(descripcion.value)
    cp          = str(int(cp.value))