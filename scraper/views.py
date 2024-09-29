from django.shortcuts import render, redirect
from .tasks import run_yahoo_scraper
import json
from ecommerce_scraper_project import redis_client


def home(request):
    if request.method == "POST":
        run_yahoo_scraper()
        return redirect("results")
    return render(request, "scraper/home.html")


def results(request):

    r = redis_client
    products = []
    data = r.get("lol")

    if data:
        products = json.loads(data)
        print(products)
    return render(request, "scraper/results.html", {"products": products})
