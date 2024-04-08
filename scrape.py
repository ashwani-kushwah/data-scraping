import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape data
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=iphone&_sacat=0"

# Set headers to mimic a web browser for better scraping compatibility
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# An empty dictionary to store scraped data (title and price)
data = {'Title': [], 'Price': []}

# Sending a request to the URL
r = requests.get(url, headers=headers)
# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

# Uncomment the following line if you want to view the parsed HTML structure
# print(soup.prettify())

# Select all 'span' elements within 'div' tags with class 's-item__title' (targets titles)
spans = soup.select("div.s-item__title span")
# Select all 'span' elements with class 's-item__price' (targets prices)
prices = soup.select("span.s-item__price")


# Iterate through each title 'span' element
for span in spans:
    title = span.get_text(strip=True)   # Extract the text content of the span element and strip extra spaces
    data['Title'].append(title)     # Append the extracted title to the 'Title' list in the data dictionary

# Iterate through each price 'span' element
for price in prices:
    
    price = price.get_text(strip=True)  # Extract the text content of the span element and strip extra spaces
    data['Price'].append(price)    # Append the extracted price to the 'Price' list in the data dictionary

    # Check if the length of both lists (titles and prices) are equal
    # This ensures we have corresponding data for each product
    if len(data['Price']) == len(data['Title']):
        break   # If lengths are equal, break the loop to avoid extra iterations


# Create a pandas DataFrame from the scraped data dictionary
df = pd.DataFrame.from_dict(data)

# Save the DataFrame to a CSV file named 'data.csv'
df.to_csv('data.csv')
