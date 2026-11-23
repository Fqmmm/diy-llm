import torch
x = torch.randn(32, 32)
print(f"x.stride(0):{x.stride(0)}")
print(f"x.stride(1):{x.stride(1)}")
y = x.view(1024) # 只是改变了看待数据的方式，内存地址没变
print(f"y.stride(0):{y.stride(0)}")
z = x.transpose(0, 1) # 修改了 stride，没有复制数据
print(f"z.stride(0):{z.stride(0)}")
print(f"z.stride(1):{z.stride(1)}")