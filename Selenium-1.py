from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.pl")

#locators
google_cookies = "L2AGLb"
google_logo = "/html/body/div[1]/div[2]/div/a/picture/img"
google_searchField = "q"
google_searchButton = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
search_txt = "Tesla"
site_nav = "/html/body/div[5]/section/div/div/div/header/ol[1]"
#price_1 = "/html/body/div[5]/main/div/div[2]/div/section/div/p[1]/strong"


#------------------------------------------------------------------------------------------------------------------------------------

#acceptCookies
popup = driver.find_element(By.ID, google_cookies)
popup.send_keys(Keys.ENTER)

#google logo
#glogo = driver.find_element(By.XPATH, google_logo)
#print('Google - Logo is visible =', glogo.is_displayed())

#google search & enter
search_f = driver.find_element(By.NAME, google_searchField)
search_f.send_keys(search_txt)
search_b = driver.find_element(By.XPATH, google_searchButton)
search_b.send_keys(Keys.ENTER)
enter_site = driver.find_element(By.PARTIAL_LINK_TEXT, search_txt)
enter_site.send_keys(Keys.ENTER)

#site nav visible
nav = driver.find_element(By.XPATH, site_nav)
print('Navigation bar is displayed =', nav.is_displayed())

#for learning purposes
hold = input()

driver.close()