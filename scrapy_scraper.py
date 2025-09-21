import scrapy

class QuotesSpider(scrapy.Spider):
    """A basic Scrapy spider to scrape quotes from quotes.toscrape.com
    """
    name = "quotes" # required name for distinguishing spiders
    start_urls = ["http://quotes.toscrape.com/"] # required initial URL for sending requests

    def parse(self, response):
        for quote in response.css(".quote"):
            yield {
                "text": quote.css(".text::text").get(),
                "author": quote.css(".author::text").get(),
                "tags": "|".join(quote.css(".tags .tag::text").getall())
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)