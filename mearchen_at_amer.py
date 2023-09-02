import scrapy

class mearchen_at_amer(scrapy.Spider):
    name = 'mearchen_amer'
    start_urls = ['https://www.sagen.at/texte/maerchen/maerchen_usa/maerchen_indianer.html']


    def parse(self, response):
        for link in [response.urljoin(sublink) for sublink in response.css('a.textNormal::attr(href)').extract()]:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': 'Deutsch (AT)',
            'Titel': response.css('h1.main_title::text').get(),
            'Inhalt': response.css('div#main_div p::text').getall(),
            'Link': response
        }


