import os
import sys

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = 'Run Scrapy spider'

    def handle(self, *args, **options):
        # Set the path to the Scrapy project
        sys.path.append(os.path.join(os.path.dirname(__file__), '../../../yahoo_auction_scraper'))
        os.chdir(os.path.join(os.path.dirname(__file__), '../../../yahoo_auction_scraper'))

        from yahoo_auction_scraper.yahoo_spider import YahooSpider

        process = CrawlerProcess(get_project_settings())
        process.crawl(YahooSpider)
        process.start()