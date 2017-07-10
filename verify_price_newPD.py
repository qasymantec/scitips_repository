# -*- coding: utf-8 -*-
import unittest,sys,time,re
import  ConfigParser
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException


report = open("result.html","w")
report.write('<html><body><table border ="1"><tr><th>URL</th><th>One Year Entitlement</th><th>Two Year Entitlement</th><th>Three Year Entitlement</th></tr>')

f =  open('swift_data.txt','r')
#f =  open('file_2line.txt','r')

for line in f.readlines():                      
    url = line
    print "################################################################################################################"
    print url
    driver = webdriver.Firefox()
    #driver = webdriver.Remote(command_executor='http://10.72.113.117:7500/wd/hub' ,desired_capabilities = {"browserName": "firefox","platform": "WINDOWS"})
    driver.get(url)
    driver.set_window_size(1300, 1080)
    
    try:
        if driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[2]').is_displayed():
            count = 1
        else:
            count = 2
    except:
        count=2
        pass
    try:
        if driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[3]').is_displayed():
            count2 = 1
        else:
            count2 = 2
    except:
        count2=2
        pass
    
    
    print "price verify for 1 year subscription"
    time.sleep(3)
    driver.set_window_size(1900,1080)
    priceObject = './/*//div[contains(@class,"pd-transactions")]/div[1]/*[contains(@class,"pd-prices-current-price")]'
    aemText = driver.find_element_by_xpath(priceObject).text
    newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR]','',aemText)
    remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
    btn = driver.find_element_by_xpath('//*//div[contains(@class,"pd-transactions-button")]/a')
    check_trfid = btn.get_attribute("href")
    if 'trf_id=nortoncom' not in check_trfid:
        print ("trfid is missing")         
    else:
        print "trfid is present in the buy link"
    btn.click()
    time.sleep(5)
    if "checkOut" in driver.current_url:
        item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, './/*[contains(@id,"OverlayPrice")]/span')))
        estoreText = driver.find_element_by_xpath('.//*[contains(@id,"OverlayPrice")]/span').text
        newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,MYR]','',estoreText)
        #print newEstoreText
        remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
        print "AEM price "+remAemEro
        print "estore price  "+remEstoreEro
        
        if remAemEro ==remEstoreEro:
            report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
            report.write(report_string)
            report = open("result.html","a")
            
        else:
            print 'price is not match'  
            report_string = '<tr><td>'+ str(url) +'</td><td><center><font color="red">FAIL</center></font></td>'        
            report.write(report_string)
            report = open("result.html","a")
        driver.delete_all_cookies()
    else:
        item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
        estoreText = driver.find_element_by_xpath('//table[@class="cart-table"]/tbody/tr[2]/td[4]').text
        print estoreText
        newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR]','',estoreText)
        print newEstoreText
        remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
        print remEstoreEro
        
        if remAemEro ==remEstoreEro:
            report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
            report.write(report_string)
            report = open("result.html","a")
        else:
            print 'price is not match'  
            report_string = '<tr><td>'+ str(url) +'</td><td><center><font color="red">FAIL</center></font></td>'        
            report.write(report_string)
            report = open("result.html","a")
        driver.delete_all_cookies()
        
   
    if count == 1:
        print "price verify for 2 years subscription"
        driver.get(url) 
        driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[2]').click()
        time.sleep(1)
        
        aemText = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[2]/*[contains(@class,"pd-prices-current-price")]').text
        newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR]','',aemText)
        remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
        btn = driver.find_element_by_xpath('//div[@class="pd-transactions"]/div[2]/div/a')
        btn.click()
        time.sleep(5)
        if "checkOut" in driver.current_url:
            item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, './/*[contains(@id,"OverlayPrice")]/span')))
            estoreText = driver.find_element_by_xpath('.//*[contains(@id,"OverlayPrice")]/span').text
            #print estoreText
            newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,MYR]','',estoreText)
            #print newEstoreText
            remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            #print remEstoreEro
            print "AEM price "+remAemEro
            print "estore price  "+remEstoreEro
            if remAemEro==remEstoreEro:
                report_string = '<td><center><font color="green">PASS</font></center></td><td><center>-</center></td>'       
                report.write(report_string)
                report = open("result.html","a")
            else:
                print 'price is not match'
                report_string = "<td><center><font color='red'>FAIL</font></center></td><td><center>-</center></td>"        
                report.write(report_string)
                report = open("result.html","a")
            driver.delete_all_cookies()
            count = 0
            
        else:
            item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
            estoreText = driver.find_element_by_xpath('//table[@class="cart-table"]/tbody/tr[2]/td[4]').text
            print estoreText
            newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR]','',estoreText)
            print newEstoreText
            remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            print remEstoreEro
            if remAemEro==remEstoreEro:
                report_string = '<td><center><font color="green">PASS</font></center></td>'       
                report.write(report_string)
                report = open("result.html","a")
            else:
                print 'price is not match'
                report_string = "<td><center><font color='red'>FAIL</font></center></td>"        
                report.write(report_string)
                report = open("result.html","a")
            driver.delete_all_cookies()
            count = 0
    
    if count2 == 1:
        print 'price verify for 3 year subscription'
        driver.get(url) 
        driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[3]').click()
        time.sleep(1)
        
        aemText = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[3]/*[contains(@class,"pd-prices-current-price")]').text
        print aemText
        newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR]','',aemText)
        print newAemText
        remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
        print remAemEro
        btn = driver.find_element_by_xpath('//div[@class="pd-transactions"]/div[3]/div/a')
        btn.click()
        time.sleep(5)
        
        if "checkOut" in driver.current_url:
            item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, './/*[contains(@id,"OverlayPrice")]/span')))
            estoreText = driver.find_element_by_xpath('.//*[contains(@id,"OverlayPrice")]/span').text
            #print estoreText
            newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK]','',estoreText)
            print newEstoreText
            remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            print remEstoreEro
            if remAemEro==remEstoreEro:
                report_string = '<td><center><font color="green">PASS</font></center></td>'       
                report.write(report_string)
                report = open("result.html","a")
            else:
                print 'price is not match'
                report_string = "<td><center><font color='red'>FAIL</font></center></td>"        
                report.write(report_string)
                report = open("result.html","a")
            driver.delete_all_cookies()
            count2 = 0
        else:
            item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
            estoreText = driver.find_element_by_xpath('//table[@class="cart-table"]/tbody/tr[2]/td[4]').text
            print estoreText
            newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR]','',estoreText)
            print newEstoreText
            remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            print remEstoreEro
            if remAemEro==remEstoreEro:
                report_string = '<td><center><font color="green">PASS</font></center></td>'       
                report.write(report_string)
                report = open("result.html","a")
            else:
                print 'price is not match'
                report_string = "<td><center><font color='red'>FAIL</font></center></td>"        
                report.write(report_string)
                report = open("result.html","a")
            driver.delete_all_cookies()
            count2 = 0
        report.write("</tr>")
    else:
        
        pass
        count = 0
        count2 = 0

    
    driver.close()
f.close()

   
    
            
            

    