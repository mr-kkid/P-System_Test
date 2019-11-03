from Subtra import Sub

class Mod():

    def __init__(self,m,n):
        self.a,self.b=self.Max_Min(m,n)
        self.c=0

    def Run(self):
        while(self.b):
            self.c=Sub(self.a,self.b).Run()
            self.a=self.b
            self.b=self.c
            self.a,self.b=self.Max_Min(self.a,self.b)
        return self.a

    def Max_Min(self,m,n):
        if n>m:
            return n,m
        return m,n