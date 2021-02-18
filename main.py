# import p
# print(p)
import p
class child(p.pat):
    def __init__(self,path):
        super().__init__(path)
    def cal(self):
        print(path)
path=input("enter the path :")
obj=child(path)
obj.cal()