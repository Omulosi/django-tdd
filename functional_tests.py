from selenium import webdriver
import chromedriver_binary

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
