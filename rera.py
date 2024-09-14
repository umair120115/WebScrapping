# Extraction of data from a website 

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://hprera.nic.in/PublicDashboard'

driver=webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(20)

links=driver.find_elements(By.CSS_SELECTOR,'a[onclick="tab_project_main_ApplicationPreview($(this));"]')


for i in range(6):
    links[i].click()
    details=driver.find_elements(By.CSS_SELECTOR,'td[class="fw-600"]')
    close_btn=driver.find_element(By.CSS_SELECTOR,'button[class="btn btn-sm btn-secondary"]')

   
    for detail in details:
        print(detail.text)
    close_btn.click()

driver.close()
