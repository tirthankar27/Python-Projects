from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.pythonanywhere.com/login/")

user_name=driver.find_element(By.NAME, value='auth-username')
user_name.send_keys('tirthankarghosh4@gmail.com')

user_password=driver.find_element(By.NAME, value='auth-password')
user_password.send_keys('&0r1va*FLU5#DoM4')

login=driver.find_element(By.ID, value='id_next')
login.click()

# driver.quit()
# driver.close() quit a single tab