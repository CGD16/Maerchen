import scrapy

class mearchen_at_öste(scrapy.Spider):
    name = 'mearchen_öste'
    start_urls = ['https://www.sagen.at/texte/maerchen/maerchen_oesterreich/allgemein/maerchen_oesterreich_allgemein.htm',
                  'https://www.sagen.at/texte/maerchen/maerchen_oesterreich/allgemein/vernaleken/alpenmaerchen_vernaleken.html']


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