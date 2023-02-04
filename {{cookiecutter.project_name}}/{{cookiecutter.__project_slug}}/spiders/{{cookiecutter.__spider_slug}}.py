from scrapy import Request, Spider


class {{cookiecutter.spider_name.replace(' ', '')}}Spider(Spider):
    name = "{{cookiecutter.__spider_slug}}"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(f"https://www.example.com?page={i}")

    def parse(self, response):
        pass
