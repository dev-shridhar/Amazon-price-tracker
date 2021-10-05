import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "theanakinskywalker.force@gmail.com"
password = "anakin@123"
URL = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5VSQNG?ref_=ast_sto_dp&th=1&psc=1"

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "en-US,en-IN;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6"
}
response = requests.get(URL,headers= headers)

web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

product = soup.find(name="span",class_="a-size-large product-title-word-break").text.strip()
the_price = soup.find(name= "span",class_="a-size-medium a-color-price priceBlockBuyingPriceString").text.replace("₹","")
price = float(the_price.replace(",",""))
message = f"{product} is now at {price}"

BUY_PRICE = 90000

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="sidkulkarnimj@gmail.com",
                            msg=f"Subject:Amazon prize alert!\n\n{message}\n{URL}"
                            u'\u2011'.encode('ascii', 'ignore'))
