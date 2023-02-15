from datetime import datetime
import uuid
from product_inmemory_db import ProductInMemoryDb


class Product():

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.id = uuid.uuid1()
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

    def create(self,id:int):
        {'id':{self.id}, 'Title': {self.title},
        'Short_description': {self.short_description},
        'Description': {self.description},
        'Slug': {self.slug},
        'Permanent_link': {self.permalink},
        'Stock_keeping_Unit': {self.sku},
        'Price': {self.price},
        'Reqular_Price': {self.regular_price},
        'Sale_Price': {self.sale_price},
        'Manage_Stock' :{self.manage_stock},
        'Stock_Quantity': {self.stock_quantity},
        'Visible': {self.is_visible},'Date_Created':43,'Date_Modified':43}
        return self.__repr__()

    #this method shall be able read a product via id/uuid or ... from the the product datastructure (dictionary,list or maybe database)
    def read(self,id):
       for item in ProductInMemoryDb.product_list:
        if item['id']== id :
            return item
        return 'item not found'

    #this method shall be able to update product and amend the data structure for related product
    def update(self,id:int,**attributes):
       for item in ProductInMemoryDb.product_list:
        if item['id']== id:
            item.__init__(**attributes)
            return attributes
        print('item updated')

    #this method shall be able to remove the product
    def delete(self,id:int):
        for item in ProductInMemoryDb.product_list:
            if item['id']== id :
                ProductInMemoryDb.product_list.remove(item)
                print('item succssesfully deleted')

    #shall I get all products with staticmethod ? any better solution ? what about a class method ?
    # what is the diffrence ?
    # shall I seprate the datastructe from the class ? why? who? any better solution?
    #@staticmethod
    def list_all(self):
        for item in ProductInMemoryDb.product_list:
            print(item)

    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: N/A \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "