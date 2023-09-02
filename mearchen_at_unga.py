import scrapy

class Ungarn(scrapy.Spider):
    name = 'ungarn_scrapy'
    start_urls = ['https://www.sagen.at/texte/maerchen/maerchen_ungarn/ungarn_volksmaerchen/volksmaerchen_ungarn.htm']

    def parse(self, response):
        for link in [response.urljoin(sublink) for sublink in response.css('div#main_div a.textNormal::attr(href)').extract()]:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': 'Ungarisch',
            'Titel': response.css('div#main_div h1.main_title::text').get(),
            'Inhalt': response.css('div#main_div p::text').getall()[:-2],
            'Link': response

        }
