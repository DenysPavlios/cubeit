import scrapy

class GITSpider(scrapy.Spider):
    name = "djini"
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Golang&region=UKR&location=kyiv"]
    current_page = ""

    def parse(self, response):
        if response.url == self.current_page:
            return

        self.current_page = response.url

        for p in response.css('.job-list-item__title'):
            # if ('Trainee AQA Engineer' in p.css('a::text').get()):
            p_text = p.css('a::text').get()
            p_url = response.urljoin(p.css('a::attr(href)').get())
            item = {p_url: p_text.strip()}
            yield item

        next_page = response.css('a.page-link::attr(href)').get()
        if next_page:
            telegramm = response.follow(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)


#
# import json
#
# # scrapy runspider parse_3.py -o github_link.json
#
# with open('github_link.json') as f:
#     data = json.load(f)
#
# for item in data:
#     for key, value in item.items():
#
#         print(f"{key + value}")
#
