import numpy as np
a1=np.array([[1,2],[3,4],[5,6]])#np.arrary()初始化数据，此处初始化了一个三行二列数组
a2=np.arange(6)#创建长度为6元素(0~5)的一维数组
a3=np.linspace(0,10,7)#创建首位是0，末位是10，含有7个数的等差数列
a4=np.ones((2,3))#创建3行2列都是1的数组
a5=np.logspace(0,2,5)#创建首位是10的0次方，末位是10的4次方，含有5个数的等比数列

#hstack函数能将两个多维数组在水平方向上折叠，通过vstack函数能将两个多维数组在垂直方向上堆叠
#eg:
a=np.array([[1,2],[3,4],[5,6]])
b=np.array([[-1,-2],[-3,-4],[-5,-6]])
c=np.vstack((a,b))#表示在垂直方向上堆叠
print(c)
#[[ 1  2]
# [ 3  4]运行结果
# [ 5  6]
# [-1 -2]
# [-3 -4]
# [-5 -6]]
d=np.hstack((a,b))
print(d)#横向堆叠示例结果如下
#[[ 1  2 -1 -2]
#[ 3  4 -3 -4]
#[ 5  6 -5 -6]]  
e=np.array([[1],[2]])
print(e)
#[[1]
# [2]]
f=[10,20,30]
print(f)#输出结果：[10, 20, 30]
print(e+f)
#[[11 21 31]
# [12 22 32]]
print(a1)
#[[1 2]
# [3 4]
# [5 6]]
#a[0]代表的是[1，2]
#a[1]代表的是[3，4]
#a[0,1]代表的是2
#a.ndim表示a的数组维数
#a.size表示a的数组个数
#a.dype表示a的元素类型