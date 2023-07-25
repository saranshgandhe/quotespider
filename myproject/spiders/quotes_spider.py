import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537',
        'DOWNLOAD_DELAY': 3
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.errback_httpbin,
                                 dont_filter=True)

    def parse(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError occurred on %s', response.url)

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError occurred on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError occurred on %s', request.url)
