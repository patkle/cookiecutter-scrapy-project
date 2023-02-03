#import os  # only necessary when using a proxy service

BOT_NAME = "{{cookiecutter.project_slug}}"

SPIDER_MODULES = ["{{cookiecutter.project_slug}}.spiders"]
NEWSPIDER_MODULE = "{{cookiecutter.project_slug}}.spiders"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"

ROBOTSTXT_OBEY = False

# HTTPCACHE_ENABLED = True
# HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 400, 401, 402, 403, 404]

## Proxy Services:

#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_scraperapi_middleware.ScrapyScraperAPIMiddleware": 350,
#    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 400,
#}
#SCRAPERAPI_KEY = os.environ.get("SCRAPERAPI_KEY")

#DOWNLOADER_MIDDLEWARES = {"scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610}
#ZYTE_SMARTPROXY_ENABLED = True
#ZYTE_SMARTPROXY_APIKEY = os.environ.get("ZYTE_SMARTPROXY_APIKEY")


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
