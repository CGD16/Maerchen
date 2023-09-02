import scrapy


class maerchen_welt_eu(scrapy.Spider):
    name = "maerchen_eu"
    allowed_domains = ['maerchen-welt.eu']
    start_urls = ['http://maerchen-welt.eu/']

    def parse(self, response):
        # response.xpath('//p[@class="text"]//a/@href').get() --> 'daenemark/andersen/der_tannenbaum_maerchen.htm'
        full_links = [response.urljoin(sublink) for sublink in response.xpath('//p[@class="text"]//a/@href').extract()]
        for link in full_links:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': response.css('h1::text').get(),
            'Titel': response.css('h2::text').get(),
            'Inhalt': response.css('p.text::text').getall()[:-1],
            'Link': response
            # 'Eckdaten': response.css('p.text > span::text').get()
        }