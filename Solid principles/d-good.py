

from abc import ABC, abstractmethod

class DataSource(ABC):
    def __init__(self,path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass
    @abstractmethod
    def write_data(self, data):
        pass

class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data
    def write_data(self,data):
        with open(self.path,'w') as file:
            file.write(data)

class DbDataSource(DataSource):
    def read_data(self):
        return "data from database"
    def write_data(self,data):
        print(f"write {data} to database")

class TextOperations:
    def __init__(self, data):
        self.data = data

    def search_for_word(self, word):
        return word in self.data

    def count_occurences(self, word):
        return self.data.count(word)

file = TextDataSource("output.txt")
db = DbDataSource("customers")

obj = TextOperations(file.read_data())
print(f"{obj.search_for_word('more')}")
print(f"{obj.count_occurences('be')}")

obj = TextOperations(db.read_data())
print(f"{obj.search_for_word('data')}")
print(f"{obj.count_occurences('from')}")