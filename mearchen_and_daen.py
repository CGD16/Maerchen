import scrapy


class mearchen_and_daen(scrapy.Spider):
    name = "mearchen_daen"
    start_urls = ['https://www.andersenstories.com/de/andersen_maerchen/list']



    def parse(self, response):
        full_links = [response.urljoin(sublink) for sublink in response.css('ul.bluelink > li > span > a::attr(href)').extract()]
        for link in full_links:
            yield response.follow(link, callback=self.get_stories)

    def get_stories(self, response):
        yield {
            'Herkunft': 'Dänisch',
            'Titel': response.css('h1.title::text').get(),
            'Inhalt': response.css('div.text::text').extract(),
            'Link': response
        }