# {{cookiecutter.project_name}}

{% if cookiecutter.deploy_to_scrapy_cloud == "y" -%}
This project is configured to be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).  
{% endif %}

{%- if cookiecutter.proxy_service == "Zyte Smart Proxy Manager" %}
It uses [Zyte Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) as proxy service.  
{% endif %}
{%- if cookiecutter.proxy_service == "ScraperAPI" %}
It uses [ScraperAPI](https://www.scraperapi.com/?fp_ref=patrick50) as proxy service.  
{% endif %}
{%- if cookiecutter.use_spidermon == "y" %}
This project uses Spidermon for monitoring purposes. 
It is also set up to send messages via a telegram bot.  
{%- endif %}
{%- if cookiecutter.host_on_kaggle == "y" %}
The dataset can be found [here](TODO).  
A Jupyter Notebook with some EDA on that data can be found [here](TODO).  
{%- endif %}

## {{cookiecutter.spider_name}}

The spider can be ran with
```zsh
python3 -m scrapy crawl {{cookiecutter.__spider_slug}} -a pages=5 -O {{cookiecutter.__spider_slug}}.csv
```

### Arguments

With `-a` you can specify arguments for the spider.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |

{% if cookiecutter.proxy_service != "None" or cookiecutter.use_spidermon == "y" %}
## Setting up locally
  
When setting up this project locally you must create a **.env** file with the following data:  

|setting   |description   |  
|---|---|  
    {%- if cookiecutter.proxy_service == "Zyte Smart Proxy Manager" %}
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |  
    {%- endif -%}
    {%- if cookiecutter.proxy_service == "ScraperAPI" %}
|SCRAPERAPI_KEY   |your api key for ScraperAPI   |  
    {%- endif -%}
    {%- if cookiecutter.use_spidermon == "y" %}
|[SPIDERMON_TELEGRAM_SENDER_TOKEN](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |authorization token for your telegram bot   |  
|[SPIDERMON_TELEGRAM_RECIPIENTS](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |@channelname, chat it or group id   |  
    {%- endif -%}
{%- endif %}
  
{% if cookiecutter.deploy_to_scrapy_cloud == "y" %}
## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).  
    {%- if cookiecutter.proxy_service != "None" or cookiecutter.use_spidermon == "y" -%}
Don't forget to add the following settings in your cloud project's settings:
|setting   |description   | 
|---|---|
        {%- if cookiecutter.proxy_service == "Zyte Smart Proxy Manager" %}
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
        {%- endif -%}
        {%- if cookiecutter.proxy_service == "ScraperAPI" %}
|SCRAPERAPI_KEY   |your api key for ScraperAPI   |
        {%- endif -%}
    {%- endif -%}
    {%- if cookiecutter.use_spidermon == "y" %}
|[SPIDERMON_TELEGRAM_SENDER_TOKEN](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |authorization token for your telegram bot   |  
|[SPIDERMON_TELEGRAM_RECIPIENTS](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |@channelname, chat it or group id   |  
    {%- endif -%}
{%- endif %}
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
