# Web scraping

There are incredible amount of data on the internet which can be used for your personal interest or in the organisations. We need data to find some insights and do some valuable research. by just looking at the data on internet and trying to find some trends, patterns or valuable insights from an enourmous amount is not possible and not worth your time. 
data is the most valuable asset on which we can rely taking some important decisions in your personal life or in organizations. 

# why we should use the data present on internet?

Here I have given some real time use cases why we need data present on internet. 
1. Use case in day to day life
    * we buy mostly everything online in this digital era. And to buy something we always need to scroll alot of website and pages to pay attention on the price, quality, and reliability of the product that we want to buy.
    * For example we want to buy a data science book in python or R. What we do is to scroll the online website such as amazon and check the price and reviews of the each book but still don't understand if this book is good or not. what other people say about after reading the book. we try to read each reviews and that can be very time consuming and yet we don't know if we are reading the right books reviews because there are so many books available on the same topic. 

2. Use case in Organisations
    * There are many use cases in the organization where you need to collect the data from online and do some analysis for decision making, finding new trend and patters in the market. customers feedback on a product and so on.
    
# How to collect the data from internet 
* We can use webscraping technique to collect data from internet. 

There are enough amount of packages in python to do web scraping such as:
1. Beautiful Soup
2. Mechanical Soup
3. Selenium
4. Scrapy 

Also we can collect the data via APIs. Because in some cases you need to find some hidden APIs to request the data from the  website. 

Here I have used Selenium to scrape data about data science books from amazon website. 

What you need to scrape the data from amazon. 

1. Python IDE: To write an efficient code (I have used jupyter notebook)
2. Selenium: Python package which is used to scape the data faster. 
3. Web driver: web driver is a tool to open the browser we chose (Chrome, Firefox, Edge, or Safari). Whatever browser you want to use, the driver should be compatible with your browser version and your operating system.

Here you can find all the information about selenium: https://selenium-python.readthedocs.io/

How to install selenium:

pip install selenium

Download web driver:
If you are using chrome then download the chrome driver from here https://chromedriver.chromium.org/downloads and save it in your computer. later you need to provide a path to where you have saved the chrome driver. 

Note: You need to download the same version of web driver of your web browser. For example if you are using chrome of version 93 then download Chrome driver of version 93.0.4577.15 which you can find from the above link.

To see how I did the scraping. all the code open the Scraper.ipynb file. 

Analyse those data and find some insights and use cases. 

I have intended to find the most trending data science books on amazon, and most popular subjects of the books.  


### Trending-data-science-book-on-amazon

1. To find the trending data science books I Scraped the data science books available on amazon using selenium and python.

### I choose to scrape informations below 

  * Book name
  * Rating stars
  * Rating counts
  * Price 
  * Link of book 
  
  # Store the CSV file into SQL 
  
  ![alt text](https://github.com/vinamrata-git/Amazon-scraper-selenium-python/blob/main/Img/storedata2sql.png)
