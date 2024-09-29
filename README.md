# ecommerce_scraping

This project is a web scraping application that scrapes product listings from a Japanese e-commerce platform using Scrapy. It also implements Celery for asynchronous task processing and is built using Django. Docker is used to manage the environment.

## Prerequisites
- **Docker**: Ensure Docker is installed on your system. [Install Docker](https://docs.docker.com/get-docker/)

## Setup Instructions

### 1. Clone the repository
Start by cloning the project repository:

```bash
git clone https://github.com/iamajay626/ecommerce_scraping.git
cd ecommerce_scraping
```

### 2. Build and start the application using Docker Compose
Run the following command to build and start the containers for Django, Scrapy, Celery, and Redis:

```bash
docker-compose up
```

Docker will automatically handle building the images, starting the services, and linking them together.

Once the containers are running, you can access the application at:

```bash
http://127.0.0.1:8000/
```
