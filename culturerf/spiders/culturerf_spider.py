import scrapy

class CultureSpider(scrapy.Spider):
    name = 'culture'
    #https://www.culture.ru/literature/poems?page=1&limit=45&query=
    allowed_domains = ['www.culture.ru']
    start_urls = ['https://www.culture.ru/literature/poems/']
    pages_count = 798


    def start_requests(self):
        for page in range(1, 1+self.pages_count):
            url = f'https://www.culture.ru/literature/poems?page={page}&limit=45&query='
            yield scrapy.Request(url, callback=self.pages_pages)


    def pages_pages(self, response, **kwargs):
        for href in response.css('.card-heading_title-link::attr(href)').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response, **kwargs):
        item = {
                "author": response.css('.entity-heading_subtitle::text').getall(),
                "title": response.css('.entity-heading_title::text').getall(),
                "content": [text.strip('') for text in response.css('.content-columns_block *::text').getall()]
                    }
        yield item
