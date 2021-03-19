def addTwo(a, b):
    return a + b

a = 11
b = 19
print(addTwo(a, b))
#print(addTwo("11", b))
print(addTwo("Nhat", "Nghe"))
print(addTwo([1,3,5], [2,4,6]))


##### In bang cửu chuong
import random
def In_bang_cuu_chuong(N: int):
    for i in range(1,11):
        print(f"{N} x {i} = {N*i} \t {random.random()}")

In_bang_cuu_chuong(5)
print(range(1,11))
#print(type(range(1,11)))
print(list(range(1,11)))