
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import csv
import getpass
import selenium.webdriver.support.ui as ui
# import urlparse

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

lists = ["mortgage","homeloan","mortgage broker","Loan Calculator"]

for i in lists:
    driver.get("https://www.google.com/search?q="+i+"&num=20&start=0&sourceid=chrome&ie=UTF-8")
    time.sleep(5)
    # result_list = driver.find_element_by_class_name('yuRUbf').get_attribute('href')
    result_list = driver.find_elements_by_xpath("//a[@class='yuRUbf']")
    print(result_list)
    # result_list = driver.find_element_by_tag_name('a').get_attribute('href')
    for tag in result_list:
        tag.click()
        time.sleep(1)
        print(tag.get_attribute('href'))
    # print(result_list)
    # print(urlparse.parse_qs(urlparse.urlparse(result_list).query)["q"])
    # with open('Website_list.txt','w') as f:
    #     for item in result_list:
    #         f.write("%s\n" % item)

