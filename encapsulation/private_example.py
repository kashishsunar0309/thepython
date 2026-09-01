class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private property
p1 = person("Emil", 26)
print(p1.name)
print(p1.__age)  # This will cause an error.
