import scrapy


class AmazonScrapperSpider(scrapy.Spider):
    name = "amazon_scrapper"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=best+laptops+under+under+%241000&page=2&xpid=Nl9IauHK64Hpn&crid=W0MGZZSBRDLN&qid=1741587067&sprefix=%2Caps%2C289&ref=sr_pg_2"]

    def parse(self, response):
        
        divs = response.css('div.puis-card-container.s-card-container')
        print("answer  : ",len(divs))
        for div in divs:
            html_content = div.get()
            yield {
            'html': html_content
            }
