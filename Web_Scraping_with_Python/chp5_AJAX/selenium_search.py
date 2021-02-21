import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


# 对PhantomJS的Selenium支持已经被禁止，请使用Chrome或Firefox的无头版本
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
# driver = webdriver.Chrome()

driver.get('http://example.python-scraping.com/search')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '20';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
driver.implicitly_wait(30)
links = driver.find_elements_by_css_selector('#results a')
countries_or_districts = [link.text for link in links]
print(countries_or_districts)

time.sleep(2)
pic_path = './data/python_website.png'

# 想起来之前用过find_elements_by_xpath（）来定位过页面元素的位置，发现以下方法可用：
# 即先得到标签的width、height，然后再设置窗口大小。经过测试可以实现对网页整体截图
eles = driver.find_elements_by_xpath("//html")
locs = []
width = 1920
height = 1080
if len(eles) > 0:
    width = int(eles[0].size['width'])
    height = int(eles[0].size['height'])

driver.set_window_size(width, height)
driver.save_screenshot(pic_path)
driver.close()
