import torch

x = torch.arange(12,dtype = torch.float32).reshape((3,4))
y = torch.tensor([1,2,3,4],[1,2,3,4],[0,1,2,3])

print(x == y)

sum1 = x.sum # 求和

#广播机制
a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))
#维度要一样：
(3,1) #把A复制成(3,2) 纵向复制一份
(1,2)#把B复制成（3，2） 横向复制两份

#访问
x[1,2] = 9
x[1,:]
x[0:2,:]
x[1:2,2:]

# 指针 id(variable)
Z = torch.zeros_like(y) # Z为零，数据类型和y里面一样


