

class Sub():

    def __init__(self,m,n):
        self.a,self.b=m,n

    def Run(self):
        Min=min(self.a,self.b)
        self.a-=Min
        self.b-=Min
        if self.a!=0:
            return self.a
        if self.b!=0:
            return -self.b
        return 0
