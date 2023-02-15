from abc_data_storage import DataStorage

class ProductInMemoryDb(DataStorage):
    product_list=[]

    def __init__(self):
        pass
    @classmethod
    def add(cls,dict):
        cls.product_list.append(dict)
        return 1
    @classmethod
    def update(cls,dict):
        for item in cls.product_list:
            if item['id']==dict[id]:
                item.update(dict)
                return item
    @classmethod
    def read(cls,id:int):
        #for item in cls.product_list:
            #if item['id']== id :
                #return item
        next(item for item in cls.product_list if item['id']==id)
    @classmethod
    def delete(cls,id:int):
        for item in cls.product_list:
            if item['id']==id:
                cls.product_list.remove(item)
