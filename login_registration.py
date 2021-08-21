#регистрация аккаунта
# import time
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account_btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# my_account_btn.click()
# text_email = driver.find_element_by_id('reg_email')
# text_email.send_keys('zhiga@mail.ru')
# text_password = driver.find_element_by_id('reg_password')
# text_password.send_keys('MashaZhiga624!')
# register_btn = driver.find_element_by_name('register')
# register_btn.click()
# driver.quit()

#вход в систему
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account_btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# my_account_btn.click()
# username = driver.find_element_by_id('username')
# username.send_keys('zhiga@mail.ru')
# text_password = driver.find_element_by_id('password')
# text_password.send_keys('MashaZhiga624!')
# login_btn = driver.find_element_by_name('login')
# login_btn.click()
# logout_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/customer-logout/"]:nth-child(1)')
# ))
# driver.quit()










