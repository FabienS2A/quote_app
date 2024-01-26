from pathlib import Path
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self): #crawler de page en page
        urls = [
            "https://quotes.toscrape.com",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text" : quote.css("span.text::text").get(),
                "author" : quote.css("small.author::text").get()
            }
        #go to next page
        url = response.css(".pager .next > a::attr(href)").get()
        if url is not None:
            yield response.follow(url=url, callback=self.parse)


