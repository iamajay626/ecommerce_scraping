import scrapy
import redis
import json

r = redis.Redis(host="redis", port=6379)


class YahooSpider(scrapy.Spider):

    name = "yahoo_spider"
    allowed_domains = ["fril.jp"]
    start_urls = ["https://fril.jp/category/682"]

    page_limit = 6

    index = 0

    final_data = []

    def parse(self, response):
        for product in response.css("section.view.view_grid div.item"):
            name = product.css('span[data-test="item_name"]::text').get(default="none")
            selling_status = product.css("div.item-box__soldout_ribbon::text").get()
            if selling_status:
                selling_status = "sold out"
            selling_status = "avalible "
            if name is None:
                continue
            self.final_data.append(
                {
                    "title": name,
                    "selling_status": selling_status,
                }
            )

        self.index += 1

        if self.index != self.page_limit:
            next_page = response.css('a[rel="next"]::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)
            else:
                r.set("lol", json.dumps(self.final_data), ex=60)
        else:
            data = json.dumps(self.final_data)
            r.set("lol", data, ex=60)
