class Myclass:
    __privateVar = 27
    def __privMeth(self):
      print("Im inside class Myclass")
    def hello(self):
      print("Private Variable value:", Myclass.__privateVar)
foo = Myclass()
foo.hello()
