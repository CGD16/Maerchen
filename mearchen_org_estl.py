import scrapy

class mearchen_org_estl(scrapy.Spider):
    name = "mearchen_estl"
    start_urls = ['https://de.wikisource.org/wiki/Esthnische_M%C3%A4rchen']

    def parse(self, response):
        full_links = [response.urljoin(sublink) for sublink in response.css('ol > li > a::attr(href)').extract()]
        for link in full_links:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': response.css('tbody > tr:nth-of-type(7) > td:nth-of-type(2) > a::attr(title)').get(),
            'Titel': response.css('span.mw-page-title-main::text').get(),
            'Inhalt': response.css('div[style*="display:table; text-align:justify; text-indent:0px; padding-left:10px; padding-right:10px;"] > p::text').extract(),
            'Link': response
        }