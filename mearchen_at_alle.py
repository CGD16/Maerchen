import scrapy

class mearchen_at_alle(scrapy.Spider):
    name = "mearchen_sammlung"
    start_urls = ['https://www.sagen.at/texte/maerchen/maerchen.htm']

    def parse(self, response):
        for link_to_nation in [response.urljoin(sublink) for sublink in response.css('div#main_div a.textNormal::attr(href)').extract()]:
            yield response.follow(link_to_nation, callback=self.get_nation_stories)

    def get_nation_stories(self, response):
        for link_to_stories in [response.urljoin(sublink) for sublink in response.css('div#main_div a.textNormal::attr(href)').extract()]:
            yield response.follow(link_to_stories, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': response.css('span.textKleinRotFett a::text').get().strip(),
            'Titel': response.css('div#main_div h1.main_title::text').get(),
            'Inhalt': response.css('div#main_div p::text').extract(),
            'Link': response
        }


