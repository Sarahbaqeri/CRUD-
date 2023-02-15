import json
from abc_data_storage import DataStorage

class JsonDict(DataStorage):

    def __init__(self, file_path='/Users/sarahbagheri/python_samples-5/python_razm/sara-baq/razm1/product_crud/product_json.json') -> None:
        
        self.file_path = file_path

    def add(self,dict) -> None:
        items=self.read_file()
        items.append(dict)
    
        with open(self.file_path, 'w') as f:
                    json.dump(items,f)


    def update(self,dict,id:int) -> None:
        items=self.read_file()
        for item in items:
            if item['id'] == id:
                items.remove(item)
                items.append(dict)
                    
        with open (self.file_path, 'w') as f:
                json.dump(items,f)

    def read(self,id:int) -> dict:
        items=self.read_file()
        for item in items :
                if item['id']== id:
                    return item

    def delete(self,id:int) -> None:
        items=self.read_file()
        for item in items :
            if item['id']== id:
                items.remove(item)

        with open(self.file_path,'w') as f:
            json.dump(items,f)

    def read_file(self) -> list:
        with open (self.file_path, 'r') as f :
            return list(json.load(f))