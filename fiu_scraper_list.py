# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 14:49:33 2016

@author: 430004498
"""


from selenium import webdriver
import time

path_to_chromedriver = "D:\\Usuarios\\430004498\\Documentos\\chromedriver"

browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = "https://www.fiu.mx/auto/info"

browser.get(url)



lista=[]

aa=browser.find_element_by_xpath('//*[(@id = "year")]')
options=[x for x in aa.find_elements_by_tag_name("option")] 

for element in options:    
    browser.find_element_by_xpath('//*[(@id = "year")]/option[contains(text(), "'+element.get_attribute("value")+'")]').click()
    time.sleep(1)    
    bb=browser.find_element_by_xpath('//*[(@id = "make")]')
    options1=[x for x in bb.find_elements_by_tag_name("option")] 
    for element1 in options1:
        browser.find_element_by_xpath('//*[(@id = "make")]/option[contains(text(), "'+element1.get_attribute("value")+'")]').click()
        time.sleep(1)        
        cc=browser.find_element_by_xpath('//*[(@id = "model")]')
        options2=[x for x in cc.find_elements_by_tag_name("option")]
        for element2 in options2:
            browser.find_element_by_xpath('//*[(@id = "model")]/option[contains(text(), "'+element2.get_attribute("value")+'")]').click()
            time.sleep(1)            
            dd=browser.find_element_by_xpath('//*[(@id = "type")]')
            options3=[x for x in dd.find_elements_by_tag_name("option")]
            for element3 in options3:
                browser.find_element_by_xpath('//*[(@id = "type")]/option[contains(text(), "'+element3.get_attribute("value")+'")]').click()
                time.sleep(1)                
                ee=browser.find_element_by_xpath('//*[(@id = "description")]')
                options4=[x for x in ee.find_elements_by_tag_name("option")]
                for element4 in options4:
                    dict = {}
                    dict["anio"]=element.get_attribute("value")
                    dict["marca"]=element1.get_attribute("value")
                    dict["submarca"]=element2.get_attribute("value")
                    dict["linea"]=element3.get_attribute("value")
                    dict["descripcion"]=element4.get_attribute("value")
                    lista.append(dict)
                    print element.get_attribute("value")+element1.get_attribute("value")+element2.get_attribute("value")+element3.get_attribute("value")+element4.get_attribute("value")
        
        
        
import pandas as pd

catalogo = pd.DataFrame(lista)
    
catalogo.to_excel("catalogo_fiu.xlsx")
