import datetime
from product import Product
from circle import Circle
from product_inmemory_db import ProductInMemoryDb
from product_injson_db import JsonDict

#instances
productdb=ProductInMemoryDb()
productjson=JsonDict()

def main():
    print('Hello World')
    
    mycircle = Circle(8)

    currentdatetime = datetime.datetime.utcnow()
    current_unixtimestamp = int(currentdatetime.timestamp())

    product_one = Product('Lenovo T410s',
        'Lenovo ThinkPad T410s Core i5 M560 2.66GHz 4GB RAM, WIN 10 14" AC ADAPTER',
        'The T410s provides a good companion for office use, that is well suited for business trips thanks to its 14.1 inch size and light weight.',
        'thinkbook-13x-gen-2-(13-inch-intel)',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/thinkbookx/thinkbook-13x-gen-2-(13-inch-intel)/21atcto1wwgb2?cid=gb:sem|se|google|G-UK-SEM-COMMERCIAL-PUBLIC-CCF-LF-Shopping-PLA-Brand-Commercial|Brand-CommercialLaptops-Intel',
        '21ATCTO1WWGB2',
        799.95,
        849.95,
        0,
        False,
        4,
        current_unixtimestamp,
        current_unixtimestamp,
        1)


    product_two = Product('Lenovo T530',
        'Lenovo 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)
    
    product_three= Product('mac T530',
        'mac 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)

   
    product_one.create(1)
    product_two.create(2)
    product_three.create(3)
    productdb.add({'name':'sara','age':17})
    print(ProductInMemoryDb.product_list)
    productjson.add({'id':1,'name':'saba','age':17})
    productjson.add({'id':2,'name':'sara','age':27})
    productjson.add({'id':3,'name':'shiva','age':51})
    productjson.add({'id':4,'name':'shiva','age':53})
    productjson.update(1,{'name':'sheida','age':47})
    productjson.read(2)
    productjson.read(3)
    #productjson.delete_json(2)
    product_one.list_all()
    print("-------------------------------------")
    print("Does Product one instance of <<Circle>> class?")
    #print(isinstance(product_one, Circle))
    print("Does Product one instance of <<Product>> class?")
    #print(isinstance(product_one, Product))

if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
