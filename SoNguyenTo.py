# Nhap
#Nhap vao 1 so, xuất ra số N đó có phải số nguyen to hay k
#

N = 0
while True:
    try:
        N = int(input("Nhap so nguyen duong <= 100: "))
        if N > 0 and N <= 100:
            break # thoat vòng lặp
    except:
        print("Khong phai so nguyen")

print(f"Da nhap N = {N}")

la_so_nguyen_to = True
i = 2
while i < N :
    if N % i == 0: # chia hết ( chia du 0 )
        la_so_nguyen_to = False
        break
    i = i + 1

kq = f"{N} la so Ngto" if la_so_nguyen_to else f"{N} ko la so nguyen to"
print(kq)

# in cac so nguyen to nho hon N
step = 2
print(f"cac so nguyen to nho hon {N} la: ")
while step < N:
    if la_so_nguyen_to(step):
        print(step, "\t")
    step = step + 1

# In ra N so nguyen to dau tien
count = 0
step = 2
danhsach = [] # mang list
while count <= N:
    if La_So_Nguyen_To(step):
        danhsach.append(step)
        count = count + 1
    step = step + 1
print(danhsach)