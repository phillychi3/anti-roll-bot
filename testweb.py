
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
#req_url = "https://reurl.cc/gWbmQb"
req_url = "https://discordgift.site/store/en-US/p/discord--discord-nitro"


chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)

browser.get(req_url)
sleep(5)

print(browser.current_url)

browser.close()

browser.quit()