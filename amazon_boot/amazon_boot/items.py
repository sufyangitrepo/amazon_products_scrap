# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import itemloaders
from itemloaders.processors import MapCompose,TakeFirst
import scrapy
from scrapy.item import Item, Field



def remmove_space(text: str) -> str:
    """
    :param text:
    :return: str
     this function is just to remove the start and end space of every new field
    """
    return text.strip()


"""
  
  This is an Item in this class we define the structure 
  of data that will be extracted from the any page
  in  this case one item will have four things 
  1. prod_title    # title of product
  2. prod_rating   # rating of this product                 
  3. prod_price    # product price
  4. prod_url      # product image url
  
"""


class AmazonBootItem(Item):

    title = scrapy.Field(
        input_processor=MapCompose(remmove_space),
        output_processor=TakeFirst()
    )
    rating = scrapy.Field(
        input_processor=MapCompose(remmove_space),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remmove_space),
        output_processor=TakeFirst(),
    )
    prod_url = scrapy.Field(
        input_processor=MapCompose(remmove_space),
        output_processor=TakeFirst(),
    )



