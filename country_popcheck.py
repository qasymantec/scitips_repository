'''
Created on Jul 31, 2017

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


def country_popup(driver):
    try:
        if driver.find_element_by_xpath('//*//div[@class="choose-language-container"]').is_displayed():
            return True
    except:
        print "there is no pop up"
        
def verify_href():
    lst_href =[]
    lst_elem = driver.find_elements_by_xpath('//*//div[@class="choose-language-options"]/p/a')
    for i in lst_elem:
        lst_href.append(i.get_attribute('href'))
    return lst_href 
#         if page in i.get_attribute('href'):
#             print "proper page in href"
#         else:
#             print "pointing to wrong page"
        
    
    
langList = ['BE','BE-NL','CA','CA-FR','HK','HK-EN','CH','CH-FR','CH-IT']
pageList = ['norton.com','products','norton-security-for-one-device','norton-security-antivirus','HK norton-security-with-backup','downloads', 'norton-family-premier', 'norton-mobile-security']

report = open("/Users/felix_brodskiy/eclipse/CQ5 project/new_scripts/countrypop_report.html","w")
report.write('<html><body><h1>This Report Generated On: '+str(datetime.datetime.today())+'</h1><table border ="1"><tr><th>country,page</th><th>Country Pop Up Pass/Fail</th><th>Href to Correct page Pass/Fail</th></tr>')
  
for i in langList:
    for y in pageList:
        if 'HK' in i and 'norton-family-premier' in y or 'HK norton-security-with-backup' in y:
            pass
        else:
            try:
                driver = webdriver.Firefox()
                print i,y
                driver.get('https://'+i+'.norton.com/'+y)
                time.sleep(1)
                print len(verify_href())
                for x in range(len(verify_href())):
                    print verify_href()[x]
                    if y in verify_href()[x]:
                        print y +" found in "+verify_href()[x]
                        report_string = "<tr><td>" + str(i)+" "+str(y) + "</td><td></td><td><center><font color='green'>PASS</center></font></td>" 
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/new_scripts/countrypop_report.html","a")
                    else:
                        print "page is missing in href"
                        report_string = "<tr><td>" + str(i)+" "+str(y) + "</td><td></td><td><center><font color='red'>FAIL</center></font></td>" 
                        report.write(report_string)
                        report = open("/Users/felix_brodskiy/eclipse/CQ5 project/new_scripts/countrypop_report.html","a")
                if country_popup(driver)==True:
                    print 'pass'
                    report_string = "<tr><td>" + str(i)+" "+str(y) + "</td><td><center><font color='green'>POPUP PASS</center></font></td><td></td>" 
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/new_scripts/countrypop_report.html","a")
                else:
                    print 'fail'
                    report_string = "<tr><td>" + str(i)+" "+str(y) + "</td><td><center><font color='red'>POPUP FAIL</center></font></td><td></td>" 
                    report.write(report_string)
                    report = open("/Users/felix_brodskiy/eclipse/CQ5 project/new_scripts/countrypop_report.html","a")
            except:
                print "not working"
        report.write("</tr>")
        driver.close()
driver.quit()