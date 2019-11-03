from Multiply import Mul
from Subtra import Sub
from Module import Mod
import random

def Test(fuc):
    for idx in range(10000):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        #print("a=", a, "b=", b)
        while(b!=0):
            c=a%b
            a=b
            b=c
        print(a,fuc(a,b).Run())
        assert a==fuc(a,b).Run()

if __name__=="__main__":
    ans=Mul(9,9)
    print("乘法运算的结果为：",ans.Run())
    ans=Sub(7,8)
    print("减法运算的结果为：",ans.Run())
    ans=Mod(26,9)
    print("取模运算的结果为：",ans.Run())
    Test(Mod)