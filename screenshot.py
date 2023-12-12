from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://github.com/flsouto/programante/tree/master/nodejs-serve-app-use-express")
element = driver.find_element("css selector", "article")
element.screenshot('article.png')
