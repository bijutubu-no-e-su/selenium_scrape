
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time
import csv
print('INFO:start')
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1200x600')
driver = webdriver.Chrome('/usr/lib64/chromium-browser/chromedriver',chrome_options=options)
driver.get('')
driver.title
csv_contents =[]
i =0
while i  < 100:
    time.sleep(2)
    print (driver.current_url)
    contents = driver.find_elements_by_css_selector('a.view-grid-container-wrapper')
    
    if contents== []:
        break
    for content in contents:
            print(content.get_attribute('title'),content.get_attribute('href'))
            csv_contents.append([content.get_attribute('title'),content.get_attribute('href')])
    
    driver.find_element_by_xpath( '//*[@class="categories-btn p-next"]').click()
    i = i +1
with open('contents.csv','wt')as fout:
    csvout= csv.writer(fout)
    csvout.writerows(csv_contents)
driver.quit()

