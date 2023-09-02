import scrapy

class mearchen_org_deut(scrapy.Spider):
    name = "mearchen_deut"
    start_urls = ['https://de.wikisource.org/wiki/Kinder-_und_Haus-M%C3%A4rchen_Band_1_(1857)',
                  'https://de.wikisource.org/wiki/Kinder-_und_Haus-M%C3%A4rchen_Band_2_(1857)']

    def parse(self, response):
        full_links = [response.urljoin(sublink) for sublink in response.xpath('//table/tbody/tr/td/a/@href').extract()]
        for link in full_links:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': response.css('tbody > tr:nth-of-type(3) a::attr(title)').get(),
            'Titel': response.css('span.mw-page-title-main::text').get(),
            'Inhalt': response.css('div[style*="display:table; text-align:justify; text-indent:0px; padding-left:10px; padding-right:10px;"] > p::text').extract(),
            'Link': response
        }