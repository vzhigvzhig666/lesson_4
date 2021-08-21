#отображение страницы товара
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# book_btn = driver.find_element_by_css_selector('[alt = "Mastering HTML5 Forms"]')
# book_btn.click()
# title = driver.find_element_by_css_selector('[itemprop="name"]')
# title_get_text = title.text
# assert title_get_text == "HTML5 Forms"
# driver.quit()

#количество товаров в категории
# import time
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
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# html_category = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
# html_category.click()
# element = driver.find_elements_by_class_name('attachment-shop_catalog')
# if len(element) == 3:
#    print('В разделе HTML 3 книги')
# else:
#    print('Ошибка. Количество товаров в разделе HTML:' + str(len(element)))
# driver.quit()

#сортировка товаров
# import time
# from selenium.webdriver.support.select import Select
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
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# selector = driver.find_element_by_css_selector('[value="menu_order"]')
# select_check = selector.get_attribute("selected")
# if select_check is not None:
#     print('Выбрана сортировка по умолчанию')
# else:
#     print('неверный выбор сортировки')
# selector_sort = driver.find_element_by_name('orderby')
# select = Select(selector_sort)
# select.select_by_value("price-desc")
# selector_check = driver.find_element_by_css_selector('[value="price-desc"]')
# select_check_1 = selector_check.get_attribute("selected")
# if select_check_1 is not None:
#     print('Выбрана сортировка от большего к меньшему')
# else:
#     print('неверный выбор сортировки')
# driver.quit()

#отображение, скидка товара
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
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# book_btn = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# book_btn.click()
# old_price = driver.find_element_by_css_selector('del>.woocommerce-Price-amount')
# old_price_get_text = old_price.text
# assert "₹600.00" in old_price_get_text
# if old_price_get_text is not None:
#     print('элемент ₹600.00 найден')
# else:
#     print('элемент не найден')
# new_price = driver.find_element_by_css_selector('ins>.woocommerce-Price-amount')
# new_price_get_text = new_price.text
# assert "₹450.00" in new_price_get_text
# if new_price_get_text is not None:
#     print('элемент ₹450.00 найден')
# else:
#     print('элемент не найден')
# img_btn = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CLASS_NAME,'attachment-shop_single'))
# )
# img_btn.click()
# close_btn = WebDriverWait(driver,5).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close'))
# )
# close_btn.click()
#
# driver.quit()

#проверка цены в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(5)
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# time.sleep(5)
# add_to_basket_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_to_basket_btn.click()
# time.sleep(5)
# # item_count = driver.find_element_by_css_selector('a>span.cartcontents')
# # item_count_get_text = item_count.text
# # assert "1 Item" in item_count_get_text - вот здесь почему-то код не работает,хотя проверка и подбор селектора по аналогии с ценой
# # if item_count_get_text is not None:
# #     print('В корзине 1 товар')
# # else:
# #     print('Количество товаров в корзине:', item_count_get_text)
# price_count = driver.find_element_by_css_selector('a>span.amount')
# price_count_get_text = price_count.text
# assert "₹180.00" in price_count_get_text
# if price_count_get_text is not None:
#     print('Стоимость товаров - ₹180.00')
# else:
#     print('Стоимость товаров -', price_count_get_text)
# basket_btn = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]')
# basket_btn.click()
# subtotal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-subtotal>td>.woocommerce-Price-amount')))
# total = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'strong>.woocommerce-Price-amount')))
# driver.quit()

#работа в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(5)
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,300);")
# add_to_basket_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_to_basket_btn.click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,500);")
# add_to_basket_btn_2 = driver.find_element_by_css_selector('[data-product_id="180"]')
# add_to_basket_btn_2.click()
# basket_btn = driver.find_element_by_class_name('wpmenucart-contents')
# basket_btn.click()
# time.sleep(5)
# basket_delete = driver.find_element_by_css_selector('[data-product_id="182"]')
# basket_delete.click()
# time.sleep(3)
# basket_undo = driver.find_element_by_css_selector('.woocommerce-message>a')
# basket_undo.click()
# amount_edit = driver.find_element_by_name('cart[4c5bde74a8f110656874902f07378009][qty]')
# amount_edit.clear()
# amount_edit.send_keys('3')
# update_basket_btn = driver.find_element_by_css_selector('[value="Update Basket"]')
# update_basket_btn.click()
# # amount_edit_new = driver.find_element_by_name('cart[4c5bde74a8f110656874902f07378009][qty]')
# # amount_edit_new_get_text = amount_edit_new.text
# # assert amount_edit_new_get_text == "3"
# time.sleep(3)
# apply_coupon_btn = driver.find_element_by_css_selector('[value="Apply Coupon"]')
# time.sleep(3)
# apply_coupon_btn.click()
# message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error>li'), "Please enter a coupon code."))
# driver.quit()

#покупка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(5)
# shop_btn = driver.find_element_by_css_selector('#menu-item-40>[href="http://practice.automationtesting.in/shop/"]')
# shop_btn.click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,300);")
# add_to_basket_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_to_basket_btn.click()
# basket_btn = driver.find_element_by_class_name('wpmenucart-contents')
# basket_btn.click()
# wait = WebDriverWait(driver, 10)
# checkout_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'checkout-button')))
# checkout_btn.click()
# waid = WebDriverWait(driver, 10)
# first_name = waid.until(EC.element_to_be_clickable((By.ID,'billing_first_name')))
# first_name.send_keys('Mariia')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Zhigalova')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('zhiga@mail.ru')
# phone = driver.find_element_by_id('billing_phone')
# email.send_keys('8123847')
# country_selector = driver.find_element_by_id('s2id_autogen1_search')
# country_selector.click()
# country_selector.send_keys('Albania')
# country_choose = driver.find_element_by_id('select2-result-label-1742')
# country_choose.click()
# town_city = driver.find_element_by_id('billing_city')
# town_city.send_keys('Cityy')
# state_county = driver.find_element_by_id('billing_state')
# state_county.send_keys('Stateee')
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys('12345')
# address = driver.find_element_by_id('billing_address_1')
# driver.execute_script("window.scrollBy(0,600);")
# check_pay = driver.find_element_by_id('payment_method_cheque')
# check_pay.click()
# place_order = driver.find_element_by_id('place_order')
# place_order.click()
# text_presented = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
# driver.quit()