import abc
class imp(abc.ab):
    def __init__(self,p):
        super().__init__(p)
    def kaam(self):
        print(self.p)
i=input("enter the path")
obj=imp(i)
obj.kaam()
