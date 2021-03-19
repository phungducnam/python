danh_sach_mon = ["com", "pho", "hu tieu", "mi quang"]
for mon in danh_sach_mon:
    print(mon)

# Thu vien chon so ngau nhien
import random
i = random.randint(0, len(danh_sach_mon) -1)

#i = random.randint(0, 4)
print("chon dai mon", danh_sach_mon[i])

# sinh 1 bo so (khong trung) vietlotte (6 số) 6/55
# tìm số lớn nhat trong bo do
vietlotte655 = []
while len(vietlotte655) <6:
    lucky_number = random.randint(1, 55)
    if lucky_number in vietlotte655:
        continue
    vietlotte655.append(lucky_number)

print("Bo so cua ban", vietlotte655)
max_number = vietlotte655[0] # Phan tu dau
for number in vietlotte655:
    if number > max_number:
        max_number = number
print(f"So lon nhat la {max_number}")