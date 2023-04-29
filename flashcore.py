from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 

driver = webdriver.Firefox()

driver.get("https://flashscore.com.br")