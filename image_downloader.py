from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import base64
from urllib import request
import cv2 as cv
import os
import io
from PIL import Image

options = Options()

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)
person = 'J K Rowling'
driver.get('https://google.com')
el = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
el.send_keys(person,Keys.ENTER)
driver.implicitly_wait(5)
images = driver.find_element(By.CSS_SELECTOR,'#hdtb-sc>div>div>div.crJ18e>div>div:nth-child(2)>a')
images.click()
driver.implicitly_wait(5)
photos = driver.find_elements(By.CSS_SELECTOR,'#center_col img')
count = 0
while count != 100:
	src = photos[count]
	
	if src is not None:
		src = src.get_attribute('src')
		with request.urlopen(src) as response:
			im = response.read()	
			image = Image.open(io.BytesIO(im))
			width, height = image.size
			if (width > 150 and height > 150):
				with open(f"{''.join(person).replace(' ','_')}/result{count}.png",'wb') as f:
					f.write(im)
					img = cv.imread(f'result{count}.png')
					
					if img is not None:
						print(img.shape)
	count+=1
	
					
driver.close()