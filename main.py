from selenium import webdriver
from lxml import html
from time import sleep
import csv
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.in/")


search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("edifice casio watches for men")
search.send_keys(Keys.ENTER)

sleep(1)
at1=[]
at2=[]
at3=[]
at4=[]
at5=[]
tree=html.fromstring(driver.page_source)

for product_tree in tree.xpath('//div[contains(@data-cel-widget,"search_result_")]'):
    brand = product_tree.xpath('.//span[@class="a-size-base-plus a-color-base"]/text()')
    at1.append(brand)

    title=product_tree.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')
    at2.append(title)

    reviews=product_tree.xpath('.//span[@class="a-size-base"]/text()')
    at3.append(reviews)

    price=product_tree.xpath('.//span[@class="a-price-whole"]/text()')
    at4.append(price)

    stock_details = product_tree.xpath('.//span[@class="a-size-small a-color-price"]/text()')
    at5.append(stock_details)

t1=[]
for i in at1:
    if i==[]:
        t1.append("NaN")
    else:
        t1.append(i)

t2=[]
for i in at2:
    if i==[]:
        t2.append("NaN")
    else:
        t2.append(i)

t3=[]
for i in at3:
    if i==[]:
        t3.append("NaN")
    else:
        t3.append(i)

t4=[]
for i in at4:
    if i==[]:
        t4.append("NaN")
    else:
        t4.append(i)

t5=[]
for i in at5:
    if i==[]:
        t5.append("NaN")
    else:
        t5.append(i)


output1=[]
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output1.append(i)

reemovNestings(t1)
print(output1)

output2=[]
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output2.append(i)
reemovNestings(t2)
print(output2)




output3=[]
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output3.append(i)
reemovNestings(t3)
print(output3)


output4=[]
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output4.append(i)
reemovNestings(t4)
print(output4)


output5=[]
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output5.append(i)
reemovNestings(t5)
print(output5)


print(len(output1))
print(len(output2))
print(len(output3))
print(len(output4))
print(len(output5))
lst=[]
for i in range(len(output1)):
    lst.append(output1[i])
    lst.append(output2[i])
    lst.append(output3[i])
    lst.append(output4[i])
    lst.append(output5[i])

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 5

rows = list(divide_chunks(lst, n))
print(rows)

driver.quit()


headings=['BRAND','NAME','No of Reviews','Price','Availability']
filename = "Product_info1.csv"

# writing to csv file
with open(filename, 'w',encoding="utf-8") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(headings)

    # writing the data rows
    csvwriter.writerows(rows)