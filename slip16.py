class Rect:
    def __init__(self, l2, w2):
         self.l=l2
         self.w=w2
    def RectArea(self):
        self.a=self.l*self.w
        print("Area of Rectangle:",self.a)
    def Rectper(self): 
            self.p = 2 *(self.l+self.w)
            print("perimeter of  Rectangle:",self.p)
            #main body
l1 = int(input("enter length:"))

w1 = int(input("enter width:"))
obj = Rect(l1,w1)
obj.RectArea()
obj.Rectper()

