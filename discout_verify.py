# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2017

@author: felix_brodskiy
'''
import unittest,sys,time,re
import  ConfigParser
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException
import datetime
import logging,re

def percentage(part, whole):
    return 100 * float(part)/float(whole)
def saleprice(strike,price):
    return float(strike)-float(price)
def country_popup():
    try:
        if driver.find_element_by_xpath('//*//div[@class="choose-language-container"]').is_displayed():
            country_popup = 1
            print "found pop up"
        else:
            country_popup = 2
        time.sleep(2)
        if country_popup ==1:
            print "closing"
            driver.find_element_by_xpath('.//*[@id="language-selector"]//button').click()
            time.sleep(2)
            #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE)

    except:
        country_popup=2
        pass
    
def cleanPrice(price):
    non_decimal = re.compile(r'[^\d]+')
    cleanPrice = non_decimal.sub('',price)
    print cleanPrice
    return cleanPrice

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
main_list = emea_list+namlam_list+apj_list


url_lst= ['https://us.norton.com/norton-security-antivirus','https://br.norton.com/norton-security-for-one-device','https://malaysia.norton.com/norton-security-for-one-device']
report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","w")
report.write('<html><body><h1>This Report Generated On: '+str(datetime.datetime.today())+'</h1><table border ="1"><tr><th>URL</th><th>One Year Entitlement</th><th>Two Year Entitlement</th><th>Three Year Entitlement</th></tr>')
for url in main_list:
    try:
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(2)
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
        ent_flags= driver.find_elements_by_xpath('.//*//div[contains(@class,"pd-transactions")]/ul/li')
        print len(ent_flags)
        try:
            whole_string = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[1]/*[contains(@class,"pd-prices-old")]').text
#             whole =''.join(filter(lambda character:ord(character) < 00165,whole_string))
#             whole = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',whole)
            whole = cleanPrice(whole_string)
        except:
            print "there is not discount"
            pass
        discount_price = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[1]/*[contains(@class,"pd-prices-current-price")]').text
#         discount = ''.join(filter(lambda character:ord(character) < 00165,discount_price))
#         discount = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',discount)
        discount = cleanPrice(discount_price)
        print whole,discount
        #delta = float(whole) -float(discount)
        #print delta
        #newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
        whole = re.sub(',','.',whole)
        discount = re.sub(',','.',discount)
        print whole,discount 
        
        whole = float(whole)
        discount = float(discount)
        delta = whole - discount
        
        # print delta
        # procentage = (delta/whole)*100
        # print procentage
        try:
            saving_flag = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[1]/*[contains(@class,"pd-prices-savings")]').text
            if '%' in saving_flag:
                save = percentage(delta,whole)
                print save
                print saving_flag
                save = int(save)
                #save = int(save)
                print save
                if str(save) in saving_flag:
                    print "pass"
                    report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                else:
                    print "fail"
                    report_string = '<tr><td>'+ str(url) +'</td><td><center><font color="red">FAIL</center></font></td>'        
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
            else: 
                save = saleprice(whole,discount)
                print save
                print saving_flag
                save = str(save)
                save = save.rstrip('0').rstrip('.').rstrip('0')
                print save
                if save in saving_flag:
                    print "pass"
                    report_string = "<tr><td>" + str(url) + "</td><td><center><font color='green'>PASS</center></font></td>" 
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                else:
                    print "fail"
                    report_string = '<tr><td>'+ str(url) +'</td><td><center><font color="red">FAIL</center></font></td>'        
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
        except:
            print "there is not discount flags"
            report_string = "<tr><td>" + str(url) + "</td></td><td><center>-</center></td>"
            report.write(report_string)
            report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a") 
            pass
        if count==1:
            time.sleep(1)
            driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[2]').click()
            time.sleep(2)
            try:
                whole_string = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[2]/*[contains(@class,"pd-prices-old")]').text
#                 whole =''.join(filter(lambda character:ord(character) < 00165,whole_string))
#                 whole = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',whole)
                whole = cleanPrice(whole_string)
            except:
                print "there is no discount"
                pass
            discount_price = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[2]/*[contains(@class,"pd-prices-current-price")]').text
#             discount = ''.join(filter(lambda character:ord(character) < 00165,discount_price))
#             discount = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',discount)
            discount = cleanPrice(discount_price)
            print whole,discount
            #delta = float(whole) -float(discount)
            #print delta
            #newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
            whole = re.sub(',','.',whole)
            discount = re.sub(',','.',discount)
            print whole,discount 
            
            whole = float(whole)
            discount = float(discount)
            delta = whole - discount
            
            # print delta
            # procentage = (delta/whole)*100
            # print procentage
            try:
                saving_flag = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[2]/*[contains(@class,"pd-prices-savings")]').text
                if '%' in saving_flag:
                    save = percentage(delta,whole)
                    print save
                    print saving_flag
                    save = int(save)
                    save = int(save)
                    print save
                    if str(save) in saving_flag:
                        print "pass"
                        report_string = "</td><td><center><font color='green'>PASS</center></font></td>" 
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                    else:
                        print "fail"
                        report_string = '</td><td><center><font color="red">FAIL</center></font></td>'        
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                else: 
                    save = saleprice(whole,discount)
                    print save
                    print saving_flag
                    save = str(save)
                    save = save.rstrip('0').rstrip('.').rstrip('0')
                    print save
                    if save in saving_flag:
                        print "pass"
                        report_string = "</td><td><center><font color='green'>PASS</center></font></td>" 
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                    else:
                        print "fail"
                        report_string = '</td><td><center><font color="red">FAIL</center></font></td>'        
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
            except:
                print "there is not discount flags"
                report_string = "</td><td><center>-</center></td>"
                report.write(report_string)
                report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a") 
                pass
            count = 0
        if count2==1:
            driver.find_element_by_xpath('//div[@class="pd-transactions"]/ul/li[3]').click()
            time.sleep(2)
            try:
                whole_string = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[3]/*[contains(@class,"pd-prices-old")]').text
#                 whole =''.join(filter(lambda character:ord(character) < 00165,whole_string))
#                 whole = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',whole)
                whole = cleanPrice(whole_string)
            except:
                print "there is no discount"
                pass
            discount_price = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[3]/*[contains(@class,"pd-prices-current-price")]').text
#             discount = ''.join(filter(lambda character:ord(character) < 00165,discount_price))
#             discount = re.sub('[ ,$,USD,€,*,SFr,kr,EUR,NOK,SEK,€,RMB,MYR,CP,Ch,円(税抜)]','',discount)
            discount = cleanPrice(discount_price)
            print whole,discount
            #delta = float(whole) -float(discount)
            #print delta
            #newEstoreText = re.sub('[ ,$,.,USD,€,*,SFr.,,,.,kr,00,EUR,NOK,SEK,元,MYR,￥]','',estoreText)
            whole = re.sub(',','.',whole)
            discount = re.sub(',','.',discount)
            print whole,discount 
            
            whole = float(whole)
            discount = float(discount)
            delta = whole - discount
            
            # print delta
            # procentage = (delta/whole)*100
            # print procentage
            try:
                saving_flag = driver.find_element_by_xpath('.//*//div[contains(@class,"pd-transactions")]/div[3]/*[contains(@class,"pd-prices-savings")]').text
                if '%' in saving_flag:
                    save = percentage(delta,whole)
                    print save
                    print saving_flag
                    save = int(save)
                    save = int(save)
                    print save
                    if str(save) in saving_flag:
                        print "pass"
                    else:
                        print "fail"
                else: 
                    save = saleprice(whole,discount)
                    print save
                    print saving_flag
                    save = str(save)
                    save = save.rstrip('0').rstrip('.').rstrip('0')
                    print save
                    if save in saving_flag:
                        print "pass"
                        report_string = "</td><td><center><font color='green'>PASS</center></font></td>" 
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
                    else:
                        print "fail"
                        report_string = '</td><td><center><font color="red">FAIL</center></font></td>'        
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a")
            except:
                print "there is no discount flags"
                report_string = "</td><td><center>-</center></td>"
                report.write(report_string)
                report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a") 
                pass
            count2=0
        report.write("</tr>")
        driver.close()
    except Exception, e:
            print url+": there are no discounts for this page url"
            report_string = "<tr><td>" + str(url) + "</td></td><td><center>-</center></td>"
            report.write(report_string)
            report = open("/Users/felix_brodskiy/eclipse/CQ5 project/tnt_scripts/discount_report.html","a") 
            print e
            driver.quit()
    