from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class FinanceReportCsv:
    def Download(self):
        driver = webdriver.Chrome()
        driver.get("https://www.etsy.com")
        username = "huynhhong90@hotmail.de"
        password = "America90"

    
        accBtn = driver.find_element(By.CSS_SELECTOR, '.wt-btn.wt-btn--filled.wt-mb-xs-0')
        accBtn.click()

        siBtn = driver.find_element(By.CSS_SELECTOR,'.wt-btn.wt-btn--small.wt-btn--transparent.wt-mr-xs-1.inline-overlay-trigger.signin-header-action.select-signin')
        siBtn.click()

        time.sleep(1)
        emailField = driver.find_element(By.XPATH,"//input[@id='join_neu_email_field']")
        emailField.send_keys(username)

        time.sleep(1)
        pwdField = driver.find_element(By.CSS_SELECTOR,'#join_neu_password_field')
        pwdField.send_keys(password)


        siBtn2 = driver.find_element(By.CSS_SELECTOR,"button[value='sign-in']")
        siBtn2.click()

        #shopmanager
        time.sleep(2)
        shopMng = driver.find_element(By.XPATH,"//a[contains(@href,'https://www.etsy.com/de/your/shops/me/dashboard?ref=hdr-mcpa')]")
        shopMng.click()

        #Finanzen Button
        time.sleep(2)
        fnBtn = driver.find_element(By.CSS_SELECTOR,".list-nav-item.pl-xs-3.pr-xs-2[href='/your/bill']")
        fnBtn.click()

        #Monatliche Abrechnung
        time.sleep(2)
        opBtn = driver.find_element(By.XPATH,"//a[contains(@href,'/your/account/payments/monthly-statement?ref=seller-platform-mcnav')]")
        opBtn.click()


        time.sleep(2)
        dlBtn = driver.find_element(By.CSS_SELECTOR,".wt-btn.wt-btn--primary.wt-btn--small-xs")
        dlBtn.click()

        time.sleep(1000)
        # time.sleep(2)
        # opBtn = driver.find_element(By.XPATH,"//select[@id='filter-csv-type']")
        # opBtn.click()

        # time.sleep(2)
        # bestelltArtikel = driver.find_element(By.XPATH,"//option[@value='transaction-level']")
        # bestelltArtikel.click()

        # time.sleep(2)
        # jahr = driver.find_element(By.XPATH,"//select[@id='filter-year']")
        # jahr.click()

        # time.sleep(2)
        # jahr = driver.find_element(By.XPATH,"//option[@value='2022']")
        # jahr.click()

        # time.sleep(2)
        # csvDlBtn = driver.find_element(By.CSS_SELECTOR,"button[class='btn-primary small']")
        # csvDlBtn.click()
    
