from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://github.com/flsouto/programante/tree/master/nodejs-aws-lambda-s3")
element = driver.find_element("css selector", ".highlight-source-js pre")
element.screenshot('code.png')
