#Importing necessary modules for webscraping

import requests
from bs4 import BeautifulSoup
import pandas
import csv

#downloading the webpage as a HTML

html_data=requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off").text

#Creating a beautiful Soup object

soup = BeautifulSoup(html_data,"html5lib")

laptop_product_block = soup.find_all("div", class_="_1AtVbE col-12-12")

#Creation of a dataframe
laptop_data=pandas.DataFrame(columns = ["Laptop Name", "Price","Rating"])

for laptop in laptop_product_block:
    laptop_name = laptop.find("div", class_="_4rR01T")
    #For checking if the find() returns None then .text function doesn't work.
    if(laptop_name==None):
        continue
    laptop_name = laptop.find("div", class_="_4rR01T").text
    laptop_price = laptop.find("div", class_="_30jeq3 _1_WHN1").text
    laptop_rating = laptop.find("div", class_="_3LWZlK").text
    
    laptop_data= laptop_data.append({"Laptop Name": laptop_name, "Price":laptop_price, "Rating":laptop_rating}, ignore_index= True)

print(laptop_data)   #Printing the dataframe
laptop_data.to_csv("File1.csv", encoding="utf-8")
#encoding="utf-8" ----> It is there to prevent encoding error
#File 1 is saved in the current directory



    
    







    

                               



