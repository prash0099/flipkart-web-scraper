from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import csv

# Headless mode for Firefox
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

product = 'phone'

# Open CSV to write data
with open('flipkart_scraped_product_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Price', 'Product Link'])

    for i in range(1, 3):
        driver.get(f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
        wait = WebDriverWait(driver, 20)
        product_in=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'tUxRFH')))
        for info in product_in:
            try:
                name = info.find_element(By.CLASS_NAME, 'KzDlHZ').text
                print(name)
            except:
                name = 'N/A'
            try:
                price = info.find_element(By.CLASS_NAME, 'Nx9bqj').text
                print(price)
            except:
                name = 'N/A'
            try:
                href = info.find_element(By.CLASS_NAME, 'CGtC98').get_attribute('href')
                print(href)
            except:
                href = 'N/A'
            writer.writerow([name, price, href])
driver.close()
            

