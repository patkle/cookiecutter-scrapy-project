# {{cookiecutter.project_name}}


It uses Zyte Smart Proxy Manager.  
{% if cookiecutter.host_on_kaggle == "y" -%}
The dataset can be found [here.](__kaggle_dataset_url__).  
A Jupyter Notebook with some EDA on that data can be found [here](__kaggle_notebook_url__).  
{%- endif %}
{% if cookiecutter.deploy_to_scrapy_cloud == "y" -%}
This project can be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/)
{%- endif %}
- Uses [Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) or [ScraperAPI](https://www.scraperapi.com/?fp_ref=patrick50)?

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


## Setting up locally

When setting up this project locally you must create a **.env** file with `ZYTE_SMARTPROXY_APIKEY` equal to your smart proxy manager api key.  

{% if cookiecutter.deploy_to_scrapy_cloud == "y" -%}
## Deploy to Scrapy Cloud

There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).  
Don't forget to add the ZYTE_SMARTPROXY_APIKEY setting in your cloud project's settings!
{%- endif %}

## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
