from selenium import webdriver


driver=webdriver.Chrome("F:\\install\\Selenium\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get_screenshot_as_file("./screenshots/Abrakadabra.png")
driver.quit()
