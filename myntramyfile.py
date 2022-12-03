
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Storage Array
sneakers = []

#Scraping Function
def scrape_page(page_no):
    
    driver.get(f"https://www.myntra.com/shoes?p={page_no}")
    shoes_myntra = driver.find_elements(By.CLASS_NAME, "product-base")
    for shoes in shoes_myntra:
        try:
            shoes.find_element(By.CLASS_NAME,"product-ratingsContainer")
        except:
            continue    
        details = shoes.text.split('\n')
        rating = details[0]
        name = details[3]
        category = details[4]
        if "sneakers" in category.lower():
            sneakers.append([rating,name,category])

#We want 4 pages.
for i in range(4):
    scrape_page(i+1)

#Output File
output = open("final result.csv", "w")
for sneaker in sneakers:
    print(*sneaker, sep=",", file=output)

output.close 

