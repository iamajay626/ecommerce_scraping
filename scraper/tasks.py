# scraper_app/tasks.py
import subprocess
from celery import shared_task
from ecommerce_scraper_project import redis_client


@shared_task
def run_yahoo_scraper():
    r = redis_client
    data = r.get("lol")

    if data:
        return
    subprocess.run(["scrapy", "crawl", "yahoo_spider"], cwd="yahoo_crawler")
