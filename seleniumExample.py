from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://seleniumhq.org')
element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/a/img')
from selenium.webdriver.common.keys import Keys
element.click()
driver.back()
search = driver.find_element_by_id('gsc-i-id1')
search.send_keys('webdriver')
search.send_keys(Keys.RETURN)
# element = driver.find_element_by_name('q')
# element.send_keys('test')


# element.send_keys(Keys.RETURN)

# element2 = 
