# -*- coding: utf-8 -*-
import unittest,sys,time,re
import  ConfigParser
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException
import datetime
import logging

logging.basicConfig(filename="trfid_info.log",level = logging.INFO, filemode="w")
region = sys.argv[1]
main_list = []
emea_list= [
'http://pl.norton.com/norton-security-for-one-device',
'http://pl.norton.com/norton-security-antivirus',
'http://pl.norton.com/norton-security-with-backup',
'https://pl.norton.com/norton-mobile-security',
            
'https://at.norton.com/norton-mobile-security',            
'http://at.norton.com/norton-security-for-one-device',
'http://at.norton.com/norton-security-antivirus',
'http://at.norton.com/norton-security-with-backup',

'https://be.norton.com/norton-mobile-security',
'http://be.norton.com/norton-security-for-one-device',
'http://be.norton.com/norton-security-antivirus',
'http://be.norton.com/norton-security-with-backup',

'http://be-nl.norton.com/norton-security-for-one-device',
'http://be-nl.norton.com/norton-security-antivirus',
'http://be-nl.norton.com/norton-security-with-backup',
'https://be-nl.norton.com/norton-mobile-security',

'http://gr.norton.com/norton-security-for-one-device',
'http://gr.norton.com/norton-security-antivirus',
'http://gr.norton.com/norton-security-with-backup',
'https://gr.norton.com/norton-mobile-security',

'http://cz.norton.com/norton-security-for-one-device',
'http://cz.norton.com/norton-security-antivirus',
'http://cz.norton.com/norton-security-with-backup',
'https://cz.norton.com/norton-mobile-security',

'http://dk.norton.com/norton-security-for-one-device',
'http://dk.norton.com/norton-security-antivirus',
'http://dk.norton.com/norton-security-with-backup',
'https://dk.norton.com/norton-mobile-security',

'http://fi.norton.com/norton-security-for-one-device',
'http://fi.norton.com/norton-security-antivirus',
'http://fi.norton.com/norton-security-with-backup',
'https://fi.norton.com/norton-mobile-security',

'http://fr.norton.com/norton-security-for-one-device',
'http://fr.norton.com/norton-security-antivirus',
'http://fr.norton.com/norton-security-with-backup',
'https://fr.norton.com/norton-mobile-security',
'https://fr.norton.com/norton-antivirus',

'http://de.norton.com/norton-security-for-one-device',
'http://de.norton.com/norton-security-antivirus',
'http://de.norton.com/norton-security-with-backup',
'https://de.norton.com/norton-mobile-security',
'https://de.norton.com/norton-antivirus',

'http://hu.norton.com/norton-security-for-one-device',
'http://hu.norton.com/norton-security-antivirus',
'http://hu.norton.com/norton-security-with-backup',
'https://hu.norton.com/norton-mobile-security',

'http://ie.norton.com/norton-security-for-one-device',
'http://ie.norton.com/norton-security-antivirus',
'http://ie.norton.com/norton-security-with-backup',
'https://ie.norton.com/norton-mobile-security',

'http://il.norton.com/norton-security-for-one-device',
'http://il.norton.com/norton-security-antivirus',
'http://il.norton.com/norton-security-with-backup',
'https://il.norton.com/norton-mobile-security',

'http://it.norton.com/norton-security-for-one-device',
'http://it.norton.com/norton-security-antivirus',
'http://it.norton.com/norton-security-with-backup',
'https://it.norton.com/norton-mobile-security',
'https://it.norton.com/norton-antivirus',

'http://nl.norton.com/norton-security-for-one-device',
'http://nl.norton.com/norton-security-antivirus',
'http://nl.norton.com/norton-security-with-backup',
'https://nl.norton.com/norton-mobile-security',

'http://no.norton.com/norton-security-for-one-device',
'http://no.norton.com/norton-security-antivirus',
'http://no.norton.com/norton-security-with-backup',
'https://no.norton.com/norton-mobile-security',



'http://pt.norton.com/norton-security-for-one-device',
'http://pt.norton.com/norton-security-antivirus',
'http://pt.norton.com/norton-security-with-backup',
'https://pt.norton.com/norton-mobile-security',

'http://ro.norton.com/norton-security-for-one-device',
'http://ro.norton.com/norton-security-antivirus',
'http://ro.norton.com/norton-security-with-backup',
'https://ro.norton.com/norton-mobile-security',

'http://ru.norton.com/norton-security-for-one-device',
'http://ru.norton.com/norton-security-antivirus',
'http://ru.norton.com/norton-security-with-backup',
'https://ru.norton.com/norton-mobile-security',

'http://za.norton.com/norton-security-for-one-device',
'http://za.norton.com/norton-security-antivirus',
'http://za.norton.com/norton-security-with-backup',
'https://za.norton.com/norton-mobile-security',

'http://es.norton.com/norton-security-for-one-device',
'http://es.norton.com/norton-security-antivirus',
'http://es.norton.com/norton-security-with-backup',
'https://es.norton.com/norton-mobile-security',
'https://es.norton.com/norton-antivirus',

'http://se.norton.com/norton-security-for-one-device',
'http://se.norton.com/norton-security-antivirus',
'http://se.norton.com/norton-security-with-backup',
'https://se.norton.com/norton-mobile-security',

'http://ch.norton.com/norton-security-for-one-device',
'http://ch.norton.com/norton-security-antivirus',
'http://ch.norton.com/norton-security-with-backup',
'https://ch.norton.com/norton-mobile-security',

'http://ch-it.norton.com/norton-security-for-one-device',
'http://ch-it.norton.com/norton-security-antivirus',
'http://ch-it.norton.com/norton-security-with-backup',
'https://ch-it.norton.com/norton-mobile-security',

'http://ch-fr.norton.com/norton-security-for-one-device',
'http://ch-fr.norton.com/norton-security-antivirus',
'http://ch-fr.norton.com/norton-security-with-backup',
'https://ch-fr.norton.com/norton-mobile-security',

'http://tr.norton.com/norton-security-for-one-device',
'http://tr.norton.com/norton-security-antivirus',
'http://tr.norton.com/norton-security-with-backup',
'https://tr.norton.com/norton-mobile-security',

'http://ae.norton.com/norton-security-for-one-device',
'http://ae.norton.com/norton-security-antivirus',
'http://ae.norton.com/norton-security-with-backup',
'https://ae.norton.com/norton-mobile-security',

'http://uk.norton.com/norton-security-for-one-device',
'http://uk.norton.com/norton-security-antivirus',
'http://uk.norton.com/norton-security-with-backup',
'https://uk.norton.com/norton-mobile-security',
'https://uk.norton.com/norton-antivirus'
]


namlam_list = [
'http://ca.norton.com/norton-security-for-one-device',
'https://us.norton.com/norton-mobile-security',               
'https://us.norton.com/core-secure-router-select',               
'http://us.norton.com/norton-security-for-one-device',
'http://us.norton.com/norton-security-antivirus',
'http://us.norton.com/norton-security-with-backup',
'https://us.norton.com/norton-antivirus',

'http://ca.norton.com/norton-security-for-one-device',
'http://ca.norton.com/norton-security-antivirus',
'http://ca.norton.com/norton-security-with-backup',
'https://ca.norton.com/norton-antivirus',
'https://ca.norton.com/norton-mobile-security',

'http://ca-fr.norton.com/norton-security-for-one-device',
'http://ca-fr.norton.com/norton-security-antivirus',
'http://ca-fr.norton.com/norton-security-with-backup',
'https://ca-fr.norton.com/norton-antivirus',
'https://ca-fr.norton.com/norton-mobile-security',

'http://pr.norton.com/norton-security-for-one-device',
'http://pr.norton.com/norton-security-antivirus',
'http://pr.norton.com/norton-security-with-backup',
'https://pr.norton.com/norton-mobile-security',


'http://lam.norton.com/norton-security-for-one-device',
'http://lam.norton.com/norton-security-antivirus',
'http://lam.norton.com/norton-security-with-backup',
'https://lam.norton.com/norton-mobile-security',

'http://ar.norton.com/norton-security-for-one-device',
'http://ar.norton.com/norton-security-antivirus',
'http://ar.norton.com/norton-security-with-backup',
'https://ar.norton.com/norton-mobile-security',

'http://br.norton.com/norton-security-for-one-device',
'http://br.norton.com/norton-security-antivirus',
'http://br.norton.com/norton-security-with-backup',
'https://br.norton.com/norton-mobile-security',

'http://cl.norton.com/norton-security-for-one-device',
'http://cl.norton.com/norton-security-antivirus',
'http://cl.norton.com/norton-security-with-backup',
'https://cl.norton.com/norton-mobile-security',

'http://co.norton.com/norton-security-for-one-device',
'http://co.norton.com/norton-security-antivirus',
'http://co.norton.com/norton-security-with-backup',
'https://co.norton.com/norton-mobile-security',

'http://mx.norton.com/norton-security-for-one-device',
'http://mx.norton.com/norton-security-antivirus',
'http://mx.norton.com/norton-security-with-backup',
'https://mx.norton.com/norton-mobile-security'               
]

apj_list = [
'http://in.norton.com/norton-security-with-backup',
'https://jp.norton.com/norton-antivirus',
'http://au.norton.com/norton-security-for-one-device',
'http://au.norton.com/norton-security-for-three-devices',
'http://au.norton.com/norton-security-antivirus',
'https://au.norton.com/norton-mobile-security',
'https://au.norton.com/norton-antivirus',

'http://malaysia.norton.com/norton-security-for-one-device',
'http://malaysia.norton.com/norton-security-with-backup',
'http://malaysia.norton.com/norton-security-antivirus',
'https://malaysia.norton.com/norton-mobile-security',
'https://malaysia.norton.com/norton-antivirus',


'http://cn.norton.com/norton-security-for-one-device',
'http://cn.norton.com/norton-security-for-three-devices',
'http://cn.norton.com/norton-security-antivirus',
'https://cn.norton.com/norton-mobile-security',
'https://cn.norton.com/norton-antivirus',

'http://jp.norton.com/norton-security-for-one-device',
'http://jp.norton.com/norton-security-for-three-devices',
'http://jp.norton.com/norton-security-antivirus',
'https://jp.norton.com/norton-mobile-security',


'http://hk-en.norton.com/norton-security-for-one-device',
'http://hk-en.norton.com/norton-security-for-three-devices',
'http://hk-en.norton.com/norton-security-antivirus',
'https://hk-en.norton.com/norton-mobile-security',
'https://hk-en.norton.com/norton-antivirus',

'http://hk.norton.com/norton-security-for-one-device',
'http://hk.norton.com/norton-security-for-three-devices',
'http://hk.norton.com/norton-security-antivirus',
'https://hk.norton.com/norton-mobile-security',
'https://hk.norton.com/norton-antivirus',

'http://in.norton.com/norton-security-for-one-device',
'http://in.norton.com/norton-security-with-backup',
'http://in.norton.com/norton-security-antivirus',
'https://in.norton.com/norton-mobile-security',
'https://in.norton.com/norton-antivirus',

'http://kr.norton.com/norton-security-for-one-device',
'http://kr.norton.com/norton-security-for-three-devices',
'http://kr.norton.com/norton-security-antivirus',
'https://kr.norton.com/norton-mobile-security',
'https://kr.norton.com/norton-antivirus',

'http://nz.norton.com/norton-security-for-one-device',
'http://nz.norton.com/norton-security-for-three-devices',
'http://nz.norton.com/norton-security-antivirus',
'https://nz.norton.com/norton-mobile-security',
'https://nz.norton.com/norton-antivirus',

'http://sg.norton.com/norton-security-for-one-device',
'http://sg.norton.com/norton-security-with-backup',
'http://sg.norton.com/norton-security-antivirus',
'https://sg.norton.com/norton-mobile-security',
'https://sg.norton.com/norton-antivirus',

'http://tw.norton.com/norton-security-for-one-device',
'http://tw.norton.com/norton-security-for-three-devices',
'http://tw.norton.com/norton-security-antivirus',
'https://tw.norton.com/norton-mobile-security',
'https://tw.norton.com/norton-antivirus'         
]

def country_popup():
    try:
        if driver.find_element_by_xpath('//*//div[@class="choose-language-container"]').is_displayed():
            country_popup = 1
            print "found pop up"
        else:
            country_popup = 2
        time.sleep(3)
        if country_popup ==1:
            print "closing"
            driver.find_element_by_xpath('.//*[@id="language-selector"]//button').click()
            #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE)

    except:
        country_popup=2
        pass
    
def cleanPrice(price):
    non_decimal = re.compile(r'[^\d]+')
    cleanPrice = non_decimal.sub('',price)
    print cleanPrice
    return cleanPrice
       
        
report = open("result.html","w")
report.write('<html><body><h1>This Report Generated On: '+str(datetime.datetime.today())+'</h1><a href="trfid_info.log">Here is link to trf_id info file</a><table border ="1"><tr><th>URL</th><th>One Year Entitlement</th><th>Two Year Entitlement</th><th>Three Year Entitlement</th></tr>')
if region == "emea":
    main_list = emea_list
elif region == "namlam":
    main_list = namlam_list
elif region == "apj":
    main_list = apj_list
else:
    main_list = emea_list+namlam_list+apj_list
   
for url in main_list:
    try:
        print "################################################################################################################"
        print url
        driver = webdriver.Firefox()
        #driver.maximize_window()
        
        
        
        #driver = webdriver.Remote(command_executor='http://10.149.226.43:7000/wd/hub' ,desired_capabilities =webdriver.DesiredCapabilities.FIREFOX)# {"browserName": "IE","platform": "WINDOWS"})
        driver.get(url)        
        driver.set_window_size(1800, 1080)
        
        country_popup()
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
        #driver.set_window_size(1900,1080)
        priceObject = './/*//div[contains(@class,"pd-transactions")]/div[1]/*[contains(@class,"pd-prices-current-price")]'
#         element = driver.find_element_by_xpath('//*//li[contains(@class,"navbar-item dropdown")][1]/a')
#         action = webdriver.ActionChains(driver)
#         action.move_to_element(element)
#         action.perform()
        aemText = driver.find_element_by_xpath(priceObject).text
#         newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',aemText)
#         remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
        aemClean = cleanPrice(aemText)
        btn = driver.find_element_by_xpath('//*//div[contains(@class,"pd-transactions-button")]/a')
        check_trfid = btn.get_attribute("href")
        if 'trf_id=nortoncom' not in check_trfid:
            print ("trfid is missing")
            logging.info("trfid is missing in buy link: "+ check_trfid)         
        else:
            print "trfid is present in the buy link"
            logging.info("trfid is present in buy link: " + check_trfid)
        btn.click()
        time.sleep(5)
        try:
            if driver.find_element_by_xpath('//*//div[contains(@class,"entitlement-cta-display")]/a').is_displayed():
                popup = 1
            else:
                popup = 2
        except:
            popup=2
            pass
        if popup == 1:
                driver.find_element_by_xpath('//*//div[contains(@class,"entitlement-cta-display")]/a').click()
                time.sleep(5)
        if "checkOut" in driver.current_url:
            item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//span[contains(@id,"OverlayPrice")]')))
            estoreText = driver.find_element_by_xpath('//*//span[contains(@id,"OverlayPrice")]').text
#             newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,MYR,CP,Ch]','',estoreText)
#             remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            cleanEstore = cleanPrice(estoreText)
            print "AEM price "+aemClean
            print "estore price  "+cleanEstore
            
            if aemClean ==cleanEstore:
                report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
                report.write(report_string)
                report = open("result.html","a")
                
            else:
                print 'price is not match'  
                report_string = '<tr><td><a href='+ str(url) +'>'+str(url)+'</a></td><td><center><font color="red">FAIL</center></font></td>'        
                report.write(report_string)
                report = open("result.html","a")
                logging.info("AEM price "+aemClean+" estore price  "+cleanEstore)
            popup=0
            driver.delete_all_cookies()
        else:
            if "jp" not in url:
                item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
            else:
                item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//div[contains(@class,"cart")]//tbody/tr[2]/td[3]')))
            estoreText = item.text
            print estoreText
            cleanEstore = cleanPrice(estoreText)
#             newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
#             print newEstoreText
#             remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
            print cleanEstore
            
            if aemClean ==cleanEstore:
                report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
                report.write(report_string)
                report = open("result.html","a")
            else:
                print 'price is not match'  
                report_string = '<tr><td><a href='+ str(url) +'>'+str(url)+'</a></td><td><center><font color="red">FAIL</center></font></td>'        
                report.write(report_string)
                report = open("result.html","a")
                logging.info(url +" AEM price "+aemClean+" estore price  "+cleanEstore)
            driver.delete_all_cookies()
    
            
       
        if count == 1:
            print "price verify for 2 years subscription"
            driver.get(url)
            country_popup() 
            time.sleep(3)
            driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[2]').click()
            time.sleep(2)
            
            aemText = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[2]/*[contains(@class,"pd-prices-current-price")]').text
#             newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',aemText)
#             remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
            cleanAem =cleanPrice(aemText)
            btn = driver.find_element_by_xpath('//div[@class="pd-transactions"]/div[2]/div/a')
            check_trfid2 = btn.get_attribute("href")
            if 'trf_id=nortoncom' not in check_trfid2:
                print ("trfid is missing")
                logging.info("trfid is missing in buy link: "+ check_trfid2)         
            else:
                print "trfid is present in the buy link"
                logging.info("trfid is present in buy link: "+ check_trfid2)
            btn.click()
            time.sleep(3)
            
            try:
                if driver.find_element_by_xpath('//*//div[contains(@class,"entitlement-cta-display")]/a').is_displayed():
                    popup = 1
                else:
                    popup = 2
            except:
                popup=2
                pass
            if popup == 1:
                    driver.find_element_by_xpath('//*//div[contains(@class,"entitlement-cta-display")]/a').click()
                    time.sleep(5)
            
            if "checkOut" in driver.current_url:
                item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//span[contains(@id,"OverlayPrice")]')))
                estoreText = driver.find_element_by_xpath('//*//span[contains(@id,"OverlayPrice")]').text

                cleanEstore = cleanPrice(estoreText)
                print "AEM price "+cleanAem
                print "estore price  "+cleanEstore
                if cleanAem==cleanEstore:
                    if "in" in url or "sg" in url or "malaysia" in url:
                        report_string = '<td><center><font color="green">PASS</font></center></td>'       
                        report.write(report_string)
                        report = open("result.html","a")
                    else:
                        report_string = '<td><center><font color="green">PASS</font></center></td><td><center>-</center></td>'       
                        report.write(report_string)
                        report = open("result.html","a")
                else:
                    if "in" in url or "sg" in url or "malaysia" in url:
                        print 'price is not match'
                        report_string = "<td><center><font color='red'>FAIL</font></center></td>"        
                        report.write(report_string)
                        report = open("result.html","a")
                        logging.info("AEM price "+cleanAem+" estore price  "+cleanEstore)
                    else:
                        print 'price is not match'
                        report_string = "<td><center><font color='red'>FAIL</font></center></td><td><center>-</center></td>"        
                        report.write(report_string)
                        report = open("result.html","a")
                        logging.info("AEM price "+cleanAem+" estore price  "+cleanEstore)
                driver.delete_all_cookies()
                count = 0
                popup=0
            else:
                if "jp" not in url:
                    item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
                else:
                    item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//div[contains(@class,"cart")]//tbody/tr[2]/td[3]')))
                estoreText = item.text

#                 newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
#                 print newEstoreText
#                 remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
                cleanEstore =cleanPrice(estoreText)
                print cleanAem
                print cleanEstore
                
                if cleanAem ==cleanEstore:
                    report_string = "<td><center><font color='green'>PASS</font></center></td>" 
                    report.write(report_string)
                    report = open("result.html","a")
                else:
                    print 'price is not match'  
                    report_string = '<td><center><font color="red">FAIL</font></center></td>'        
                    report.write(report_string)
                    report = open("result.html","a")
                    logging.info("AEM price "+cleanAem+" estore price  "+cleanEstore)
                driver.delete_all_cookies()
            
                
            
        
        if count2 == 1:
            print 'price verify for 3 year subscription'
            driver.get(url)
            country_popup()
            time.sleep(3)
            driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[3]').click()
            time.sleep(2)
            
            aemText = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[3]/*[contains(@class,"pd-prices-current-price")]').text
#             print aemText
#             newAemText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,€,RMB,MYR,円(税抜)]','',aemText)
#             print newAemText
#             remAemEro = ''.join(filter(lambda character:ord(character) < 00165,newAemText))
            cleanAem = cleanPrice(aemText)
            print cleanAem
            btn = driver.find_element_by_xpath('//div[@class="pd-transactions"]/div[3]/div/a')
            btn.click()
            time.sleep(3)
            
            if "checkOut" in driver.current_url:
                item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//span[contains(@id,"OverlayPrice")]')))
                estoreText = driver.find_element_by_xpath('//*//span[contains(@id,"OverlayPrice")]').text
                #print estoreText
#                 newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,CP,MYR]','',estoreText)
#                 print newEstoreText
#                 remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
#                 print remEstoreEro
#                 remEstoreEro= re.sub('aleice:', '',remEstoreEro)
                cleanEstore=cleanPrice(estoreText)
                print cleanEstore
                if cleanAem==cleanEstore:
                    report_string = '<td><center><font color="green">PASS</font></center></td>'       
                    report.write(report_string)
                    report = open("result.html","a")
                else:
                    print 'price is not match'
                    report_string = "<td><center><font color='red'>FAIL</font></center></td>"        
                    report.write(report_string)
                    report = open("result.html","a")
                    logging.info(url+" AEM price "+cleanAem+" estore price  "+cleanEstore)
                driver.delete_all_cookies()
                count2 = 0
            else:
                if "jp" not in url:
                    item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//table[@class="cart-table"]/tbody/tr[2]/td[4]')))
                else:
                    item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*//div[contains(@class,"cart")]//tbody/tr[2]/td[3]')))
                estoreText = item.text
#                 print estoreText
#                 newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
#                 print newEstoreText
#                 remEstoreEro = ''.join(filter(lambda character:ord(character) < 00165,newEstoreText))
                cleanEstore = cleanPrice(estoreText)
                print cleanEstore
                
                if cleanAem ==cleanEstore:
                    report_string = '<td><center><font color="green">PASS</font></center></td>' 
                    report.write(report_string)
                    report = open("result.html","a")
                else:
                    print 'price is not match'  
                    report_string = '<td><center><font color="red">FAIL</center></font></td>'        
                    report.write(report_string)
                    report = open("result.html","a")
                    logging.info("AEM price "+cleanAem+" estore price  "+cleanEstore)
                driver.delete_all_cookies()
           
            report.write("</tr>")
        else:
            
            pass
            count = 0
            count2 = 0
    
       
        driver.close()
    except Exception, e:
        print url+": error while running test"
        print e
        driver.quit()
       
    
            
            

    