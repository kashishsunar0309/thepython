class Outer:
    def __init__(self):
        self.name = "Outer class"
        
    class inner:
        def __init__(self):
            self.name = "Inner class"
        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer)
