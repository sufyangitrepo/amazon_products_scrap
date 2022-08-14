import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import AmazonBootItem

"""
  Amazon Spider is crawlspider that will extract the all urls of given starting url
  Link Extractor will extract links base on given Rule and take a function 
  that function is used to extract the data from current page  
  it has three class attributes 
  name              # Name of spider
  allowed domains   # all domains that used for data extracting
  start urls        # urls where to start extracting the data
  
"""


class AmazonSpider(CrawlSpider):

    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['http://www.amazon.com/']

    rules = [
        # Rule for links and with link extractor
        Rule(LinkExtractor(allow='www.amazon.com', ), callback='parse_product', follow=True, )
    ]

    def parse_product(self, response):
        """
        :param response:
        :return:
        it will used to parse the product page and will extract
        the four things
        title , price , image url , rating
        ItemLoader will be used

        """
        name = response.xpath('//span[@id="productTitle"]/text()').extract_first()
        if name:
            scrapy.Request()
            item = AmazonBootItem()  # Item Instance
            # ItemLoader
            loader = ItemLoader(item=item, selector=response)
            loader.add_value('title', name)
            loader.add_xpath('rating', '//*[@id="averageCustomerReviews"]/span[3]/a/span/text()')
            loader.add_xpath(
                'price', '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')
            url = response.xpath('//*[@id="main-video-container"]/div/div[1]/video/@src').get()
            if url:
                loader.add_value('prod_url', url)
            else:
                loader.add_xpath('prod_url', '//*[@id="imgTagWrapperId"]/img/@src')

            yield loader.load_item()
