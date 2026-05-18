import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Happy87911%40%40@localhost/business_dashboard"

engine = create_engine(DATABASE_URL)

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 26):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        data.append({
            "business_name": title,
            "category": ["Restaurant", "Gym", "Cafe", "Salon", "Hospital"][page % 5],
            "city": ["Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad"][page % 5],
            "address": "Demo Address",
            "phone": "N/A",
            "source": "BooksToScrape"
        })

print("Total Records:", len(data))

df = pd.DataFrame(data)

df.to_sql("listing_master", con=engine, if_exists="append", index=False)

print("Data inserted into MySQL successfully!")