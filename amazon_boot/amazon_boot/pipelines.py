# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter
from enum import Enum

"""
  All constants required for database are placed in DbConstants
"""

class DbConstant(Enum):
    TB_NAME = 'product_tb'
    DB_NAME = 'mydb.db'
    ID_COL = 'id'
    NAME_COL = 'prod_name'
    PRICE_COL = 'prod_price'
    RATING_COL = 'rating'
    CREATE_TB_QUERY = 'CREATE TABLE {} ({} INTEGER PRIMARY KEY AUTOINCREMENT, {} TEXT, {} TEXT, {} TEXT)' \
        .format(TB_NAME, ID_COL, NAME_COL, PRICE_COL, RATING_COL)
    DROP_TB_QUERY = """DROP TABLE IF EXISTS {}""".format(TB_NAME)

"""
  In this Pipeline item is processed and insert into database
"""

class AmazonBootPipeline:

    def __init__(self):
        """
           in this function creating database connection
            and table in that database by calling two functions
            create_connection(),
            create_table()
        """

        self.cursor = None
        self.connection = None
        self.create_connection()
        self.create_table()

    def process_item(self, item, spider):
        """
        :param item:
        :param spider:
        :return: item

         this function in pipelines is used to process item
         inserting every item into database by calling insert method

        """
        self.insert(item)
        return item

    def create_table(self):
        """
        :return: None
        in this function create table is executed
        """
        self.cursor.execute(DbConstant.CREATE_TB_QUERY)

    def create_connection(self):
        """
        :return: None
        this funtion will create database and build connection with database
        and create cursor object for that database

        """
        self.connection = sqlite3.connect(DbConstant.DB_NAME, )
        self.cursor = self.connection.cursor()

    def insert(self, item):
        """
        :param item:
        :return: None
        this function will insert given item into table that is create in database
        with reference of cursor
        """
        self.cursor.execute('INSERT INTO {} VALUES({}, {}, {}, {})'.format(
            DbConstant.TB_NAME,
            item['name'],
            item['price'],
            item['rating'],
            item['stock']
        ))
        self.cursor.commit()
