

class Mul():
    '''
    定义规则：
    1、ab->rp
    2、ac->q
    3、p->ab,q->c
    补充：还可以设置中间变量来控制并行和串行
    '''
    def __init__(self,m,n):
        self.a,self.b=self.Max_Min(m,n)
        self.c=1
        self.r=0
        self.p=0
        self.q=0

    def Max_Min(self,m,n):
        if n>m:
            return n,m
        return m,n

    def Run(self):
        while(self.a>0):
            #第一个规则：ab->rp
            self.a-=self.b
            self.r+=self.b
            self.p=self.b
            self.b = 0

            #第二个规则：ac->q
            self.a-=self.c
            self.q=self.c
            self.c = 0

            #第三个规则：p->ab,q->c
            self.a+=self.p
            self.b+=self.p
            self.c=self.q
            self.q=0

        return self.r