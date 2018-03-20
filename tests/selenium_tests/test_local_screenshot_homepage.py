from selenium import webdriver


driver=webdriver.Chrome("F:\\install\\Selenium\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://127.0.0.1:1234/opencart.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get_screenshot_as_file("./screenshots/Abrakadabra_local.png")
driver.quit()
