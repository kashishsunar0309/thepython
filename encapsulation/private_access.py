class person:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    
    def get_age(self):
        return self._age

p1 = person("Ashish",17)
print(p1.get_age())