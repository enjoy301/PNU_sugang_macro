from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def enrol():
    sub_driver = webdriver.Chrome(path, options=options)
    sub_driver.implicitly_wait(10)
    sub_driver.get("https://sugang.pusan.ac.kr/sugang/Login.aspx")
    sub_driver.find_element_by_id("txtid").send_keys("YourStudentID")
    sub_driver.find_element_by_id("txtpassword").send_keys("*********")
    sub_driver.find_element_by_id("btnlogin").click()

    sub_driver.find_element_by_id("txtCode").send_keys("CP24150")
    sub_driver.find_element_by_id("txtBunban").send_keys("060")
    sub_driver.find_element_by_id("btninsert").click()
    print(sub_driver.find_element_by_xpath('//*[@id="lbError"]').text)
    sub_driver.find_element_by_xpath('//*[@id="dgSinchungList_ctl05_txtChangeBunban"]').send_keys("061")
    sub_driver.find_element_by_xpath('//*[@id="dgSinchungList"]/tbody/tr[5]/td[13]/a').click()
    print(sub_driver.find_element_by_xpath('//*[@id="lbError"]').text)
    sub_driver.find_element_by_xpath('//*[@id="btnexit"]').click()

    sub_driver.close()


options = webdriver.ChromeOptions() 
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
path = "chromedriver.exe"

driver = webdriver.Chrome(path, options=options)
driver.implicitly_wait(10)
while True:
    try:
        driver.get("https://e-onestop.pusan.ac.kr/menu/class/C03/C03001?menuId=2000030301&rMenu=03")

        Select(driver.find_element_by_id('subject_is')).select_by_value('1')
        time.sleep(2)
        Select(driver.find_element_by_id('refinementAndMajor')).select_by_value('346712')
        driver.find_element_by_id('search').click()

        webapplication = driver.find_element_by_xpath('//*[@id="header_b"]/tr[3]/td[10]').text[:5]
        database = driver.find_element_by_xpath('//*[@id="header_b"]/tr[31]/td[10]').text[:5]

        if webapplication[:2] != webapplication[3:]:
            enrol()
        if database[:2] != database[3:]:
            enrol()
    except:
        print("bug")
        driver.close()
        driver = webdriver.Chrome(path, options=options)
        driver.implicitly_wait(10)

driver.close()
