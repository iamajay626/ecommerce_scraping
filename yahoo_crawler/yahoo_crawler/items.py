import scrapy


class YahooScraperItem(scrapy.Item):
    product_title = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()
    product_availability = scrapy.Field()
