#keyword_crawler

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import csv
import getpass
import selenium.webdriver.support.ui as ui
import os

from webdriver_manager.chrome import ChromeDriverManager

SCROLL_PAUSE_TIME = 3.0

driver = webdriver.Chrome(ChromeDriverManager().install())

with open("Website_details.csv","w",newline="") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=['Website','Description','Keywords'])
    writer.writeheader
    
    text_file = open("result.txt","r")

    # for file in os.listdir():
    #     text_file = open(file,"r")
    lists = text_file.readlines()
    # print(lists)
    for web in lists:
        
        # print("https://"+web)
        print(web)
        driver.get(web)
        time.sleep(3.0)

        # keyword = driver.find_element_by_xpath("/html/head/meta[2]")
        try:
            keyword = driver.find_element_by_xpath("//meta[@name='Keywords']").get_attribute("content")
            print("Keyword:",keyword)
        except NoSuchElementException:
            keyword = "N\A"

        try:
            keyword = driver.find_element_by_xpath("//meta[@name='keyword']").get_attribute("content")
            print("keywords:",keyword)
        except NoSuchElementException:
            keyword = "N\A"  
        
        try:
            keyword = driver.find_element_by_xpath("//meta[@name='keywords']").get_attribute("content")
            print("keywords:",keyword)
        except NoSuchElementException:
            keyword = "N\A" 

        try:
            description = driver.find_element_by_xpath("//meta[@name='Description']").get_attribute("content")
            print("Description:",description)
        except NoSuchElementException:
            description = "N\A"

        try:
            description = driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
            print("description:",description)
        except NoSuchElementException:
            description = "N\A"

        writer.writerow({'Website':web,'Description':description,'Keywords':keyword})
        time.sleep(1.0)
    