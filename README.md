# Quotes Scraper

This Scrapy project extracts quotes, authors, and tags from http://quotes.toscrape.com. It handles errors and includes some techniques to avoid being blocked by the website.

## Project Structure

The spider "quotes" is defined in the `quotes_spider.py` file located in the `spiders` directory. 

The spider starts by making requests to the URLs defined in the `start_urls` attribute. When a response is received, the `parse` method is called to extract the data.

## What The Spider Does

Here's a brief description of what the spider does:

1. The spider sends a GET request to the URLs defined in the `start_urls`.
2. It then extracts the data contained in the quote elements of the page, specifically the text, author, and tags.
3. The extracted data is then stored in a Python dictionary and yielded.
4. The spider also looks for the link to the next page and follows it if found.
5. This process repeats for all the subsequent pages until there are no more pages left to scrape.

The spider also has error handling for HTTP errors, DNS lookup errors, and timeout errors.

## Running The Spider

Here's a step-by-step process on how to setup and run the Scrapy spider correctly:

Create a new Scrapy project: In your terminal, navigate to the directory where you want to create your new Scrapy project. Enter the following command:
```
scrapy startproject myproject
```

Navigate to your new Scrapy project directory:
```
cd myproject
```

Create a new Spider: In the myproject directory, there's a subdirectory named spiders. You need to create your spider within this directory. Navigate to spiders directory:
bash
```
cd myproject/spiders
```

Now, create a new Python file here, say quotes_spider.py, and paste your spider code into this file.
```
nano quotes_spider.py
```

Navigate back to the project directory:
```
cd ../..
```

Run the Spider: Now you can run your spider using the crawl command followed by the name of the spider:
```
scrapy crawl quotes -o quotes.json
```
The scrapy crawl quotes -o quotes.json command must be run from the top level of your Scrapy project (i.e., in the myproject directory), not from inside the spiders directory. The -o quotes.json part of the command tells Scrapy to store the scraped data in a JSON file.

Remember to replace myproject and quotes_spider.py with the actual names you've used for your Scrapy project and spider file.

## Prerequisites
Make sure you have the following prerequisites before running the spider:

```
Python 3
```
```
Scrapy (pip install scrapy)
```

## Responsible Usage
This spider is for educational purposes only. Always ensure that you're allowed to scrape a website and that you respect its scraping policy (usually found in the robots.txt file). Be careful not to overwhelm the website with too many requests.

Remember to replace `quotes` with the actual name of your spider if you've named it differently.