import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import csv

# the website i'm scrapping is https://www.transparenthands.org/page/{number}/?s=life
URL = 'https://www.transparenthands.org/page/'

for page in range(1, 10):
    # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example

    # check the url structure to add any other parameters that are needed
    req = requests.get(URL + str(page) + '/?s=life')
    soup = bs(req.text, 'html.parser')

    # find all the h3 tags with the class 'h4 text-bold'
    titles = soup.find_all('h3', attrs={'class', 'h4 text-bold'})

    # open a csv file to write to
    with open('data.csv', 'a') as csv_file:
        for i in range(1, 10):
            if page > 1:
                print(f"{(i-3)+page*15}" + titles[i].text)
                # write to a csv file
                writer = csv.writer(csv_file)
                writer.writerow([f"{(i-3)+page*15}" + titles[i].text])

            else:
                print(f"{i-3}" + titles[i].text)
                # write to a csv file
                writer = csv.writer(csv_file)
                writer.writerow([f"{i-3}" + titles[i].text])

    sleep(randint(2, 10))
