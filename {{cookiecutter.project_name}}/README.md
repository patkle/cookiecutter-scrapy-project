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
{%- if cookiecutter.host_on_kaggle == "y" %}
The dataset can be found [here](__kaggle_dataset_url__).  
A Jupyter Notebook with some EDA on that data can be found [here](__kaggle_notebook_url__).  
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
|placeholder   |string   |placeholder in case I want to add another arg   |

{% if cookiecutter.proxy_service != "None" %}
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
{%- endif %}
  
{% if cookiecutter.deploy_to_scrapy_cloud == "y" %}
## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).  
    {%- if cookiecutter.proxy_service != "None" -%}
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
{%- endif %}
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
