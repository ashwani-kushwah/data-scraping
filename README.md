# Data Scraping with Python 🐍

## Project Overview

This Python script scrapes data for iPhones listed on eBay. It utilizes the requests library to fetch the webpage content, **BeautifulSoup** for parsing the HTML structure, and 🐼 **Pandas** for creating a structured data frame.

## Functionality
* Fetches data for iPhones listed on eBay from a predefined URL.
* Extracts product titles and prices.
* Stores the scraped data in a pandas DataFrame.
* Saves the DataFrame to a CSV file named data.csv.

## Requirements
* Python 3.x
* requests library
  
  ```bash
  pip install requests
  ```
* beautifulsoup4 library
  
  ```bash
  pip install bs4
  ```
* pandas library
  
  ```bash
  pip install pandas
  ```

## Contributing

Contributions are welcome! If you have ideas for improvements or want to add more questions, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-new-question`
3. Commit your changes: `git commit -m 'Add a new question'`
4. Push to the branch: `git push origin feature-new-question`
5. Submit a pull request.
