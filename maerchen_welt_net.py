import scrapy

class mearchen_welt_net(scrapy.Spider):
    name = 'mearchen_net'
    start_urls = ['http://www.maerchen-welt.net/russische-volksmaerchen/',
                  'http://www.maerchen-welt.net/ukrainische-volksmaerchen/',
                  'http://www.maerchen-welt.net/belorussische-volksmaerchen/',
                  'http://www.maerchen-welt.net/maerchen-der-brueder-grimm/']

    def parse(self, response):
        # Herkunftsmärchen betrachten
        links = response.css('div.entry-content > p > a::attr(href)')
        for link in links:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': response.css('footer.entry-meta > a[rel="category tag"]::text').get(),
            'Titel': response.css('header.entry-header > h1.entry-title::text').get(),
            'Inhalt': response.css('div.entry-content p::text').getall(),
            'Link': response
        }

