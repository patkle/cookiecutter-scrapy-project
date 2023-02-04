{%- if cookiecutter.proxy_service != "None" -%}
import os
{% endif %}

BOT_NAME = "{{cookiecutter.__project_slug}}"

SPIDER_MODULES = ["{{cookiecutter.__project_slug}}.spiders"]
NEWSPIDER_MODULE = "{{cookiecutter.__project_slug}}.spiders"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"

ROBOTSTXT_OBEY = False

# HTTPCACHE_ENABLED = True
# HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 400, 401, 402, 403, 404]

{% if cookiecutter.proxy_service == "Zyte Smart Proxy Manager" -%}
DOWNLOADER_MIDDLEWARES = {"scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610}
ZYTE_SMARTPROXY_ENABLED = True
ZYTE_SMARTPROXY_APIKEY = os.environ.get("ZYTE_SMARTPROXY_APIKEY")
{%- endif %}
{% if cookiecutter.proxy_service == "ScraperAPI" -%}
DOWNLOADER_MIDDLEWARES = {
    "scrapy_scraperapi_middleware.ScrapyScraperAPIMiddleware": 350,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 400,
}
SCRAPERAPI_KEY = os.environ.get("SCRAPERAPI_KEY")
{%- endif %}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
