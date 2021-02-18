class parent:
    def __init__(self,inn):
        self.inn=inn
        print(self.inn)
    def abc(self):
        self.a=5
        print(self.a)
    def de(self):
        self.e=6
        print(self.a)
        print(self.inn)
# # obj=parent()
# # obj.abc()
# # obj.de()
# def a():
#     a=5
#     b=4
#     print(a+b)
class child(parent):
    def __init__(self,val):
        super().__init__(val)
        # print(val)


obj=child(85)